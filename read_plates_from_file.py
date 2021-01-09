import numpy as np
import time
import pytesseract
import codecs
import re
import os
from cv2 import cv2
from PIL import Image

plate_cascade = cv2.CascadeClassifier('tr_plate_number.xml')
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
plates_lst = []
plate_croped = ''
p = []
opt_try = 1
opt_lst = [1.12,1.07]
opt_used = []
def option_1(opt_1):
    global p
    plates = plate_cascade.detectMultiScale(src, opt_1, 4)
    for (x,y,w,h) in plates:
        global plate_croped
        cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,0),0)
        plate_croped = src[y:y+h, x:x+w]
    cv2.imwrite('images\output\plate.png',plate_croped) 
    img_cv = cv2.imread('images\output\plate.png')
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    plt = (pytesseract.image_to_string(img_rgb, lang='eng', config='--psm 9'))
#   plt = (pytesseract.image_to_string(img_rgb, lang='eng', config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPRSTUVYZ0123456789'))
    p = re.findall('\d{2}\s?[A-Z]{1,3}\s?\d{2,4}', plt) 
    cv2.destroyAllWindows()
img_cnt =len(os.listdir('images\input'))  
print (img_cnt)

for i in range(img_cnt):     
    im_name = 'images\input\m'+str(i)+'.jpg'
    src = cv2.imread(im_name)
    print (im_name)
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    for j in range(len(opt_lst)):
        p = []
        k = opt_lst[j]
        option_1(k)
        if p:
            len_p = len(p[0])
            if len_p >= 7:
                plates_lst.append(p)
                opt_used.append(k)
                break

print (plates_lst)   
print (len(plates_lst))
print (opt_used)
