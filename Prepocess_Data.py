import pandas as pd
values = []
vector = []
count = 0
row_count = 0
fo = open('/Users/saumyasaxena/Desktop/New Data/Data_txt/Pose1_Front.txt','r')
lines = fo.readlines()
for line in lines:
    if '[[[' in line:
        row_count += 1
    line = line.replace('[[[','')
    # line = line.replace(']]]','')
    # line = line.replace('[','')
    # line = line.replace(']','')
    for x in line.split():
        if ']]]' in x:
            x = x.replace(']]]','')
            if len(x) >= 1:
                y = float(x)
                vector.append(y)
            values.append(vector)
            del vector
            vector = []
        else:
            x = x.replace('[', '')
            x = x.replace(']','')
            if len(x) >= 1:
                y = float(x)
                vector.append(y)
            else:
                continue


    print(values)
    print(row_count)
df = pd.DataFrame(values)
df.to_csv('Pose3_Back166.csv', index=False)