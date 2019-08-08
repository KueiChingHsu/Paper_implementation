from module.client import socket_client
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.IP import user_ip
#user_ip ='10.17.173.29'
socket_client(user_ip,'reg/user/extractor.pickle')
socket_client(user_ip,'reg/user/helper.pickle')
socket_client(user_ip,'reg/user/password_update_RC.py')

