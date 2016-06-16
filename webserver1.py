import socket
import re
import threading
import sys, getopt
import os

#za vseki tip fail da se pra6ta header
#error handling ako ne su6testvuva faila - DONE!
#open za cheteneto na failove kakvi gre6ki vru6ta - DONE!
#ot koq papka da se vzimat failovete - DONE!

def RetrFile(name, sock, filename):
	try:		
		filePath = folder + "/" + filename
        	f = open(filePath, 'rb')
	except IOError:
		errorMsg = "File could not be found!"
		sock.send(errorMsg)
		sock.close()
		return

	fileType = filename[-3:]
	print(fileType)
	
	if(fileType == '.py' or fileType == 'txt'):
		sock.send("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/plain\n
			""")
	elif(fileType == 'tml'):
		sock.send("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html\n
			""")
	elif(fileType == 'png'):
		sock.send("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: image/png\n
			""")
	elif(fileType == 'jpg'):
		sock.send("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: image/jpeg\n 
			""")

	bytesToSend = f.read(1024)
	sock.send(bytesToSend)
        while bytesToSend != "":
        	bytesToSend = f.read(1024)
        	sock.send(bytesToSend)
	f.close()
	sock.close()

host = '' 
port = ''
folder = ''

#get port and folder from cmd line
try:
	opts, args = getopt.getopt(sys.argv[1:],"hp:f:",["port=", "folder="])
except getopt.GetoptError:
	print 'webserver1.py -p <port> -f <folder>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
        	print 'webserver1.py -p <port> -f <folder>'
        	sys.exit()
    	elif opt in ("-p", "--port"):
        	port = arg
	elif opt in ("-f", "--folder"):
        	folder = arg
port = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#change socket behaviour - to be able to reconnect faster
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
#queue the requests
sock.listen(5) 

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(4096) # get the request, 1kB max
    print req
    # req should be sth like GET /move?a=20&b=3 HTTP/1.1

    match = re.match('GET .*?.=(\d+)', req)
    if match:
        a = match.group(1)
        print "a: " + a

    match = re.match('GET .*&.=(\d+)', req)
    if match:
        b = match.group(1)
        print "b: " + b
	sumOfBoth = int(a) + int(b)
	print "a + b = %d" % (sumOfBoth)
	print "\n"

        csock.sendall("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html

			<html>
			<body>
			sum: %d
			</body>
			</html>
			""" % (sumOfBoth))
	csock.close()

    match = re.match('GET /(.*) ', req)
    if match:
        fileName = match.group(1)
        print "file: " + fileName
	#get the file
	t = threading.Thread(target=RetrFile, args=("RetrThread", csock, fileName))
        t.start()
	print("after t.start()")
	helper = folder + "/" + fileName
	print(helper)

csock.close()


