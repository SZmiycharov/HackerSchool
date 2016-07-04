import socket
import re
import threading
import sys, getopt
import os
import time
import getrandom
import subprocess
import os.path
import logging

logging.basicConfig(filename='/home/slavi/Desktop/webserver1.log',level=logging.DEBUG)

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
	except IOError:
		errorMsg = "File could not be found!"
		client.sendall("""HTTP/1.1 204 No Content
Server: SLAVI
Content-Type: text/html\n
""")
		client.sendall("""
			<html>
			<body>
			<p><b> sum: %s </b></p>
			</body>
			</html>""" % (errorMsg))
		client.close()
		return
		
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
		req = ''
		data = ''
		req = client.recv(8192)
		print req
		request_method = req.split(' ')[0]

#*******************************************************GET**************************************************************************

		if(request_method == 'GET'):
			print "in GET method"
			string = req.split(' ')[1].split('/')[1]
			if string == 'scripts':
				print "GET in first if"
				maxvalue = req.split(' ')[1].split('MAX=')[1].split('\n')[0]
				print maxvalue
				command = "python %s -m %s"%(req.split(' ')[1].split('?')[0].split('/')[2], maxvalue)
				print command
				print req.split(' ')[1].split('?')[0].split('/')[2]
				temp = str(req.split(' ')[1].split('?')[0].split('/')[2])
				if os.path.isfile(temp):
					print "GET after os path isfile"
					output = subprocess.check_output(command, shell=True)
					client.sendall("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html\n""")
	   				client.sendall(output)
					logging.info("Returned 2 random numbers less than %s!"%(maxvalue))
					client.close()
				else:
					client.sendall("""HTTP/1.1 204 No Content
			Server: SLAVI
			Content-Type: text/html\n""")
					client.sendall("""
			<html>
			<body>
			<p><b> NO SUCH FILE! </b></p>
			</body>
			</html>""")
					client.close()

			elif string.split('?')[0] == 'upload':
				filePath = string.split('filePath=')[1].split()[0]
				currFileName = filePath.split('%2F')[-1].split('.')[0]
				currFileType = filePath.split('%2F')[-1].split('.')[1]
				print "filePath: %s"%(filePath)
				newfile = self.directory + "/" + currFileName + "1." + currFileType
				print "newfile: %s"%(newfile)
				length = len(filePath.split('%2F'))
				print length
				absoluteFilePath = ''
				for i in range (1,length):
					print i
					absoluteFilePath += '/' + filePath.split('%2F')[i]
				print absoluteFilePath
				f = open(absoluteFilePath, 'rb')
				f2 = open(newfile, 'wb+')
				bytesToSend = f.read(4096)
				f2.write(bytesToSend)
				while bytesToSend != '':
				    bytesToSend = f.read(4096)
				    f2.write(bytesToSend)
				f.close()
				f2.close()
				client.sendall("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html\n""")
				client.sendall("""
			<html>
			<body>
			<p> File uploaded! </p>
			</body>
			</html>""")	
				logging.info("Uploaded file %s!"%(absoluteFilePath))
				
				client.close()
		

			elif string.split('?')[0] == 'sum':
				print "GET in first elif"
				match = re.match('GET .*?.=(.*)&', req)
				if match:
					a = match.group(1)
					print "a: " + a

					match = re.match('GET .*&.=(.*) HTTP', req)
					if match:
						b = match.group(1)
						print "b: " + b
						try:
							a = int(a)
							b = int(b)
						except ValueError:
							client.sendall("""HTTP/1.1 400 Bad Request
		Server: SLAVI
		Content-Type: text/html\n""")
							client.sendall("""
			<html>
			<body>
			<p><b> BAD PARAMETERS! </b></p>
			</body>
			</html>""")
							client.close()
						else:
							sumOfBoth = a + b
							print "a + b = %s" % (sumOfBoth)
							print "\n"
							client.sendall("""HTTP/1.1 200 OK
		Server: SLAVI
		Content-Type: text/html\n""")
							client.sendall("""
			<html>
			<body>
			<p><b> sum: %d </b></p>
			</body>
			</html>""" % (sumOfBoth))
							logging.info("Found sum of %s and %s!"%(a,b))
							client.close()
			
			elif string == 'files':
				print "GET in second elif"
				fileName = req.split(' ')[1].split('/')[2]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					self.RetrFile(client, fileName)
					client.close()
				elif len(fileName.split('.')) == 1:
					print "GET in third elif"
					client.sendall("""HTTP/1.1 400 Bad Request
			Server: SLAVI
			Content-Type: text/html\n""")
					client.sendall("""
				<html>
				<body>
				<p><b> Web server cannot understand command! </b></p>
				<p>Should be sum, files or scripts</p>
				</body>
				</html>""")
					client.close()
			else:
				print "GET in else"
				client.sendall("""HTTP/1.1 400 Bad Request
			Server: SLAVI
			Content-Type: text/html\n""")
				client.sendall("""
				<html>
				<body>
				<p><b> Web server cannot understand command! </b></p>
				<p>Should be sum, files or scripts</p>
				</body>
				</html>""")
				client.close()
				


