import pandas as pd
import numpy as np

df = pd.read_pickle("0825_new_data.pkl")
df_norm = df.copy(deep=True)
idx = pd.IndexSlice
ids = set()

for id, _, _ in df.index:
    ids.add(id)

ids = sorted(ids)

# features = ['kda', 'dealt', 'dpm', 'dealttaken', 'kill_at14', 'diffdpm', 'diffgold', 'cs100', 'goldearned100', 'visionscore100', 'dragon100', 'baron100', 'tower100', 'cs200', 'goldearned200', 'visionscore200', 'dragon200', 'baron200', 'tower200', 'win', 'tier']
features = ['kda', 'dealt', 'dpm', 'dpg', 'dpd', 'dtpm', 'goldearned', 'kills', 'object', 'diffdpg', 'diffcs','gpm','xpm']
i = 0
for id in ids:
    for feature in features:
        val = df_norm.loc[idx[id, :, feature]].values
        val = np.concatenate(val)
        a = val.min()
        b = val.max()
        print(feature, val, a, b)
        if a == b:
            val_norm = [1] * 10
        else:
            val_norm = (val - a) / (b - a)
        df_norm.loc[idx[id, 100, feature]] = val_norm[0:5]
        df_norm.loc[idx[id, 200, feature]] = val_norm[5:10]
    print(i); i += 1
df_norm.to_pickle("0825_new_all_data_norm.pkl")