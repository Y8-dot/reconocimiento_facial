import cv2

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_detect = cv2.CascadeClassifier('haarcascade_eye.xml')
cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.1, 4)
    eyes = eyes_detect.detectMultiScale(gray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.putText(img, 'Cara', (x,y-20), 2, 0.5, (255,0,0), 1, cv2.LINE_AA)
        cv2.rectangle(img, (x,y), (x+w, y+w), (255, 0, 0), 5)

        for(ex, ey, ew, eh) in eyes:
            cv2.putText(img, 'ojos', (x, y + 60), 2, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + ew), (0, 255, 0), 5)



    cv2.imshow('img', img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cam.release()
