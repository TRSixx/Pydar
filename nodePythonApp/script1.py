import time 
import sys
print('Hello from python')

i=0
while True:
	print('Hello from '+str(i))
	i+=1
	sys.stdout.flush()
	time.sleep(1)