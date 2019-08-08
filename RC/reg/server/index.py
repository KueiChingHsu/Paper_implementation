import os
import time

print('RC Startup')

os.system("python2 reg/server/receive_file.py")
os.system("python3 reg/server/reg_server_rc.py")
os.system("python2 reg/server/send_file.py")


print('RC Close')

