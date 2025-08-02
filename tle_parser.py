import requests
from pathlib import Path
from datetime import datetime


DATA_DIR = Path("data/imported_tle")
URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=csv"

def import_tle( DATA_DIR = DATA_DIR, URL = URL ):

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    imported_tle_path = DATA_DIR / f'active_{current_time}.csv'

    resp = requests.get(URL)
    resp.raise_for_status()

    imported_tle_path.write_text(resp.text, encoding="utf-8")

    print(f'Файл сохранён по пути {imported_tle_path}')

if __name__ == "__main__":
    import_tle()