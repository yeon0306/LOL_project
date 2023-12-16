import pandas as pd
import numpy as np

df = pd.read_csv("./3일치 통계데이터/0915_top.csv")
df_mid = pd.read_csv("./3일치 통계데이터/0915_mid.csv")
df_jug = pd.read_csv("./3일치 통계데이터/0915_jug.csv")
df_spt = pd.read_csv("./3일치 통계데이터/0915_spt.csv")
df_adc = pd.read_csv("./3일치 통계데이터/0915_adc.csv")

print(f"TOP 데이터 수 : {len(df)}")
print(f"MID 데이터 수 : {len(df_mid)}")

df_list = []
df_id_list = []
features = ['kda', 'dealt', 'dpm', 'dpg', 'dpd', 'dtpm', 'goldearned', 'kills', 'object', 'diffdpg', 'diffcs','gpm','xpm', 'win', 'tier']
for j in range(0,len(df),2):
    sub_df_list = []
    sub_df_id_list = []
    blue_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j]['kda'],             df_mid.iloc[j]['kda'],            df_jug.iloc[j]['kda'],            df_spt.iloc[j]['kda'],            df_adc.iloc[j]['kda']],
            [df.iloc[j]['dealt'],           df_mid.iloc[j]['dealt'],          df_jug.iloc[j]['dealt'],          df_spt.iloc[j]['dealt'],          df_adc.iloc[j]['dealt']],
            [df.iloc[j]['dpm'],             df_mid.iloc[j]['dpm'],            df_jug.iloc[j]['dpm'],            df_spt.iloc[j]['dpm'],            df_adc.iloc[j]['dpm']],
            [df.iloc[j]['dpg'],             df_mid.iloc[j]['dpg'],            df_jug.iloc[j]['dpg'],            df_spt.iloc[j]['dpg'],            df_adc.iloc[j]['dpg']],
            [df.iloc[j]['dpd'],             df_mid.iloc[j]['dpd'],            df_jug.iloc[j]['dpd'],            df_spt.iloc[j]['dpd'],            df_adc.iloc[j]['dpd']],
            [df.iloc[j]['dtpm'],            df_mid.iloc[j]['dtpm'],           df_jug.iloc[j]['dtpm'],           df_spt.iloc[j]['dtpm'],           df_adc.iloc[j]['dtpm']],
            [df.iloc[j]['goldearned'],      df_mid.iloc[j]['goldearned'],     df_jug.iloc[j]['goldearned'],     df_spt.iloc[j]['goldearned'],     df_adc.iloc[j]['goldearned']],
            [df.iloc[j]['kills'],           df_mid.iloc[j]['kills'],          df_jug.iloc[j]['kills'],          df_spt.iloc[j]['kills'],          df_adc.iloc[j]['kills']],
            [df.iloc[j]['object'],          df_mid.iloc[j]['object'],         df_jug.iloc[j]['object'],         df_spt.iloc[j]['object'],         df_adc.iloc[j]['object']],
            [df.iloc[j]['diffdpg'],         df_mid.iloc[j]['diffdpg'],        df_jug.iloc[j]['diffdpg'],        df_spt.iloc[j]['diffdpg'],        df_adc.iloc[j]['diffdpg']],
            [df.iloc[j]['diffcs'],          df_mid.iloc[j]['diffcs'],         df_jug.iloc[j]['diffcs'],         df_spt.iloc[j]['diffcs'],         df_adc.iloc[j]['diffcs']],
            [df.iloc[j]['gpm'],             df_mid.iloc[j]['gpm'],            df_jug.iloc[j]['gpm'],            df_spt.iloc[j]['gpm'],            df_adc.iloc[j]['gpm']],
            [df.iloc[j]['xpm'],             df_mid.iloc[j]['xpm'],            df_jug.iloc[j]['xpm'],            df_spt.iloc[j]['xpm'],            df_adc.iloc[j]['xpm']],
            [df.iloc[j]['win'],             df_mid.iloc[j]['win'],            df_jug.iloc[j]['win'],            df_spt.iloc[j]['win'],            df_adc.iloc[j]['win']],
            [df.iloc[j]['tier'],            df_mid.iloc[j]['tier'],           df_jug.iloc[j]['tier'],           df_spt.iloc[j]['tier'],           df_adc.iloc[j]['tier']]
        ],
        columns=['TOP','MID', 'JUG', 'SPT', 'ADC'],
        index=['kda', 'dealt', 'dpm', 'dpg', 'dpd', 'dtpm', 'goldearned', 'kills', 'object', 'diffdpg', 'diffcs','gpm','xpm', 'win', 'tier']
    )
    sub_df_list.append(blue_data_frame)
    sub_df_id_list.append(df.iloc[j]['tid'])
    red_data_frame = pd.DataFrame(
        [
            # [TOP, MID]
            [df.iloc[j+1]['kda'],             df_mid.iloc[j+1]['kda'],            df_jug.iloc[j+1]['kda'],            df_spt.iloc[j+1]['kda'],            df_adc.iloc[j+1]['kda']],
            [df.iloc[j+1]['dealt'],           df_mid.iloc[j+1]['dealt'],          df_jug.iloc[j+1]['dealt'],          df_spt.iloc[j+1]['dealt'],          df_adc.iloc[j+1]['dealt']],
            [df.iloc[j+1]['dpm'],             df_mid.iloc[j+1]['dpm'],            df_jug.iloc[j+1]['dpm'],            df_spt.iloc[j+1]['dpm'],            df_adc.iloc[j+1]['dpm']],
            [df.iloc[j+1]['dpg'],             df_mid.iloc[j+1]['dpg'],            df_jug.iloc[j+1]['dpg'],            df_spt.iloc[j+1]['dpg'],            df_adc.iloc[j+1]['dpg']],
            [df.iloc[j+1]['dpd'],             df_mid.iloc[j+1]['dpd'],            df_jug.iloc[j+1]['dpd'],            df_spt.iloc[j+1]['dpd'],            df_adc.iloc[j+1]['dpd']],
            [df.iloc[j+1]['dtpm'],            df_mid.iloc[j+1]['dtpm'],           df_jug.iloc[j+1]['dtpm'],           df_spt.iloc[j+1]['dtpm'],           df_adc.iloc[j+1]['dtpm']],
            [df.iloc[j+1]['goldearned'],      df_mid.iloc[j+1]['goldearned'],     df_jug.iloc[j+1]['goldearned'],     df_spt.iloc[j+1]['goldearned'],     df_adc.iloc[j+1]['goldearned']],
            [df.iloc[j+1]['kills'],           df_mid.iloc[j+1]['kills'],          df_jug.iloc[j+1]['kills'],          df_spt.iloc[j+1]['kills'],          df_adc.iloc[j+1]['kills']],
            [df.iloc[j+1]['object'],          df_mid.iloc[j+1]['object'],         df_jug.iloc[j+1]['object'],         df_spt.iloc[j+1]['object'],         df_adc.iloc[j+1]['object']],
            [df.iloc[j+1]['diffdpg'],         df_mid.iloc[j+1]['diffdpg'],        df_jug.iloc[j+1]['diffdpg'],        df_spt.iloc[j+1]['diffdpg'],        df_adc.iloc[j+1]['diffdpg']],
            [df.iloc[j+1]['diffcs'],          df_mid.iloc[j+1]['diffcs'],         df_jug.iloc[j+1]['diffcs'],         df_spt.iloc[j+1]['diffcs'],         df_adc.iloc[j+1]['diffcs']],
            [df.iloc[j+1]['gpm'],             df_mid.iloc[j+1]['gpm'],            df_jug.iloc[j+1]['gpm'],            df_spt.iloc[j+1]['gpm'],            df_adc.iloc[j+1]['gpm']],
            [df.iloc[j+1]['xpm'],             df_mid.iloc[j+1]['xpm'],            df_jug.iloc[j+1]['xpm'],            df_spt.iloc[j+1]['xpm'],            df_adc.iloc[j+1]['xpm']],
            [df.iloc[j+1]['win'],             df_mid.iloc[j+1]['win'],            df_jug.iloc[j+1]['win'],            df_spt.iloc[j+1]['win'],            df_adc.iloc[j+1]['win']],
            [df.iloc[j+1]['tier'],            df_mid.iloc[j+1]['tier'],           df_jug.iloc[j+1]['tier'],           df_spt.iloc[j+1]['tier'],           df_adc.iloc[j+1]['tier']]
        ],
        columns=['TOP','MID', 'JUG', 'SPT', 'ADC'],
        index=['kda', 'dealt', 'dpm', 'dpg', 'dpd', 'dtpm', 'goldearned', 'kills', 'object', 'diffdpg', 'diffcs','gpm','xpm', 'win', 'tier']
    )
    sub_df_list.append(red_data_frame)
    sub_df_id_list.append(df.iloc[j + 1]['tid'])
    sub_df_feature = pd.concat(sub_df_list, keys=sub_df_id_list, names=['team', 'feature'])
    df_list.append(sub_df_feature)
    df_id_list.append(df.iloc[j]['id'] // 10)
    blue_id = df.iloc[j]['id'] // 10
    red_id = df.iloc[j + 1]['id'] // 10
    if (blue_id != red_id):
        print("아이디가 안맞아요")
    print(j)

df_feature = pd.concat(df_list, keys=df_id_list, names=['id'])
df_feature.to_pickle("0915_new_all_data.pkl")
print(df_feature.head())