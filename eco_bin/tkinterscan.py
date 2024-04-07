import cv2
from pyzbar.pyzbar import decode
import time
import random
from tkinter import *

wn = Tk()
wn.title('Scaner')
wn.geometry('500x500')

code = ["1234", '1111', '5555']
cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
txt = label(wn, width=100, height=70, text='')
txt.grid(row=0, column=0)
while camera == True:
	sucess, frame = cam.read()
 
	for i in decode(frame):
		
		qr = i.data.decode('utf-8')
		if qr in code and i.type == 'QRCODE':
			# print(promo[qr])
            txt.config(text=promo[qr])
		else:
			txt.config(text='-')

		time.sleep(6)

		cv2.imshow("OurQr_Code_Scanner", frame)
		cv2.waitKey(3)




wn.mainloop()