#*********************************************************POST**************************************************************************	
	
		elif(request_method == 'POST'):
			print "in POST method"
			file_requested = req.split(' ')[1].split('\n')[0]
			print file_requested
			string = req.split(' ')[1].split('/')[1]
			print string
			if string == 'scripts':
				print "POST in first if"
				maxvalue = req.split('\n')[-1].split('=')[1]
				command = "python %s -m %s"%(req.split(' ')[1].split('?')[0].split('/')[2], maxvalue)
				temp = str(req.split(' ')[1].split('?')[0].split('/')[2])
				if os.path.isfile(temp):
					print "POST after os path isfile"
					output = subprocess.check_output(command, shell=True)
					client.sendall("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html\n""")
	   				client.sendall(output)
					client.close()
				else:
					print "here"
					client.sendall("""HTTP/1.1 204 No Content
			Server: SLAVI
			Content-Type: text/html\n""")
					client.sendall("""
			<html>
			<body>
			<p><b> NO SUCH FILE! </b></p>
			</body>
			</html>""")
					client.close()		
			elif string == 'sum':
				print "POST in first elif"
				parameters = req.split()[-1]
				print("parameters: %s"%(parameters))
				
				string = req.split('&')
				a = string[0].split('=')[-1]
				print("a = %s"%(a))
				b = string[1].split('=')
				b = b[1]
				print("b = %s"%(b))
				try:
					a = int(a)
					b = int(b)
				except ValueError:
					client.sendall("""HTTP/1.1 400 Bad Request
	Server: SLAVI
	Content-Type: text/html\n""")
					client.sendall("""
		<html>
		<body>
		<p><b> BAD <OR MISSING> PARAMETERS! </b></p>
		</body>
		</html>""")
					client.close()
				else:
					sumOfBoth = a + b
					print "a + b = %s" % (sumOfBoth)
					print "\n"
					client.sendall("""HTTP/1.1 200 OK
	Server: SLAVI
	Content-Type: text/html\n""")
					client.sendall("""
		<html>
		<body>
		<p><b> sum: %d </b></p>
		</body>
		</html>""" % (sumOfBoth))
					client.close()
			elif string == 'files':
				print "POST in second elif"
				username = req.split(' ')[1].split('/')[2].split('&')[0].split('=')[1].split('/')[0]
				password = req.split(' ')[1].split('/')[2].split('&')[1].split('=')[1].split('/')[0]
				if username == '' or password == '':
					client.sendall("""HTTP/1.1 401 Unauthorized
	Server: SLAVI
	Content-Type: text/html\n""")
					client.sendall("""
		<html>
		<body>
		<p><b> BAD <OR MISSING> PARAMETERS! </b></p>
		</body>
		</html>""")
					client.close()
				else:
					fileName = file_requested.split('/')[3]
				
					if(username == 'slavi' and password == 'pass'):
						self.RetrFile(client, fileName)
						client.close()
					else:
						client.sendall("""HTTP/1.1 401 Unauthorized
	Server: SLAVI
	Content-Type: text/html\n""")
						client.sendall("""
		<html>
		<body>
		<p><b> Incorrect username or password! </b></p>
		</body>
		</html>""")
						client.close()
			else:
				print "POST in else"
				client.sendall("""HTTP/1.1 400 Bad Request
			Server: SLAVI
			Content-Type: text/html\n""")
				client.sendall("""
				<html>
				<body>
				<p><b> Web server cannot understand command! </b></p>
				<p>Should be sum, files or scripts</p>
				</body>
				</html>""")
				client.close()
				

#*************************************************END OF POST***********************************************************************
		else:
			client.sendall("Cannot recognize request method <should be POST or GET>!")
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



























