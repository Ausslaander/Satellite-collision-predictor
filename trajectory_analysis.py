from data_worker import load_ellipse_data
import numpy as np
import pandas as pd
import datetime
from skyfield.api import load, EarthSatellite


def analyze_collisions():
    df, filename = load_ellipse_data()
    return(compute_trajectories(df))

def compute_trajectories(df, step_seconds=30, duration_minutes=120):
    ts = load.timescale()
    all_trajectories = []

    for idx, row in df.iterrows():
        # Получаем время эпохи из TLE спутника
        epoch_str = row['EPOCH']
        epoch_dt = datetime.datetime.fromisoformat(epoch_str)
        start_time_utc = (
            epoch_dt.year, epoch_dt.month, epoch_dt.day,
            epoch_dt.hour, epoch_dt.minute, epoch_dt.second
        )

        t0 = ts.utc(*start_time_utc)
        total_seconds = duration_minutes * 60
        times = ts.utc(
            epoch_dt.year,
            epoch_dt.month,
            epoch_dt.day,
            epoch_dt.hour,
            epoch_dt.minute,
            epoch_dt.second + np.arange(0, total_seconds + step_seconds, step_seconds)
        )

        sat = EarthSatellite.from_omm(element_dict=row.to_dict(), ts=ts)
        positions = sat.at(times).position.km.T

        sigma_x = row.get('sigma_x', 0.5)
        sigma_y = row.get('sigma_y', 0.5)
        sigma_z = row.get('sigma_z', 0.5)

        for i, pos in enumerate(positions):
            all_trajectories.append({
                "OBJECT_NAME": row["OBJECT_NAME"],
                "NORAD_CAT_ID": row["NORAD_CAT_ID"],
                "time_utc": times[i].utc_iso(),
                "X_km": pos[0],
                "Y_km": pos[1],
                "Z_km": pos[2],
                "sigma_x": sigma_x,
                "sigma_y": sigma_y,
                "sigma_z": sigma_z,
            })
    traj_df = pd.DataFrame(all_trajectories)
    return traj_df

print(analyze_collisions())