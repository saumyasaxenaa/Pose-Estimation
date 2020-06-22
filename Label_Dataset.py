from csv import reader
from csv import writer

text = '1'

with open('/Users/saumyasaxena/Desktop/untitled folder/Pose3.csv', 'r') as read_obj, \
    open('/Users/saumyasaxena/Desktop/untitled folder/Pose3_new.csv','w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)

    for row in csv_reader:
        row.append(text)
        csv_writer.writerow(row)

