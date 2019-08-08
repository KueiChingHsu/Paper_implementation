import os
import time

print('User Password Update Phase Startup')
os.system("python3 auth/password_update_phase_user.py")
os.system("python2 auth/send_password.py")
os.system("python2 auth/receive_file_2_1.py")
print("Password Update Phase Success !")
print('User Close')
