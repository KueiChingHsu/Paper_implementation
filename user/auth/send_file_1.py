from client import socket_client
from IP import server_ip
#server_ip='192.168.1.103'
socket_client(server_ip,'auth/user1_parameter.py')
socket_client(server_ip,'auth/extractor.pickle')
socket_client(server_ip,'auth/helper.pickle')