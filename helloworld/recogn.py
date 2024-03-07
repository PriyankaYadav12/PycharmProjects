import cv2
import numpy as np

imgratan = face_recognition.load_image_file('/content/photo/img2.jpg')
imgratan = cv2.cvtColor(imgearatn,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('')
imgtest = cv2.cvtColor(imgearatn,cv2.COLOR_BGR2RGB)

cv2.show('ratan tata',imgratan)
cv2.show('ratan Test',imgtest)
cv2.waitkey(0)

# import cv2
# img= cv2.imread("img7.jpg",1)
# cv2.imshow(img)
# cv2.distroyallwindows(0)
# cv2.waitkey(0)