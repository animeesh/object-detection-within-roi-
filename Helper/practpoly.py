import numpy as np
import cv2

img = cv2.imread("Helper/frame0.jpg")
pts=np.array([[3726,1071],[3740,2033],[2262,2082],[2303,1046]])
#pts=np.array([[3726,1071],[3740,2033],[2262,2082],[2303,1046]],np.int32)
#pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])

## (1) Crop the bounding rect
rect = cv2.boundingRect(pts)
x,y,w,h = rect
croped = img[y:y+h, x:x+w].copy()

## (2) make mask
# pts = pts - pts.min(axis=0)
#
mask = np.zeros(croped.shape[:2], np.uint8)
# cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

## (3) do bit-op
dst = cv2.bitwise_and(croped, croped, mask=mask)

## (4) add the white background
# bg = np.ones_like(croped, np.uint8)*255
# cv2.bitwise_not(bg,bg, mask=mask)
# dst2 = bg+ dst

cv2.imshow("image",dst)
cv2.waitKey(0)
cv2.destroyAllWindow()