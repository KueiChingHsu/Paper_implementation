from module.client import socket_client
import sys
import os
o_path = os.getcwd()
sys.path.append(o_path)
from auth.IP import RC_ip
#RC_ip='10.17.173.100'
socket_client(RC_ip,'reg/module/parameter/reg_user_parameter.py')