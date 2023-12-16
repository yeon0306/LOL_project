header = ['label']

for j in range(0,25):
    str_val = 'b' + str(j)
    header.append(str_val)

for j in range(0,25):
    str_val = 'r' + str(j)
    header.append(str_val)

print(header)

import pickle
with open('0825_new_match_data_all.pkl', 'rb') as f:
    match_data = pickle.load(f)

import csv
with open('0825_new_match_data_all.csv', 'w', newline='') as fc:
    writer = csv.writer(fc)
    writer.writerow(header)
    j=0
    for match in match_data:
        data = [match['win']]
        for bd in match['blue']: data.append(bd)
        for rd in match['red']: data.append(rd)
        writer.writerow(data)
        print(j); j+=1