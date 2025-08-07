from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/imported_tle")
NOISE_DATA_DIR = Path("data/noisy_data")
NOISE_FILE = NOISE_DATA_DIR / "noisy_positions.csv"

def load_raw_data():
    files = list(DATA_DIR.glob("active_*.csv"))
    if not files:
        raise FileNotFoundError(f"Нет файлов active_*.csv в {DATA_DIR}")
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    print(f"Импортирован последний актуальный файл {latest_file.name}")
    return pd.read_csv(latest_file)

def load_noisy_data():
    if not NOISE_FILE.exists():
        raise FileNotFoundError(f"Нет файла noisy_positions.csv в {NOISE_DATA_DIR}")
    return pd.read_csv(NOISE_FILE)

