import cv2
from pyzbar.pyzbar import decode
import time
from data import promo
from data import codes
import pyfirmata

comport = 'COM1'
board = pyfirmata.Arduino(comport)
bz = board.get_pin('d:2:o')

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
att = 1
while camera == True:
	sucess, frame = cam.read()
	for i in decode(frame):          
		if i.type == 'QRCODE':
            att = att  + 1
            print(i.data.decode('utf-8'), 'keldi')

			bz.write(1)                #voice section
			time.sleep(0.5)
		else:
			print("-")

		time.sleep(1)

		cv2.imshow("OurQr_Code_Scanner", frame)
		cv2.waitKey(3)
