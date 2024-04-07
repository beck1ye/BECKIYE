from pyzbar.pyzbar import decode
import time
from data import promo
from data import codes
import pyfirmata
import cv2

comport = 'COM25'
board = pyfirmata.Arduino(comport)
bz = board.get_pin('d:2:o')

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True

while camera == True:       
	sucess, frame = cam.read()
	for i in decode(frame):          
		
		qr = i.data.decode('utf-8')
		if qr in codes and i.type == 'QRCODE':
			print(promo[qr])
			bz.write(1)                #voice section
			time.sleep(0.2)
			bz.write(0)
		else:
			print("-")

		time.sleep(1)

		cv2.imshow("OurQr_Code_Scanner", frame)
		cv2.waitKey(3)
