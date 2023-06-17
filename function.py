import cv2
import dlib


# Function to calculate the focal length of the camera
def FocalLength(measured_distance, real_width, width_in_ref_image):
    focal_length = (width_in_ref_image * measured_distance)/ real_width
    return focal_length


# Distance estimation function
def Distance_finder (Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance


# Face Detection by Haar-Cascade
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# For width of the face in frame
def face_data(image):
    face_width = 0 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (222,141,123), 1)
        face_width = w
    return face_width


# For capturing distance from camera
def displaying_distance(cap):
    # video = cv2.VideoCapture(0)
    previous_distance = 30 
    width = 14.3

    # To compare the distance we need another image 
    img = cv2.imread("pic.jpg")
    face_width = face_data(img)
    Focal_length = FocalLength(previous_distance, width,face_width)
    print("Focal length : ", Focal_length)


    # k = True
    while True:
        ret, frame = cap.read()

        # while (k==True):
           
        #     k=False
        #     break

        if ret==True:
            face_width_in_frame = face_data(frame)
            if face_width_in_frame !=0:
                Distance = round(Distance_finder(Focal_length, width,face_width_in_frame),2)
                cv2.putText(frame, "Distance from Camera "+"{}".format(Distance)+"CM", (50,50), cv2.FONT_HERSHEY_COMPLEX,1, (123,246,123),3)
        

        cv2.imshow("frame", frame )
        if cv2.waitKey(1)==27:
            break 

    cap.release()
    cv2.destroyAllWindows()
    # print("Distance captured : ", Distance)
    # return Distance