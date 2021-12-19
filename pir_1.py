import RPi.GPIO as GPIO
#import time
from pygame import mixer
from pygame import time

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO_PIR = 4

print ("PIR Module Test (CTRL-C to exit)")

GPIO.setup(GPIO_PIR,GPIO.IN)

Current_State  = 0
Previous_State = 0
mixer.init()
mixer.music.load("three.wav")
mixer.music.set_volume(1.0)

try:

  print ("Waiting for PIR to settle ...")

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    

  print ("Ready")     
    
  # Loop until users quits with CTRL-C
  while True :
   
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==1 and Previous_State==0:
      print ("Motion detected")
      mixer.music.play(loops=1)
      time.wait(29000)
      print ("29 sec timer ended. Stopping music")
      Previous_State=1
      # Record previous state
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print ("Ready")
      Previous_State=0
      
    time.wait(1)      
      
except KeyboardInterrupt:
  print ("Quit")
  # Reset GPIO settings
  GPIO.cleanup()

