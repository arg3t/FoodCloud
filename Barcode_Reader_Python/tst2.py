import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)

def move(locations):
	reps = 0
	for i in range(0,len(locations),2):
		
		while(arduino.read() != "1"):
                        arduino.write(locations[i])
                        time.sleep(0.25)
		arduino.flushInput()
                arduino.flushOutput()

		
		while(arduino.read() != '1'):
			arduino.write(locations[i+1])
			time.sleep(0.25)
		arduino.flushInput()
                arduino.flushOutput()

        arduino.write('-')
        
move(['1','3','2','1','3','2'])