import RPi.GPIO as GPIO
import time
#import camera_control
GPIO.setmode(GPIO.BCM)
from gpiozero import Motor

#Sensores ultrassonicos de distancia
TRIG_front = 17 
ECHO_front = 27

TRIG_left = 10
ECHO_left = 9

TRIG_right = 4 
ECHO_right = 18

#Motor A, Left Side GPIO CONSTANTS
motorR = Motor(19, 26)
# Motor B, Right Side GPIO CONSTANTS
motorL = Motor(5, 6)


print " SETUP "

GPIO.setup(TRIG_front, GPIO.OUT)
GPIO.setup(ECHO_front, GPIO.IN)

GPIO.setup(TRIG_left, GPIO.OUT)
GPIO.setup(ECHO_left, GPIO.IN)

GPIO.setup(TRIG_right, GPIO.OUT)
GPIO.setup(ECHO_right, GPIO.IN)

print " SETUP OK "
setup = False

#ler bluetooth autonomous ou remote
autonomous = True

#Funcoes de leitura de distancia

#ler distancia a frente
def front():
	GPIO.output(TRIG_front, False)
	time.sleep(0.5)

	GPIO.output(TRIG_front, True)
	time.sleep(0.00001)
	GPIO.output(TRIG_front, False)

	while GPIO.input(ECHO_front) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO_front) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance_front = pulse_duration * 17150
	distance_front = round(distance_front,2)
	
	if setup == False:
		print("Sensor front, OK")
	return(distance_front)

#ler distancia da direita
def avoid_left():
	GPIO.output(TRIG_left, False)
	time.sleep(0.5)
    
	GPIO.output(TRIG_left, True)
	time.sleep(0.00001)
	GPIO.output(TRIG_left, False)


	while GPIO.input(ECHO_left) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO_left) == 1:
		pulse_end = time.time()

	pulse_duration_left = pulse_end - pulse_start

	distance_left = pulse_duration_left * 17150
	distance_left = round(distance_left,2)
		
	if setup == False:
		print("Sensor left, OK")
	return(distance_left)

#ler distancia da esquerda
def avoid_right():  
	GPIO.output(TRIG_right, False)
	time.sleep(0.5)
    
	GPIO.output(TRIG_right, True)
	time.sleep(0.00001)
	GPIO.output(TRIG_right, False)


	while GPIO.input(ECHO_right) == 0:
		pulse_start = time.time()
		
	while GPIO.input(ECHO_right) == 1:
		pulse_end = time.time()

	pulse_duration_right = pulse_end - pulse_start
	
	distance_right = pulse_duration_right * 17150
	distance_right = round(distance_right,2)
	
	if setup == False:
		print("Sensor right, OK")
	
	return(distance_right)

#teste de sensores
print("Testando sensores")
front()
avoid_left()
avoid_right()
print("Sensores OK")

#Mainprogram
while autonomous:
	
	setup = True
	
	#Modo de operacao - Autonomo ou Manual
	modo = True #camera_control.modo()
	
	if modo == "manual":
		autonomous = False
		
	
	distancia = front()
	
	print " Distance: ", distancia, " cm"
	motorR.forward(0.6)
	motorL.forward(0.6)
		
	if distancia < 12:
		
		motorR.stop()
		motorL.stop()
		time.sleep(1)
		
        #mede distancias laterias
		distance_left = avoid_left()
		distance_right = avoid_right()
		
		print " Distance Front: ", distancia, " cm"
		print " Distance Left: ", distance_left, " cm"
		print " Distance Right: ", distance_right, " cm"
		
		if distance_left < distance_right:
            #vire para a direita
			print" turning right"
			motorR.forward(0.6)
			motorL.backward(0.6)
			time.sleep(0.5)
			
			motorR.stop()
			motorL.stop()


		else:
            #vire para a direita
			print "turning left"
			motorR.backward(0.6)
			motorL.forward(0.6)
			time.sleep(0.5)
			
			motorR.stop()
			motorL.stop()



	


    
