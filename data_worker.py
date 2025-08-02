from pathlib import Path

DATA_DIR = Path("data/imported_tle")

def load_raw_data():
    files = list(DATA_DIR.glob("active_*.csv"))
    if not files:
        raise FileNotFoundError(f"Нет файлов active_*.csv в {DATA_DIR}")
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    print(f"Импортирован последний актуальный файл {latest_file.name}")
    return latest_file