import os
import time
import datetime

ts=time.time()
dt=datetime.datetime.now()

file = open("ip.txt","r+")

with open("ip.txt","r") as file:

  for line in file:
     response =  os.system("ping  -c 1 -W 1 " + line)

     if response == 0:
        with open("IPsCheck.txt","w") as file:
            #print(line + ' pinged successfully')
            print(f'{ts}{dt} Successfully pinged {line}')
	    #file.write(line)
     else:
        print(f"{ts} {dt} server not available {line}")
