import os
import time

print('RC Startup')
os.system("python2 reg/user/receive_file.py")
os.system("python3 reg/user/reg_user_rc.py")
os.system("python2 reg/user/send_file.py")


print('RC Close')

