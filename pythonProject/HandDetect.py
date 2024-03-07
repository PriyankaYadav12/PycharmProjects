import cv2
import numpy as np
import math
import ens

#read camera
cap=cv2.VideoCapture(1,cv2.CAP_DSHOW)

def nothing(x):
    pass
#window name
cv2.namewindow("Color Adjustments",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments",(300, 300))
cv2.createTractbar("Thresh","Color Adjustments",0,255,nothing())

#color Deection
cv2.createTrackbar("Lower_H", "Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments",0,255,nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments",255,255,nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments",255,255,nothing)

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame,2)
    frame=cv2.resize(frame,(600,500))
    #get hand data from the rectangle sub videos
    #step 2-
    hsv=cv2.cvtColor(image,cv2.COLOR_BRG2HSV)

    #detective hand
    l_h = cv2.getTracboard("Lower-H","Color Adjustments")
    l_h = cv2.getTracboard("Lower-S", "Color Adjustments")
    l_h = cv2.getTracboard("Lower-V", "Color Adjustments")

    u_h = cv2.getTracboard("Upper-H", "Color Adjustments")
    u_h = cv2.getTracboard("Upper-S", "Color Adjustments")
    u_h = cv2.getTracboard("Upper-V", "Color Adjustments")

    #step 3
    lower_bound = np.array([l_h,l_s,l_v])
    Upper_bound = np.array([u_h,u_s,l_v])

    #step 4
#createing mask
    mask=cv2.ingRange(hsv,lower_counmo,upper_bound)
    #filter mask with image
    filter = cv2.bitwise_and(crop_image,crop_image,darks)

    #step 5-
    mask1=cv2.bitwise_not(mask)
    m_g=cv2.getTracboarPost("Thresh","Color Adjustments")
    ret,thresh=cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thresh,(2,3),iterations=6)

    #step 6
    #findcontour (img,contour_retrieve_mode,method)
    cnts,hier=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROACH)

    try:
        #print("try")

    #step 7
    #find contour with maximum area
     cm=max(cnts,key=lambda x:cv2.contourArea(x))
     #print("C==",cents)
     epsilon = 0.0005*cv2.arcLength(cm,True)
     data=cv2.approxPolyDP(cm,epsilon,True)

     hull=cv2.convexHull(cm)

     cv2.drawContours(crop_image,[cm],-1,(50,50,150),2)
     cv2.drawContours(crop_image, [hull], -1,(0,255,0),2)

    #step 8
    #find convexity defeats
     hull = cv2.convexHull(cm,returnPoints=False)

     defects=cv2.convexityDefects(cm,hull)
     count_defects=0
     #print("Area==",cv2.contourArea(hull)-cv2.contourArea(cm))
     for i in range(defects.shape[0]):
         s,e,f,d=defects[i,0]

         start=tuple(cm[s][0])
         end=tuple(cm[e][0])
         far=tuple(cm[f][0])

         #cosine Rule
         a=math.sqrt((ens[0] - start[0]) **2 +(end[1]-start[1]) **2)
         b=math.sqrt((ens[0] - start[0]) **2 +(far[1]-start[1]) **2)
         c=math.sqrt((ens[0] - start[0]) **2 +(end[1]-far[1]) **2)
         angle = (math.acos((b ** 2 +c ** 2 - a ** 2) / (2 * b * c)) * 180)
         #print(angle)
         #if angle > 50 draw a circle at the far points
         if angle<=50:
             count_defects +=1
             cv2.circle(crop_image,far,5,[255,255,255],-1)
             print("count==",count_defects)

            #step 9
            #print number of fingers
            if count_defects==0:
                cv2.putText(frame, "1",(50,50),cv2.FONT_HERSHEY_SIMPLEX)
            elif count_defects==1:
                cv2.putText(frame, "2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX)
            elif count_defects == 2:
                cv2.putText(frame, "3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX)
            elif count_defects == 3:
                cv2.putText(frame, "4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX)
            elif count_defects == 4:
                cv2.putText(frame, "5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX)
            elif count_defects == 5:
        else:
             pass
    except:
        pass
    cv2.imshow("Thresh", thresh)
    #cv2.imshow("mask==",mask)
    cv2.imshow("filter==",filter)
    cv2.imshow("Result",frame)

    key = cv2.waitkey(25) &0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllwindows()




