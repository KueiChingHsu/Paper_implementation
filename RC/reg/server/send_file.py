from module.client import socket_client
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.IP import server_ip
#server_ip ='192.168.1.108'
socket_client(server_ip,'reg/server/module/parameter/reg_server_RC_parameter.py')


