from module.client import socket_client
#user_ip ='192.168.1.109'
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.IP import user_ip
socket_client(user_ip,'reg/user/password_update_RC.py')