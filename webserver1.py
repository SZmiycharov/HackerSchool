import socket
import re
import threading
import sys, getopt
import os
import time

class ThreadedServer(object):
    def __init__(self, host, port, directory, clienttimeout = 60, socklisten = 5):
        self.host = host
        self.port = port
	self.directory = directory
	self.clienttimeout = clienttimeout
	self.socklisten = socklisten
        
    def listen(self):
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.socklisten)
        while True:
            client, address = self.sock.accept()
	    print "Connection from: " + `address`
            client.settimeout(self.clienttimeout)
            threading.Thread(target = self.listenToClient,args = (client,)).start()

    def RetrFile(self, client, fileName):
	try:		
		
		filePath = self.directory + '/' + fileName
        	f = open(filePath, 'rb')
		print(filePath)
	except IOError:
		print("in except")
		errorMsg = "File could not be found!"
		client.sendall(errorMsg)
		client.close()
	match = re.match('.*\.(.*)', fileName)
	fileType = match.group(1)

	if(fileType == 'py' or fileType == 'txt'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/plain\n
""")
	elif(fileType == "html" or fileType == "php"):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/html\n
""")
	elif(fileType == 'png'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/png\n
""")
	elif(fileType == 'jpg'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/jpeg\n
""")
	
	while True:
		fileData = f.read()
		if fileData == '': break
		client.sendall(fileData)
	f.close()   

    def listenToClient(self, client):
        while True:
            try:
		req = recv_timeout(client,10)
		print (req)
		string = bytes.decode(req)
		request_method = string.split(' ')[0]
		if(request_method == 'GET'):
		        match = re.match('GET .*?.=(\d+)', req)
			if match:
				client.sendall("""HTTP/1.1 200 OK
	Server: SLAVI
	Content-Type: text/html\n""")
				a = match.group(1)
				print "a: " + a

				match = re.match('GET .*&.=(\d+) HTTP', req)
				if match:
					b = match.group(1)
					print "b: " + b
					sumOfBoth = int(a) + int(b)
					print "a + b = %s" % (sumOfBoth)
					print "\n"
					client.sendall("""
	<html>
	<body>
	<p><b> sum: %d </b></p>
	</body>
	</html>""" % (sumOfBoth))
					client.close()

			else:
				match = re.match('GET /(.*) ', req)
				fileName = match.group(1)
				self.RetrFile(client, fileName)
				client.close()
		elif(request_method == 'POST'):
			file_requested = string.split(' ')[1]
			print("file requested: %s"%(file_requested))
			
			if(file_requested == '/sum'):
				parameters = string.split()[-1]
				print("parameters: %s"%(parameters))
				if parameters:
					string = req.split('&')
					a = string[0].split('=')
					a = a[1]
					print("a = %s"%(a))
					b = string[1].split('=')
					b = b[1]
					print("b = %s"%(b))
					sumOfBoth = int(a) + int(b)
					result = "a + b = %s" % (sumOfBoth)
					print result
					client.sendall(result)
					client.close()
				else:
					print("Parameters should be specified!")
					client.close()
			else:
				username = req.split(' ')[1].split('&')[0].split('=')[1].split('/')[0]
				password = req.split(' ')[1].split('&')[1].split('=')[1].split('/')[0]
				fileName = file_requested.split('/')[2]
				if(username == 'slavi' and password == 'pass'):
					self.RetrFile(client, fileName)
					client.close()
				else:
					print("Not acceptable username and/or passowrd")
					client.close()
		else:
			print("Cannot recognize %s request!"%(request_method))
			client.close()
	    except:
	    	client.close()

def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)
     
    #total data partwise in an array
    total_data=[];
    data='';
     
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
     
    #join all parts to make final string
    return ''.join(total_data)

if __name__ == "__main__":
	host = '' 
	port = '8080'
	directory = '/home/slavi/Desktop'
	#get port and folder from cmd line
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hp:f:",["port=", "directory="])		
	except getopt.GetoptError:
		print 'webserver1.py -p <port> -f <directory>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'webserver1.py -p <port> -f <directory>'
			sys.exit()
	    	elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-f", "--directory"):
			directory = arg
	port = int(port)
	if (port>=64000 or port<=1): 
		print("should specify port as parameter!")
		sys.exit()
	if not os.path.isdir(directory):
		print("not a valid directory")
		sys.exit()
		
	print("                      **********SERVER STARTED**********")
	ThreadedServer('', port, directory).listen()



























