bad_words = ['Timestamp']

with open('../Project/Pose3_Back1_new1') as oldfile, open('../Project/Pose3_Back_FIIII.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

