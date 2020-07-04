#WORKING SERVO SCRIPT
# You need to provide 5V of power if using the red servo!

import time
import wiringpi
import sys
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
# This is what sets the pwm frequency, 50 Hz (typical servo) which is determined via pwmSetRange/pwmSetClock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

'''
The longer the delay period, the more reliable the overall duty cycle of the servo seems to be. This is a slower option but a delay peroid of about 0.05 always produces consistent results
'''
#file=open("stateful","r+")
delay_period = 0.04
#counter = int(file.read().strip())
for pulse in range(50, 249, 1):
    print('sending pulse')
    wiringpi.pwmWrite(18, pulse)
    #counter+=1
    time.sleep(delay_period)
#file.write(str(counter))
#file.close()
