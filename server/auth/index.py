import os
import time


print('Server Authentication Startup')
os.system("python2 auth/receive_file_1.py")
os.system("python3 auth/server1.py")
os.system("python2 auth/send_file_2_1.py")
os.system("python2 auth/receive_file_3_1.py")
os.system("python2 auth/send_file_2_2.py")
os.system("python2 auth/receive_file_3_2.py")
os.system("python3 auth/server2.py")
os.system("python2 auth/send_file_4.py")
os.system("python2 auth/receive_file_5.py")
os.system("python3 auth/server3.py")
os.system("python2 auth/send_file_6.py")
print('Server Close')
