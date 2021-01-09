from cv2 import cv2
from PIL import Image
import pytesseract
import codecs
import re

img_cv = cv2.imread(r'images\output\plate.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
#plt = (pytesseract.image_to_string(img_rgb, lang='eng', config='--psm 9 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPRSTUVYZ0123456789'))
plt = (pytesseract.image_to_string(img_rgb, lang='eng', config='--psm 9'))
p = re.findall('\d{2}\s?[A-Z]{1,3}\s?\d{2,4}', plt)
print (p)

