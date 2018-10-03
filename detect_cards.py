import cv2 as cv
import numpy as np 

image_file = "Data/IMG_20180930_143531.jpg"
img = cv.imread(image_file)

height, width, chans = img.shape

totArea = width*height
fracton = totArea/20000
print(fracton)

smaller = cv.resize(img, (int(width/4), int(height/4)))
gray = cv.cvtColor(smaller, cv.COLOR_BGR2GRAY)
#ret , thresh = cv.threshold(gray, 80, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

smooth = cv.GaussianBlur(gray, (5,5),0)
edges = cv.Canny(smooth, 20, 100)
im2, contours, hierarchy = cv.findContours(edges,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


result_contours = []
indices = []
idx = 0

for contour in contours:
    area = cv.contourArea(contour)
    perimeter = cv.arcLength(contour,True)
    if area > 10000:
        approx_poly = cv.approxPolyDP(contour,perimeter*0.1,True)
        result_contours.append(approx_poly)
        #print(approx_poly)
        #print(area)
        x,y,w,h = cv.boundingRect(contour)
        #cv.rectangle(smaller,(x,y),(x+w,y+h),(0,255,0),2)
        indices.append(idx)
    idx=idx+1
        
for id in indices:
    cv.drawContours(smaller, contours, id, (255,255,0), 5)

#cv.drawContours(smaller, result_contours, -1, (0,255,0), 1)
cv.imshow("Image", smaller)
cv.waitKey()
cv.destroyAllWindows()