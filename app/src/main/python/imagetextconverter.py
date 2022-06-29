import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image
import base64
import io
def main_image(img):
    decoded_data = base64.b64decode(img)
    np_data = np.frombuffer(decoded_data, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

    pytesseract.pytesseract.tesseract_cmd ="E:\\download\\Tesseract-OCR\\tesseract.exe"
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    boxes =pytesseract.image_to_data(img)
    himg,wimg,_=img.shape
    for x,i in enumerate (boxes.splitlines()):
        if x!=0:
            i = i.split()
            if len(i) ==12:
                (x, y, w, h) = (int(i[6]), int(i[7]), int(i[8]), int(i[9]))
                img = cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 2)
                cv2.putText(img,i[11],(x, y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


    #cv2.imshow('img', img)
    #cv2.waitKey(0)
    pil_im = Image.fromarray(img)
    buff = io.BytesIO()
    pil_im.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    return "" + str(img_str, 'utf-8')


def main_text(img):
    decoded_data = base64.b64decode(img)
    np_data = np.frombuffer(decoded_data, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)

    pytesseract.pytesseract.tesseract_cmd ="E:\\download\\Tesseract-OCR\\tesseract.exe"
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    boxes =pytesseract.image_to_data(img)
    himg,wimg,_=img.shape
    text = ""
    for x,i in enumerate (boxes.splitlines()):
        if x!=0:
            i = i.split()
            if len(i) ==12:
                text =text+i[11]+' '
    return text



"""
img = cv2.imread('mnJH2O8SgSLbzkGQOmWI_9_Text_messages_to_convert_more_real_estate_leads.jpg')
pil_im=Image.fromarray(img)
buff = io.BytesIO()
pil_im.save(buff,format="PNG")
img_str = base64.b64encode(buff.getvalue())
data =main_image(img_str)
decoded_data =base64.b64decode(data)
np_data = np.frombuffer(decoded_data,np.uint8)
img =cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)
cv2.waitKey(0)"""

"""
img = cv2.imread('mnJH2O8SgSLbzkGQOmWI_9_Text_messages_to_convert_more_real_estate_leads.jpg')
pil_im=Image.fromarray(img)
buff = io.BytesIO()
pil_im.save(buff,format="PNG")
img_str = base64.b64encode(buff.getvalue())
print(main_text(img_str))"""
