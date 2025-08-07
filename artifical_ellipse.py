from pathlib import Path
from data_worker import load_raw_data

ELLIPSE_DATA_DIR = Path("data/ellipse_data")

def add_ellipse(sigma_x=0.5, sigma_y=0.5, sigma_z=0.5):
    df, filename = load_raw_data()  # загружаем исходные TLE

    # Добавляем колонки с параметрами эллипса ошибок
    df['sigma_x'] = sigma_x
    df['sigma_y'] = sigma_y
    df['sigma_z'] = sigma_z

    timestamp_part = filename.replace("active_", "").replace(".csv", "")
    ellipse_filename = f"ellipse_data_{timestamp_part}.csv"

    ELLIPSE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    ellipse_csv_path = ELLIPSE_DATA_DIR / ellipse_filename
    df.to_csv(ellipse_csv_path, index=False)
    print(f"Данные с параметрами эллипса для каждого спутника сохранены в {ellipse_csv_path}")


if __name__ == "__main__":
    add_ellipse()

