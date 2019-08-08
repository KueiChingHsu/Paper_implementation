from module.client import socket_client
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.IP import RC_ip
#server_ip ='192.168.1.109'
socket_client(RC_ip,'reg/module/parameter/reg_server_parameter.py')


