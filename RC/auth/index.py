import os
import time

start = time.time()
print('RC Authentication Startup')
os.system("python2 auth/receive_file_2_2.py")
os.system("python3 auth/RC_auth1.py")
os.system("python2 auth/send_file_3_2.py")
os.system("python2 auth/receive_file_4.py")
os.system("python3 auth/RC_auth2.py")
os.system("python2 auth/send_file_5.py")
print('RC Close')
