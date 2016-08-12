# Retrieve HTTP protocol to examine the HTTP Response headers.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)    # 512-character chunks
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()
