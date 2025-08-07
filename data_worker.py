from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/imported_tle")
ELLIPSE_DATA_DIR = Path("data/ellipse_data")

def load_raw_data():
    files = list(DATA_DIR.glob("active_*.csv"))
    if not files:
        raise FileNotFoundError(f"Нет файлов active_*.csv в {DATA_DIR}")
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    print(f"Импортирован последний актуальный файл {latest_file.name}")
    return pd.read_csv(latest_file), latest_file.name

def load_ellipse_data():
    files = list(ELLIPSE_DATA_DIR.glob("ellipse_data_*.csv"))
    if not files:
        raise FileNotFoundError(f"Нет файлов ellipse_data_*.csv в {ELLIPSE_DATA_DIR}")
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    print(f"Импортирован последний актуальный файл {latest_file.name}")
    return pd.read_csv(latest_file), latest_file.name

