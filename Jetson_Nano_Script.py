import logging
import datetime
import sys
import time
import math
import cv2
import numpy as np
from openpose import pyopenpose as op
from sklearn.externals import joblib

def vector(pose):
    row_count = 0
    values = []
    vector = []
    if '[[[' in pose:
        row_count += 1
        pose = pose.replace('[[[', '')
        for x in pose.split():
            if ']]]' in x:
                x = x.replace(']]]', '')
                if len(x) >= 1:
                    y = float(x)
                    vector.append(y)
                values.append(vector)
                del vector
                vector = []
            else:
                x = x.replace('[', '')
                x = x.replace(']', '')
                if len(x) >= 1:
                    y = float(x)
                    vector.append(y)
                else:
                    continue
    return(values)

def run_webcam():
    pose_new = []
    print('starting')
    fps_time = 0

    params = dict()
    params["model_folder"] = "models/"
    params["net_resolution"] = "-1x80"
#    params["profile_speed"] = 15

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    # file1 = open(r"Final_Test.txt","a")
    count = 0
    # Starting Camera
    cap = cv2.VideoCapture("nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)1280, height=(int)720, "
        "format=(string)NV12, framerate=(fraction)60/1 ! "
        "nvvidconv flip-method=0 ! "
        "video/x-raw, width=(int)1280, height=(int)720, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink")

    while cap.isOpened():
        # print('Im in while loop')
       # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
       # out_video = cv2.VideoWriter('/tmp/output.avi', fourcc, 30.0,(640,480))
        ret_val, img = cap.read()
        if ret_val == True:
            datum = op.Datum()
            imageToProcess = img
            datum.cvInputData = imageToProcess
            opWrapper.emplaceAndPop([datum])
            # file1.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
            # file1.write(str(datum.poseKeypoints))
            pose = str(datum.poseKeypoints)
            # print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
            # print("Body Key Points: \n" + str(datum.poseKeypoints))
            #out_video.write(imageToProcess)
            cv2.putText(datum.cvOutputData,'OpenPose using Python-OpenCV',(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.imshow("OpenPose 1.5.1 - Tutorial Python API", datum.cvOutputData)

            pose_new = vector(pose)
            clf_from_joblib = joblib.load('Model.pkl')
            predictions = clf_from_joblib.predict(pose_new)
            print(predictions)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    out_video.release()
    cv2.destroyAllWindows()
    cap.release()
    # file1.close()


if __name__ == "__main__":
    run_webcam()


