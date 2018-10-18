import cv2 as cv
import numpy as np 
import math


def remove_double_contours(contour_list):
    results = [contour_list[0]]    
    for ctr in contour_list:
        has_match = has_match_with_list(ctr, results)
        if not has_match:
            results.append(ctr)
    return results

def has_match_with_list(target_contour,contour_list):
    has_match = False
    for ctr in contour_list:
        d = get_contour_distance(target_contour, ctr)
        if d[0]<d[1]/3:
            has_match = True
            break
    return has_match


def get_contour_center(contour):
    x,y,w,h = cv.boundingRect(contour)
    diag = math.sqrt(w*w + h*h)
    return [x + w/2, y + h/2, diag]

def get_contour_distance(contour1, contour2):
    c1 = get_contour_center(contour1)
    c2 = get_contour_center(contour2)
    dx = c1[0]-c2[0]
    dy = c1[1]-c2[1]
    return [math.sqrt(dx*dx + dy*dy), min(c1[2], c2[2])]

    
def get_card_contours(gray_image):
    smoothed_image = cv.GaussianBlur(gray_image, (5,5),0)
    edge_image = cv.Canny(smoothed_image, 20, 100)
    im2, contours, hierarchy = cv.findContours(edge_image,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    result_contours = []
    indices = []
    idx = 0

    for contour in contours:
        area = cv.contourArea(contour)
        perimeter = cv.arcLength(contour,True)
        if area > 10000:
            approx_poly = cv.approxPolyDP(contour,perimeter*0.1,True)
            result_contours.append(approx_poly)       
            x,y,w,h = cv.boundingRect(contour)
            #cv.rectangle(smaller,(x,y),(x+w,y+h),(0,255,0),2)
            indices.append(idx)
        idx=idx+1
        
    single_contours = remove_double_contours(result_contours)
    return single_contours

def analyze_card(gray_image, contour):
    x,y,w,h = cv.boundingRect(contour)
    cropped_image = gray_image[y:y+h , x:x+w]
    cv.imshow("crop", cropped_image)

image_file = "Data/IMG_20180930_143531.jpg"
img = cv.imread(image_file)

height, width, chans = img.shape

totArea = width*height
fracton = totArea/20000
print(fracton)

smaller_image = cv.resize(img, (int(width/4), int(height/4)))
gray_image = cv.cvtColor(smaller_image, cv.COLOR_BGR2GRAY)
#ret , thresh = cv.threshold(gray, 80, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

contours = get_card_contours(gray_image)


for id in range(len(contours)):
    analyze_card(gray_image, contours[id])
    cv.drawContours(smaller_image, contours, id, (255,255,0), 5)
    break

#cv.drawContours(smaller, result_contours, -1, (0,255,0), 1)
cv.imshow("Image", smaller_image)
cv.waitKey()
cv.destroyAllWindows()