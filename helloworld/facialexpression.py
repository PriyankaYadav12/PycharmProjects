import cv2
import imaplib
face_cascade = cv2.CascadeClassifier('haarascade_frontalface_default.xml')
# read the input image
img = cv2.imread('Snapchat-131452324.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x+y), (x+w, y+h), (255, 0, 0), 3)

# Display the output
cv2.imshow('img', img)
cv2.waitkey()
