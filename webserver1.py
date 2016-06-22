import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port, folder):
        self.host = host
        self.port = port
	self.folder = folder
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def RetrFile:
	try:		
		filePath = self.folder + "/" + filename
        	f = open(filePath, 'rb')
		print(filePath)
	except IOError:
		errorMsg = "File could not be found!"
		sock.send(errorMsg)
		sock.close()
		return

	match = re.match('.*\.(.*)', filename)
	fileType = match.group(1)

	
	if(fileType == 'py' or fileType == 'txt'):
		sock.send("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/plain\n
""")
	elif(fileType == "html" or fileType == "php"):
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
	

	while True:
		fileData = f.read()
		if fileData == '': break
		sock.sendall(fileData)
	f.close()   

    def listenToClient(self, client, address):
        while True:
            try:
                req = client.recv(1024)
                if data:
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
			csock.close()

		    
		    else:
			match = re.match('GET /(.*) ', req)
			fileName = match.group(1)
			#get the file
			t = threading.Thread(target=RetrFile, args=("RetrThread", csock, fileName))
			t.start()
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
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
	ThreadedServer('', port, folder).listen()