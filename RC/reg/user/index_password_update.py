import os
import time

print('RC User Password Update Phase Startup')
os.system("python2 reg/user/receive_file.py")
os.system("python3 reg/user/password_update_phase_RC.py")
os.system("python2 reg/user/send_password.py")
print('RC Close')