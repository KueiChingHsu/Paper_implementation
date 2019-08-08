import os
import time

start = time.time()
print('User Authentication Startup')
os.system("python3 auth/user1.py")
os.system("python2 auth/send_file_1.py")
os.system("python2 auth/receive_file_2_1.py")
os.system("python3 auth/user2.py")
os.system("python2 auth/send_file_3_1.py")
os.system("python2 auth/receive_file_6.py")
os.system("python3 auth/user3.py")
print('User Close')
end = time.time()
print ("computation cost : ",end-start," seconds")