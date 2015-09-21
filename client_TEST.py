# -*- coding: utf-8 -*-

import socket

HOST = '192.168.1.100'                 # Symbolic name meaning all available interfaces
PORT = 8087              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    print 'Received', repr(data)
    #if not data: break
    conn.sendall(data)
conn.close()
