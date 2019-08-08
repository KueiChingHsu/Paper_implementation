import os
import time

start = time.time()
print('User Registration Startup')
os.system("python3 reg/use_reg_1.py")
os.system("python2 reg/send_file.py")
os.system("python2 reg/receive_file.py")
print('User Registration Success !')
print('User Close')
end = time.time()
print ("computation cost : ",end-start," seconds")