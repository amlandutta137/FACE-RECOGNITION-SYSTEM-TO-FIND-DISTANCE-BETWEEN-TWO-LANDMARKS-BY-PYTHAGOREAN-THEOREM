# # program to capture single image from webcam in python

# # importing OpenCV library
# import cv2

# # initialize the camera
# # If you have multiple camera connected with
# # current device, assign a value in cam_port
# # variable according to that
# cam_port = 0
# cam = cv2.VideoCapture(cam_port)

# # reading the input using the camera
# result, image = cam.read()

# # If image will detected without any error,
# # show result
# if result:

# 	# showing result, it take frame name and image
# 	# output
# 	cv2.imshow("GeeksForGeeks", image)

# 	# saving image in local storage
# 	cv2.imwrite("GeeksForGeeks.png", image)

# 	# If keyboard interrupt occurs, destroy image
# 	# window
# 	cv2.waitKey(0)
# 	cv2.destroyWindow("GeeksForGeeks")

# # If captured image is corrupted, moving to else part
# else:
# 	print("No image detected. Please! try again")




import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()