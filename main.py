import cv2 as cv
import sys


img = cv.imread("./images/ledBoard.jpg")
resize_img = cv.resize(img,(0, 0),fx=0.25, fy=0.2, interpolation = cv.INTER_AREA)
resize_img = cv.blur(resize_img, (2, 2))
bgr = cv.cvtColor(resize_img, cv.COLOR_RGB2BGR)
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
thresh = cv.inRange(hsv, (0,0,255), (0,0,255))
edges = cv.Canny(thresh,5,5)
contours, hierarchy= cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
number_of_objects_in_image= len(contours)

print ("The number of objects in this image: ", str(number_of_objects_in_image))

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", thresh)
cv.imshow("hsv", hsv)
cv.imshow("edges", edges)


k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_nissht.png", img)