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
import psycopg2
from multiprocessing import Process
import os

logging.basicConfig(format='%(asctime)s %(message)s',filename='/home/slavi/Desktop/webserver1.log',level=logging.DEBUG )
try:
    conn = psycopg2.connect("dbname='httpAuth' user='slavi' host='localhost' password='3111'")
except:
    print "Unable to connect to the database"
cur = conn.cursor()


class ThreadedServer(object):
    def __init__(self, host, port, directory, clienttimeout = 6, socklisten = 1000):
        self.host = host
        self.port = port
	self.directory = directory
	self.clienttimeout = clienttimeout
	self.socklisten = socklisten
	self.downloadedFiles = []
	self.downloadedFiles.append(0)
	self.uploadedFiles = []
	self.uploadedFiles.append(0)
        
    def listen(self):
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.socklisten)
	while True:
		client, address = self.sock.accept()
		print "Connection from: " + `address`
		try:
			child_pid = os.fork()
			if child_pid == 0:
				print "true"
				childpid = os.getpid()
				self.listenToClient(client)
			else:
				sys.exit(0)
		except OSError, e:
			print "exrept oserror"
			sys.exit(1)
		
	print "out of for loop**********************************************"

    def RetrFile(self, client, fileName):
	try:		
		filePath = self.directory + '/' + fileName
        	f = open(filePath, 'rb')
	except IOError:
		errorMsg = "File could not be found!"
		client.sendall("""HTTP/1.1 400 Bad Request
Server: SLAVI
Content-Type: text/html\n
""")
		client.sendall("""
			<html>
			<body>
			<p><b> %s </b></p>
			</body>
			</html>""" % (errorMsg))
		logging.error("File %s could not be found!"%(fileName))
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
					logging.info("Returned 2 random numbers less than %s; GET!"%(maxvalue))
					client.close()
				else:
					client.sendall("""HTTP/1.1 400 Bad Request
			Server: SLAVI
			Content-Type: text/html\n""")
					client.sendall("""
			<html>
			<body>
			<p><b> NO SUCH FILE! </b></p>
			</body>
			</html>""")
					logging.error("File could not be found; GET!")
					client.close()

			elif string.split('?')[0] == 'upload':
				filePath = string.split('filePath=')[1].split()[0]
				currFileName = filePath.split('%2F')[-1].split('.')[0]
				currFileType = filePath.split('%2F')[-1].split('.')[1]
				print "filePath: %s"%(filePath)
				newfile = self.directory + "/" + currFileName + "1." + currFileType
				print "newfile: %s"%(newfile)
				length = len(filePath.split('%2F'))
				absoluteFilePath = ''
				for i in range (1,length):
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
				self.uploadedFiles[0] += 1
				print self.uploadedFiles[0]
				client.sendall("""HTTP/1.1 200 OK
			Server: SLAVI
			Content-Type: text/html\n""")
				client.sendall("""
			<html>
			<body>
			<p> File uploaded! </p>
			<p> %s files already uploaded! </p>
			</body>
			</html>"""%(self.uploadedFiles[0]))	
				logging.info("Uploaded file %s; GET!"%(absoluteFilePath))
				
				
				
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
							logging.error("Bad parameters for sum; GET!")
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
							logging.info("Found sum of %s and %s; GET!"%(a,b))
							client.close()
							return
			
			elif string == 'files':
				print "GET in second elif"
				fileName = req.split(' ')[1].split('/')[2]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					self.RetrFile(client, fileName)
					logging.info("Retrieved file %s; GET!"%(fileName))
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
					logging.error("Bad command; user tried: %s; GET!"%(string))
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
				logging.error("Bad command; user tried: %s; GET!"%(string))
				client.close()
				


#*********************************************************POST**************************************************************************	
	
		elif(request_method == 'POST'):
			print "in POST method"
			file_requested = req.split(' ')[1].split('\n')[0]
			print file_requested
			string = req.split(' ')[1].split('/')[1]
			print string
			if string == 'upload':
				print "POST in upload"
				currFileName = req.split('%2F')[-1].split('.')[0]
				print currFileName
				currFileType = req.split('%2F')[-1].split('.')[1]
				print currFileType
				newfile = self.directory + "/" + currFileName + "1." + currFileType
				length = len(req.split('\n')[-1].split('filePath=')[1].split('%2F'))
				absoluteFilePath = ''
				for i in range (1,length):
					absoluteFilePath += "/" + req.split('\n')[-1].split('filePath=')[1].split('%2F')[i]
				print "abs path: %s"%(absoluteFilePath)
				print "newfile: %s"%(newfile)
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
			<p> %s files already uploaded! </p>
			</body>
			</html>"""%(self.uploadedFiles[0]))	
				logging.info("Uploaded file %s; GET!"%(absoluteFilePath))
				
				client.close()
				
			elif string == 'scripts':
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
					logging.info("Executed program: %s; POST!"%(req.split(' ')[1].split('?')[0].split('/')[2]))
					client.close()
				else:
					client.sendall("""HTTP/1.1 400 Bad Request
			Server: SLAVI
			Content-Type: text/html\n""")
					client.sendall("""
			<html>
			<body>
			<p><b> NO SUCH FILE! </b></p>
			</body>
			</html>""")
					logging.error("File %s could not be found; POST!"%(req.split(' ')[1].split('?')[0].split('/')[2]))
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
					logging.error("Bad parameters for sum; POST!"%())
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
					logging.info("Returned sum of %s and %s; POST"%(a,b))
					client.close()
			elif string == 'files':
				print "POST in second elif"
				username = req.split(' ')[1].split('/')[2].split('&')[0].split('=')[1].split('/')[0]
				password = req.split(' ')[1].split('/')[2].split('&')[1].split('=')[1].split('/')[0]
				print username
				print password
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
					logging.info("Wrong username/password; POST!")
					client.close()
				else:
					credentialsCorrect = False
					fileName = file_requested.split('/')[3]
					cur.execute("""SELECT username FROM users""")
					rows = cur.fetchall()
					for row in rows:
						if row[0] == username:
							cur.execute("""SELECT password FROM users""")
							rows = cur.fetchall()
							for row in rows:
								if row[0] == password:
									print "heASHDAHSDHAre"
									credentialsCorrect = True
									self.RetrFile(client, fileName)
									logging.info("Retrieved file %s; POST!"%(fileName))
									client.close()
							
					if not credentialsCorrect:
						client.sendall("""HTTP/1.1 401 Unauthorized
	Server: SLAVI
	Content-Type: text/html\n""")
						client.sendall("""
		<html>
		<body>
		<p><b> Incorrect username or password! </b></p>
		</body>
		</html>""")
						logging.error("User tried incorrect username or password; POST!")
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
				logging.error("Wrong command; user tried: %s; POST"%(string))
				client.close()
				

#*************************************************END OF POST***********************************************************************
		else:
			client.sendall("Cannot recognize request method <should be POST or GET>!")
			logging.error("Could not recognize request!")
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
	if (port>=65535 or port<=1): 
		print("should specify valid port as parameter!")
		sys.exit()
	if not os.path.isdir(directory):
		print("not a valid directory")
		sys.exit()
		
	print("                      **********SERVER STARTED**********")
	ThreadedServer('', port, directory).listen()



























