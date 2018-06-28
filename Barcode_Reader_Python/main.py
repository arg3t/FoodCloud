from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
import database_read
import datetime
import generate_moves
import serial

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)

def move(locations):
	reps = 0
	for i in range(0,len(locations),2):
		print "Sending " + locations[i]
		while(arduino.read() != "1"):
                        arduino.write(locations[i])
                        time.sleep(0.25)
		arduino.flushInput()
                arduino.flushOutput()

		print "Sending " + locations[i+1]
		while(arduino.read() != '1'):
			arduino.write(locations[i+1])
			time.sleep(0.25)
		arduino.flushInput()
                arduino.flushOutput()

        arduino.write('-')


print("[INFO] starting video stream...")

def dateStr():
    date_cur = ""
    if len(str(datetime.date.today().day)) == 1:
        date_cur = date_cur + "0" + str(datetime.date.today().day) + "."
    else:
        date_cur = date_cur + str(datetime.date.today().day) + "."
    if len(str(datetime.date.today().month)) == 1:
        date_cur = date_cur + "0" + str(datetime.date.today().month) + "."
    else:
        date_cur = date_cur + str(datetime.date.today().month) + "."
    date_cur += str(datetime.date.today().year)
    return date_cur
vs = VideoStream().start()
time.sleep(2.0)
dates = []
reps = 0
barcodes = None
prevcode = None
exp_date = []
current_date =   dateStr()

def main():
    global vs 
    global dates
    global reps
    global barcodes
    global prevcode
    global exp_date
    global current_date
    while True:

        try:
            while (barcodes == None or barcodes == []):
                frame = vs.read()
                frame = imutils.resize(frame, width=400)
                barcodes = pyzbar.decode(frame)
                cv2.imshow("Image", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                try:
                    a =  arduino.read() == "1"
                    if(a):
                        return
                except:
                    continue
            barcodes = pyzbar.decode(frame)
            # loop over the detected barcodes
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                if (barcodeData != prevcode):
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)

                    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
                    dates.append(database_read.getDate(barcodeData))
                    reps += 1
                    arduino.write("1")

                prevcode = barcodeData
                barcodes = None
                cv2.imshow("Image", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            break
main()
print("[INFO] cleaning up...")
arduino.write("1")
moves = generate_moves.generate(dates,current_date)
move(moves)
cv2.destroyAllWindows()
vs.stop()