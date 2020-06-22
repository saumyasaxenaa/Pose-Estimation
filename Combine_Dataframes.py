import pandas as pd

df1 = pd.read_csv('/Users/saumyasaxena/Desktop/untitled folder/New/Pose1_new.csv')
df2 = pd.read_csv('/Users/saumyasaxena/Desktop/untitled folder/New/Pose2_new.csv')
df3 = pd.read_csv('/Users/saumyasaxena/Desktop/untitled folder/New/Pose3_new.csv')
# print(df1)
# print(df2)

concat = pd.concat([df1,df2,df3])
print(concat)
concat.to_csv('Master.csv')