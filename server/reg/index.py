import os
import time
start = time.time()
print('Server Registration Startup')

os.system("python3 reg/reg_server.py")
os.system("python2 reg/send_file.py")
os.system("python2 reg/receive_file.py")
print('Server Registration Success !')

print('Server Close')
end = time.time()
print ("computation cost : ",end-start," seconds")
