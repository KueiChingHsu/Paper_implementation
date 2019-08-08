
#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: send.py
socket client
"""



import socket
import os
import sys
import struct


def socket_client(ip,filepath):
#def socket_client(filepath):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)

    print s.recv(1024)

    while 1:
        #filepath = '/home/kuei/Dropbox/test/sender/server1_user_parameter2_1.py'
        if os.path.isfile(filepath):
           
            fileinfo_size = struct.calcsize('128sl')
            
            fhead = struct.pack('128sl', os.path.basename(filepath),
                                os.stat(filepath).st_size)
            s.send(fhead)
            print 'send file: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    #print '{0} file send over...'.format(filepath)
                    break
                s.send(data)
        s.close()
        break


if __name__ == '__main__':
    socket_client()
