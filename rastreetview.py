import bluetooth
import RPi.GPIO as GPIO
import time                  #calling for header file which helps in using GPIOs of PI
btn_pressed = False
 
GPIO.setmode(GPIO.BOARD)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)

GPIO.setup(40, GPIO.OUT)

servoPWM = GPIO.PWM(40, 50)
servoPWM.start(5)

dcServo = 5
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print("Accepted connection from ",address)
while 1:
 
 data = client_socket.recv(1024)
 print ("Received: %s" % data)
 if (btn_pressed == False):
     if (data == "lw"):
      dcServo = dcServo + 0.1
      servoPWM.ChangeDutyCycle(dcServo)
      if dcServo >= 10:
          dcServo = 10
      print ("Esquerda webcam")
      btn_pressed = True
     if (data == "rw"):
      servoPWM.ChangeDutyCycle(dcServo)
      dcServo = dcServo - 0.1
      if dcServo <= 5:
          dcServo = 5
      print ("Direita webcam")
      btn_pressed = True
     if (data == "dw"):
      print ("Baixo webcam")
      btn_pressed = True
     if (data == "uw"):
      print ("Cima webcam")
      btn_pressed = True
     if (data == "lc"):
      print ("Esquerda car")
      btn_pressed = True
     if (data == "rc"):
      print ("Direita car")
      btn_pressed = True
     if (data == "dc"):
      print ("Baixo car")
      btn_pressed = True
     if (data == "uc"):
      print ("Cima car")
      btn_pressed = True
 else:
     if (data == "lw"):
      print ("Webcam parou")
      btn_pressed = False
     if (data == "rw"):
      print ("Webcam parou")
      btn_pressed = False
     if (data == "dw"):
      print ("Webcam parou")
      btn_pressed = False
     if (data == "uw"):
      print ("Webcam parou")
      btn_pressed = False
     if (data == "lc"):
      print ("Car parou")
      btn_pressed = False
     if (data == "rc"):
      print ("Car parou")
      btn_pressed = False
     if (data == "dc"):
      print ("Car parou")
      btn_pressed = False
     if (data == "uc"):
      print ("Car parou")
      btn_pressed = False
     
 
client_socket.close()
server_socket.close()
