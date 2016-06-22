import socket
import re
import threading
import sys, getopt
import os

def RetrFile(conn, filename):
	try:		
		filePath = folder + "/" + filename
        	f = open(filePath, 'rb')
		print(filePath)
	except IOError:
		errorMsg = "File could not be found!"
		conn.send(errorMsg)
		return

	match = re.match('.*\.(.*)', filename)
	fileType = match.group(1)

	
	if(fileType == 'py' or fileType == 'txt'):
		conn.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/plain\n
""")
	elif(fileType == "html" or fileType == "php"):
		conn.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/html\n
""")
	elif(fileType == 'png'):
		conn.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/png\n
""")
	elif(fileType == 'jpg'):
		conn.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/jpeg\n
""")
	while True:
		fileData = f.read()
		if fileData == '': break
		conn.sendall(fileData)
	print("finished while loop")
	f.close()
	conn.close()

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


def threaded_client(conn):
	while True:
	    req = conn.recv(4096) # get the request, 3kB max
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

			conn.send("""HTTP/1.1 200 OK
		Server: SLAVI
		Content-Type: text/html

		<html>
		<body>
		<p><b> sum: %d </b></p>
		</body>
		</html>
				""" % (sumOfBoth))
			conn.send("\n")
			conn.close()
			return
	    
	    elif re.match('GET /(.*) ', req):
		match = re.match('GET /(.*) ', req)
		fileName = match.group(1)
		RetrFile(conn, fileName)
		return
	    else:
		conn.send("Invalid request!\n")
		return


print("                   ************SERVER STARTED************")
while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#change socket behaviour - to be able to reconnect faster
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		sock.bind((host, port))
	except socket.error as e:
		print(str(e))
	sock.listen(5) 
	conn, addr = sock.accept()
	print "Connection from: " + `addr`
	tr = threading.Thread(target=threaded_client, args=(conn,))
	tr.start()







