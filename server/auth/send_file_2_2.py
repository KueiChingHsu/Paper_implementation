from client import socket_client
from IP import RC_ip
#RC_ip='192.168.1.107'
socket_client(RC_ip,'auth/server1_rc_parameter2_2.py')
socket_client(RC_ip,'auth/extractor.pickle')
socket_client(RC_ip,'auth/helper.pickle')