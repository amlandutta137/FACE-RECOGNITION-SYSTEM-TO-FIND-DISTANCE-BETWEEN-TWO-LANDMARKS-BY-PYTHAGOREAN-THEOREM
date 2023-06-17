import cv2
import dlib

# from function import face_data
# from function import Distance_finder
# from function import FocalLength
from function import displaying_distance
from new_468 import face_landmarks_468
from landmark_distance import distance_between_landmarks



video = cv2.VideoCapture(0)
coordinate = face_landmarks_468(video)
# print(coordinate)
landmark_1 = int(input("Enter the 1st landmark (between 1 to 468) : "))
landmark_2 = int(input("Enter the 2nd landmark (between 0 to 467 except the 1st landmark) : "))
distance_bt_landmark = distance_between_landmarks(coordinate, landmark_1, landmark_2)
print("The distance between ", landmark_1, " and ", landmark_2, " : ", distance_bt_landmark)




def original_landmark_distance(distance_from_camera):
    focal_length = 350.34965034965035
    landmark_distance_in_frame = distance_bt_landmark
    original_land_dist = (landmark_distance_in_frame * distance_from_camera) / focal_length
    
    return original_land_dist


print("The actual distance between the landmarks : ", original_landmark_distance(coordinate[469][0]))