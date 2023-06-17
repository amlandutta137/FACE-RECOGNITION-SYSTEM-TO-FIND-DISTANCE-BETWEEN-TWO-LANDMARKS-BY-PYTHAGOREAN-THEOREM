import cv2
import mediapipe as mp

from function import face_data
from function import Distance_finder
from function import FocalLength


def face_landmarks_468(cap):
    mp_face_mesh = mp.solutions.face_mesh
    faceMesh = mp_face_mesh.FaceMesh()
    mp_draw = mp.solutions.drawing_utils
    draw_spec = mp_draw.DrawingSpec(thickness =1, circle_radius = 1)


    previous_distance = 30 
    width = 14.3
    img = cv2.imread("pic.jpg")
    face_width = face_data(img)
    Focal_length = FocalLength(previous_distance, width,face_width)
    # cap = cv2.VideoCapture(0)

    # rows, cols = (468, 2)
    coor = [[]]

    k, l = True, True
    while True:
        _, img = cap.read()

        results = faceMesh.process(img)

        while(k == True):
            if (results.multi_face_landmarks):
                for face_landmarks in results.multi_face_landmarks:
                    mp_draw.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS, draw_spec, draw_spec)
                    for id, lm in enumerate(face_landmarks.landmark):
                        # print(lm)
                        ih, iw, ic = img.shape
                        x, y, z = int(lm.x*iw), int(lm.y*ih), int(lm.z*ic)
                        coor.append([x, y])
                        # print("id=", id, " x=", x, " y=", y, " z=", z)
            k = False
            break
        
        # while(l == True):
        Distance = 0.0
        if (_==True):
            face_width_in_frame = face_data(img)
            if face_width_in_frame !=0:
                Distance = round(Distance_finder(Focal_length, width,face_width_in_frame),2)
                coor.append([Distance, 0])
            # l = False
            # break
        # print(coor)
        # i = 0
        if (results.multi_face_landmarks):
            for face_landmarks in results.multi_face_landmarks:
                
                # mp_draw.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS, cv2.putText(cap, "{}".format(i),(x, y), cv2.FONT_HERSHEY_COMPLEX ,0.3 , (123,246,123),1))
                mp_draw.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS, draw_spec, draw_spec)
            

        # print(results.multi_face_landmarks)
        cv2.imshow("Face Mesh", img)

        key = cv2.waitKey(1)
        if key == 27:
            break

    
    print(coor)
    print("Length of list : ",len(coor))
    print("Distance from cam : ", Distance)


    return coor