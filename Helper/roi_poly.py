"""# importing cv2
import cv2
import numpy as np
# path
path = "Helper/frame0.jpg"
# Reading an image in default mode
image = cv2.imread(path)
# Window name in which image is displayed
# Center coordinates
#center_coordinates = (120, 50)
pts=np.array([[3726,1071],[3740,2033],[2262,2082],[2303,1046]],np.int32)
pts1=(3726,1071)
pts2=(3740,2033)
pts3=(2262,2082)
pts4=(2303,1046)

# Radius of circle
radius = 20

# Blue color in BGR
color1 = (0, 0, 0)
color2 = (0, 0, 255)
color3 = (0, 255, 0)
color4 = (255, 255, 255)

# Line thickness of 2 px
thickness = 20

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, pts1, radius, color1, thickness)
image = cv2.circle(image, pts2, radius, color2, thickness)
image = cv2.circle(image, pts3, radius, color3, thickness)
image = cv2.circle(image, pts4, radius, color4, thickness)
image=cv2.polylines(image,[pts],True,(0,255,0),2)
# Displaying the image
cv2.imshow("window_name", image)
cv2.waitKey(0)
cv2.destroyAllWindow()"""
# importing cv2
import cv2
import numpy as np
# path
path = "Helper/frame0.jpg"
# Reading an image in default mode
image = cv2.imread(path)
# Window name in which image is displayed
# Center coordinates
#center_coordinates = (120, 50)
pts=np.array([[3726,1071],[3740,2033],[2262,2082],[2303,1046]],np.int32)
pts1  = np.array([2303,1046])
pts2  = np.array([3726,1071])
pts3 = np.array([3740,2033])
pts4  = np.array([2262,2082])

# pts1   = np.array([400, 200])
# pts2  = np.array([800, 100])
# pts3 = np.array([1000, 450])
# pts4  = np.array([300, 600])


# Radius of circle
radius = 20

# Blue color in BGR
color1 = (0, 0, 0)
color2 = (0, 0, 255)
color3 = (0, 255, 0)
color4 = (255, 255, 255)

# Line thickness of 2 px
thickness = 20

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, pts1, radius, color1, thickness)
image = cv2.circle(image, pts2, radius, color2, thickness)
image = cv2.circle(image, pts3, radius, color3, thickness)
image = cv2.circle(image, pts4, radius, color4, thickness)
image=cv2.polylines(image,[pts],True,(0,255,0),2)
# Displaying the image
cv2.imshow("window_name", image)
cv2.waitKey(0)
cv2.destroyAllWindow()