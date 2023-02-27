import cv2
import numpy as np

img=cv2.imread('given.png')

imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_,binImage = cv2.threshold(imgGray, 110, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(binImage, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
def getContours(img,minarea,maxarea ):
    contours,_ = cv2.findContours(binImage, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area=cv2.contourArea(cnt)
        areareq=0
        if area>minarea and area<maxarea:
             #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # peri = cv2.arcLength(cnt,True)
            # approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(approx)
            # print(approx.shape)
    # cv2.drawContours(img, approx, -1, (255, 0, 0), 20)
    # x1=approx[0][0][0]
    # y1=approx[0][0][1]
    # x2=approx[1][0][0]
    # y2=approx[1][0][1]
            x,y,w,h =cv2.boundingRect(cnt)

    imgExtract=img[y:y+h,x:x+w]
    return imgExtract
    
inner=getContours(img,9000,18000)
outer=getContours(img,11000,30000)
cv2.imshow("orig",img)
cv2.imshow("outer",outer)
cv2.imshow("inner",inner)                 
cv2.waitKey(0)