import numpy as np
from cv2 import cv2

plate_cascade = cv2.CascadeClassifier('tr_plate_number.xml')

img = cv2.imread(r'images\input\m10.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plates = plate_cascade.detectMultiScale(gray, 1.07, 4)

for (x,y,w,h) in plates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    plate_croped = img[y:y+h, x:x+w]

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite(r'images\output\plate_detected.png',img)    
    cv2.destroyAllWindows()

cv2.imwrite(r'images\output\plate.png',plate_croped)
cv2.destroyAllWindows()
