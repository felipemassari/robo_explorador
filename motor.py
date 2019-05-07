import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Sensores ultrassonicos de distancia
TRIG_front = 17 
ECHO_front = 27

TRIG_left = 10
ECHO_left = 9

TRIG_right = 4 
ECHO_right = 22

from gpiozero import Motor

motorA = Motor(5, 6)
motorB = Motor(19, 26)

#Motor A, Left Side GPIO CONSTANTS
#RIGHT_MOTOR_FRONT = 26	# IN1 - Forward Drive
#RIGHT_MOTOR_REVERSE = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
LEFT_MOTOR_FRONT = 13	# IN1 - Forward Drive
LEFT_MOTOR_REVERSE = 6	# IN2 - Reverse Drive

# Inicializacao dos motores

#frontA1 = PWMOutputDevice(RIGHT_MOTOR_FRONT, True, 0, 1000)
#frontA2 = PWMOutputDevice(RIGHT_MOTOR_REVERSE, True, 0, 1000) 

#reverseA2 = PWMOutputDevice(RIGHT_MOTOR_REVERSE, True, 0, 1000)
#reverseA1 = PWMOutputDevice(RIGHT_MOTOR_FRONT, True, 0, 1000)
 

#forwardRight = PWMOutputDevice(LEFT_MOTOR_FRONT, True, 0, 1000)
#reverseRight = PWMOutputDevice(LEFT_MOTOR_REVERSE, True, 0, 1000)


while True:
	
	motorA.forward(0.5)
	print("frente")
	time.sleep(2)
	motorA.stop()
	print("parado")
	time.sleep(2)
	motorB.backward(0.5)
	print("reverse")
	time.sleep(3)
	
