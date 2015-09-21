import socket
import spidev
import time
print 'start'

host='192.168.1.100'  #client
port = 8087
addr = (host,port)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 15*1000*1000
a=0x00
print "Starting up on %s:%s" % addr
s.connect(addr)
while True:
    to_send = [a]
    
    #spi.xfer(to_send)
    spi.writebytes(to_send)
    ss = spi.readbytes(1)
    print ss
    spi_data = '%d' %ss[0]
    s.sendto(spi_data,(addr))
    #data = s.recv(1024)
    #print 'Received',data
    a=a+1
