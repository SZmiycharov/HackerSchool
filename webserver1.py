import socket
import re
import threading
import sys, getopt
import os

#za vseki tip fail da se pra6ta header - DONE!
#error handling ako ne su6testvuva faila - DONE!
#open za cheteneto na failove kakvi gre6ki vru6ta - DONE!
#ot koq papka da se vzimat failovete - DONE!




def RetrFile(sock, filename):
	try:		
		filePath = folder + "/" + filename
        	f = open(filePath, 'rb')
		print(filePath)
	except IOError:
		errorMsg = "File %s could not be found!" %(filename)
		sock.send(errorMsg)
		sock.close()
		return
	except:
    		print "Unexpected error:", sys.exc_info()[0]
    		return

	match = re.match('.*\.(.*)', filename)
	fileType = match.group(1)

	if(fileType == "html" or fileType == "php"):
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
	elif(fileType == 'pdf'):
		sock.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: application/pdf\n
""")
	elif(fileType == 'avi'):
		sock.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: video/x-msvideo\n
""")
	else:
		sock.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/plain\n
""")
	
	while True:
		fileData = f.read()
		if fileData == '': break
		sock.sendall(fileData)
	
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
try:
	sock.bind((host, port))
except socket.error as e:
	print(str(e))
sock.listen(5) 
print("                   ************SERVER STARTED************")

def threaded_client(csock):
	print("in threaded_client")
	while True:
	    req = csock.recv(4096) # get the request, 3kB max
	    print req
	    print("after req")
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

			csock.send("""HTTP/1.1 200 OK
		Server: SLAVI
		Content-Type: text/html

		<html>
		<body>
		<p><b> sum: %d </b></p>
		</body>
		</html>
				""" % (sumOfBoth))
	    
	    elif re.match('GET /(.*) ', req):
		match = re.match('GET /(.*) ', req)
		fileName = match.group(1)
		#get the file
		t = threading.Thread(target=RetrFile, args=("RetrThread", csock, fileName))
		t.start()
	    else:
		csock.send("Invalid request!\n")
		csock.close()
	csock.close()

while True:
	csock, caddr = sock.accept()
	print "Connection from: " + `caddr`
	tr = threading.Thread(target=threaded_client, args=(csock,))
	tr.start()

















