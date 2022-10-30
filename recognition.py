import numpy as np
import cv2
car_cascade = cv2.CascadeClassifier("training/cascade.xml")

img = cv2.imread("positives/withmask_1.jpg")
height, width, c = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
objetos = car_cascade.detectMultiScale(gray, 1.01, 5)

print(objetos)

n = 1
for (x,y,w,h) in objetos:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(img, str(f"Mask #{n}"), (x, y-5), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 255), 1)
    n += 1

cv2.imshow('Mask Recognition', img)
cv2.waitKey(0)
cv2.destroyAllWindows()