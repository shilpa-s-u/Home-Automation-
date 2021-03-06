import RPi.GPIO as GPIO
import time


while True:
 try:
      GPIO.setmode(GPIO.BOARD)
      GPIO.setwarnings(False)
     
      
      GPIO.setup(40,GPIO.OUT)
      

      PIN_TRIGGER = 16
      PIN_ECHO = 18

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print ("Waiting for sensor to settle")

      time.sleep(1)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()
            

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      
      if distance>70:
       print("watertank is full")
       GPIO.output(40,0)
      elif distance<20:
       print("watertank is intermediate")
       s=input("Do you want switch on motor if yes press y or n")
       if s == "y":
          GPIO.output(40,1)
          print("motor on")
       else :
           print("invalid option")
      else :
        print("water is low")
        print("motor on")
        GPIO.output(40,1)
 finally:
      GPIO.cleanup()

