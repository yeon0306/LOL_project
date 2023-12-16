import pandas as pd
import numpy as np

df = pd.read_pickle("0917_new_all_data_norm.pkl")
idx = pd.IndexSlice

position = ['TOP', 'MID', 'JUG', 'SPT', 'ADC']
numeric_features = ['kda', 'dealt', 'dpm', 'dpg', 'dpd', 'dtpm', 'goldearned', 'kills', 'object', 'diffdpg', 'diffcs','gpm','xpm']

ids = set()
for id, _, _ in df.index: ids.add(id)
ids = sorted(ids)
match_data = []

for id in ids:
    blue_data = df.loc[idx[id, 100, numeric_features]].values
    blue_data = [float(val) for val in blue_data.ravel()]  # Convert all elements to float
    red_data = df.loc[idx[id, 200, numeric_features]].values
    red_data = [float(val) for val in red_data.ravel()]  # Convert all elements to float

    # Convert 'win' to numeric (0 or 1)
    blue_win = df.loc[idx[id, 100, 'win']].values
    win = int(blue_win[0])  # Assuming 'win' is either 0 or 1

    blue_sum = sum(blue_data)
    red_sum = sum(red_data)

    forecast = 0
    if blue_sum > red_sum: forecast = 1

    acc = 0
    if win == forecast: acc = 1

    match_info = {
        "id": id,
        "blue": blue_data,
        "red": red_data,
        "win": win,
        "forecasts": forecast,
        "acc": acc
    }
    print(id, win, forecast, acc)
    match_data.append(match_info)
import pickle

with open('0917_new_match_data_all.pkl', 'wb')as f:
    pickle.dump(match_data, f)

