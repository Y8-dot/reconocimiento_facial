import cv2
import mediapipe as mp
import math
import time as tm
import serial

arduino = serial.Serial('COM7', 9600) #Declaramos el puerto y los baudios donde manipularemos al arduino

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

"""Variables para almacenarlas"""

parpadeo = False
conteo = 0
time = 0
start = 0
final = 0
conteo_sue = 0
muestra = 0

mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)

mpMallaFacial = mp.solutions.face_mesh
MallaFacial = mpMallaFacial.FaceMesh(max_num_faces=1)


while True:
    ret,frame = cap.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = MallaFacial.process(frameRGB)

    px = []
    py = []
    lista = []
    r = 3
    t = 5

    if resultados.multi_face_landmarks:
        for rostros in resultados.multi_face_landmarks:
            mpDibujo.draw_landmarks(frame, rostros, mpMallaFacial.FACEMESH_CONTOURS, ConfDibu, ConfDibu)


            for id,puntos in enumerate(rostros.landmark):
                al, an, c = frame.shape
                x, y = int(puntos.x*an), int (puntos.y*al)
                px.append(x)
                py.append(y)
                lista.append([id, x, y])
                if len(lista) == 468:

                    #para el ojo derecho
                    x1, y1 = lista[145][1:]
                    x2, y2 = lista[159][1:]
                    cx, cy = (x1 + x2)// 2, (y1 + y2) // 2
                    cv2.line(frame, (x1, y1), (x2, y2), (0,0,0), t)
                    cv2.circle(frame, (x1, y1), r, (0,0,0), cv2.FILLED)
                    cv2.circle(frame, (x2, y2), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (cx, cy), r, (0, 0, 0), cv2.FILLED)
                    longitud1 = math.hypot(x2 - x1, y2 - y1)
                    #print("Longitud 1", longitud1)

                    #para el ojo izquierdo
                    x3, y3 = lista[374][1:]
                    x4, y4 = lista[386][1:]
                    cx2, cy2 = (x3 + x4) // 2, (y3 + y4) // 2
                    longitud2 = math.hypot(x3-x4, y3-y4)
                    #print("Longitud 2", longitud2)

                    #conteo de parpadeo
                    cv2.putText(frame, f'Parpadeos:{int(conteo)}', (300, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

                    if longitud1 <= 9.2 and longitud2 <= 9.2:
                        conteo = conteo + 1
                        tm.sleep(0.5)
                        #parpadeo = True
                        if conteo >=4:
                            conteo = 0

    cv2.imshow('test_eyes', frame)
    k = cv2.waitKey(30)
    print(conteo)
    arduino.write(b'9')
    lectura = arduino.readline()
    print(lectura)
   # arduino.close()


    if k == 27:
        break
cap.release()
