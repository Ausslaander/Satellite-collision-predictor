from pathlib import Path
from data_worker import load_raw_data
import pandas as pd
import numpy as np
from skyfield.api import load, EarthSatellite

NOISE_DATA_DIR = Path("data/noisy_data")
DATA_DIR = Path("data/imported_tle")

def add_noise(sigma=0.5, samples_per_sat=100, time_utc=(2025, 8, 1, 12, 0, 0)):
    df = pd.read_csv(load_raw_data())

    ts = load.timescale()
    t = ts.utc(*time_utc)


    all_noisy_points = []

    for idx, row in df.iterrows():
        sat = EarthSatellite.from_omm_dataframe(df.iloc[[idx]], ts)
        pos = sat.at(t).position.km

        noise = np.random.normal(0, sigma, size=(samples_per_sat, 3))
        noisy_positions = pos + noise

        for point in noisy_positions:
            all_noisy_points.append({
                "OBJECT_NAME": row["OBJECT_NAME"],
                "NORAD_CAT_ID": row["NORAD_CAT_ID"],
                "X_km": point[0],
                "Y_km": point[1],
                "Z_km": point[2]
            })
    noisy_df = pd.DataFrame(all_noisy_points)
    NOISE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    noisy_csv_path = NOISE_DATA_DIR / "starlink_noisy_positions.csv"
    noisy_df.to_csv(noisy_csv_path, index=False)
    print(f"Шумные координаты сохранены в {noisy_csv_path}")

    return None

