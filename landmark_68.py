import cv2
import dlib

def face_landmark(video):
# cap = cv2.VideoCapture(0)
    hog_face_detector = dlib.get_frontal_face_detector()
    # hog_face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rows, cols = (68, 2)
    coor = [[]]

    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    k = True
    while True:
        _, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = hog_face_detector(gray)
        if(k==True): 
            for face in faces:
                face_landmarks = dlib_facelandmark(gray, face)    
                if(face_landmarks):       
                    for n in range(0, 68):
                        x = face_landmarks.part(n).x
                        y = face_landmarks.part(n).y
                        # cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
                        cv2.putText(frame, "{}".format(n),(x, y), cv2.FONT_HERSHEY_COMPLEX ,0.3 , (123,246,123),1)
                        print(n, x, y)
                        coor.append([x, y])
                    k = False
                    break
        
        for face in faces:
            face_landmarks = dlib_facelandmark(gray, face)
            for n in range(0, 68):
                x = face_landmarks.part(n).x
                y = face_landmarks.part(n).y
                # cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
                cv2.putText(frame, "{}".format(n),(x, y), cv2.FONT_HERSHEY_COMPLEX ,0.3 , (123,246,123),1)
                # print(n, x, y)

        cv2.imshow("Face Landmarks", frame)
        # print(coor)

        key = cv2.waitKey(1)
        if key == 27:
            break
    
    # print(coor)
    return coor
    # cap.release()
    # cv2.destroyAllWindows()