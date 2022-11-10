import sys
import socket
from datetime import datetime

print(r""" ____    ____       _____        _____    ____   ____  _____   ______    ____   ____       _____        _____   
                                        
 ## ### # # ##  #   ### ##   #  ##  ### 
#    #  ### # # #   #   # # # # # #  #  
 #   #  ### ##  #   ##  ##  # # ##   #  
  #  #  # # #   #   #   #   # # # #  #  
##  ### # # #   ### ### #    #  # #  #   
 ____    ____       _____        _____    ____   ____  _____   ______    ____   ____       _____        _____  """)

scantarget = input(str("The IP you want to scan: "))

print("Scanning target " + scantarget)
print("Scan started at " + str(datetime.now()))

try:

    for port in range(1, 65535):
        se = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = se.connect_ex((scantarget,port))
        if result == 0:
            print("[*] PORT {} is open.".format(port))
        se.close

except KeyboardInterrupt:
       print("\n Exiting.")
       sys.exit()

except socket.error:
       print("\ The HOST is not responding.")
       sys.exit()   
      
