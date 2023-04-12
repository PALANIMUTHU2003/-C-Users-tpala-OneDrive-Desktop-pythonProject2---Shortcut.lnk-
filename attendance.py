import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

images = []
classNames = []
path = 'C:/Users/tpala/PycharmProjects/pythonProject2/images'
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findencodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[4]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('C:/Users/tpala/PycharmProjects/pythonProject2/Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


ElonMusk = "Tesla"  # Option 2: Remove the space in the variable name
if len(ElonMusk) < 4:
    print("Length of ElonMusk is less than 4")
else:
    print("Length of ElonMusk is greater than or equal to 4")

cap = cv2.VideoCapture(0)

while True:
    success, Elon_Musk = cap.read()
    #img = captureScreen()
    img = cv2.resize(Elon_Musk,(0,0),None,0.25,0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img)
    encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(Elon_Musk, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(Elon_Musk, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(Elon_Musk, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)
