import cv2 as cv
import numpy as np
shapes = {}
colors = [["red",255,0,0],["green",0,255,0],["blue",0,0,255]]
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(colors)):
        d = abs(R- int(colors[i][1])) + abs(G-int(colors[i][2]))+ abs(B- int(colors[i][3]))
        if(d<=minimum):
            minimum = d
            cname = colors[i][0]
    return cname

def side(n):
    pair = {0:1,1:2,2:3,3:0}
    length = int(((approx[n][0][0]-approx[pair[n]][0][0])**2 + (approx[n][0][1]-approx[pair[n]][0][1])**2)**(1/2))
    return length
def diag(n):
    pair = {0:2,1:3}
    length = int(((approx[n][0][0]-approx[pair[n]][0][0])**2 + (approx[n][0][1]-approx[pair[n]][0][1])**2)**(1/2))
    return length
def slope(n):
    pair = {0:1,1:2,2:3,3:0}
    try:
        slope = ((approx[n][0][1]-approx[pair[n]][0][1])/(approx[n][0][0]-approx[pair[n]][0][0]))
    except:
        slope = 0
    return slope
def mid(n):
    pair = {0:2,1:3}
    mid = approx[n][0][0]+approx[pair[n]][0][0]
    return mid

img= cv.imread('sample.png')
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imggray, 245, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
del contours[0]

for cnt in contours:
    approx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv.putText(img,"Triangle",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
        shape = "Triangle"
    elif len(approx) == 4:
        x,y,w,h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >=0.95 and aspectRatio <= 1.05 :
            cv.putText(img,"Square",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
            shape = "Square"
        else :
            s1 = side(0)
            s2 = side(1)
            s3 = side(2)
            s4 = side(3)
            d1 = diag(0)
            d2 = diag(1)
            sl1 = slope(0)
            sl2 = slope(1)
            sl3 = slope(2)
            sl4 = slope(3)
            mid1 = mid(0)
            mid2 = mid(1)
            if np.isclose(mid1,mid2,0,2) :
                if np.isclose([s1,s2,s3,s4],s1,0,2).all() :
                    cv.putText(img,"Rhombus",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
                    shape = "Rhombus"
                elif np.isclose(s1,s3,0,2) and np.isclose(s2,s4,0,2) and np.isclose(d1,d2,0,2) :
                    cv.putText(img,"Rectangle",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
                    shape = "Rectangle"
                else :
                    cv.putText(img,"Parallelogram",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
                    shape = "Parallelogram"
            elif np.isclose(sl1,sl3,0,0.1) or np.isclose(sl2,sl4,0,0.1) :
                cv.putText(img,"Trapezium",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
                shape = "Trapezium"
            else :
                cv.putText(img,"Quadrilateral",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
                shape = "Quadrilateral"
    elif len(approx) == 5:
        cv.putText(img,"Pentagon",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
        shape = "Pentagon"
    elif len(approx) == 6:
        cv.putText(img,"Hexagon",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
        shape = "Hexagon"
    elif len(approx) >10 :
        cv.putText(img,"Circle",(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0))
        shape = "Circle"
    M = cv.moments(cnt)
    cx = int(round(M["m10"]/M["m00"],2))
    cy = int(round(M["m01"]/M["m00"],2))
    b,g,r = img[int(cy),int(cx)]
    area = round(M["m00"],1)
    cname = getColorName(r,g,b)
    shapes[shape] = [cname,area,cx,cy]

l = list(shapes.items())
for i in range(len(l)-1):
    if l[i+1][1][1]<l[i][1][1]:
        m = l[i+1]
        l[i+1] = l[i]
        l[i] = m
shapes = dict(l)
print(shapes)
cv.imshow("sample",img)
cv.waitKey(0)
cv.destroyAllWindows()

