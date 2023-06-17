import math
from function import displaying_distance

def distance_between_landmarks(coordinate, land_1, land_2):
    print("landIndex", land_1, land_2)
    print(coordinate[land_2][0], coordinate[land_1][0], coordinate[land_2][1],coordinate[land_1][1])
    print(coordinate[land_2][0]-coordinate[land_1][0], coordinate[land_2][1]-coordinate[land_1][1])
    print((coordinate[land_2][0]-coordinate[land_1][0])**2, (coordinate[land_2][1]-coordinate[land_1][1])**2)
    distance = math.sqrt(((coordinate[land_2][0]-coordinate[land_1][0])**2) + ((coordinate[land_2][1]-coordinate[land_1][1])**2))
    return distance


