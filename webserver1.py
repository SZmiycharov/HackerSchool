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
import re
import cgi
import Response
import ServerFunctions

logging.basicConfig(format='%(asctime)s %(message)s',filename='/home/slavi/Desktop/webserver1.log',level=logging.DEBUG )
try:
    conn = psycopg2.connect("dbname='httpAuth' user='slavi' host='localhost' password='3111'")
except:
    print "I am unable to connect to the database"
cur = conn.cursor()

class Server(object):	
    def __init__(self, host, port, directory, clienttimeout = 60, socklisten = 5):
    	self.host = host
    	self.port = port
    	self.directory = directory
    	self.clienttimeout = clienttimeout
    	self.socklisten = socklisten
    
	def uploadFile(fileextension, fileToUpload):
		serverFile = self.directory + '/newfile.' + fileextension
		f = open(serverFile, 'wb+')
		f.write(fileToUpload)
		f.close()

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
		
    def listenToClient(self, client):
        while True:
            try:
		req = ''
		data = ''
		req = recv_timeout(client, 1)
		request_method = req.split(' ')[0]

#*******************************************************GET**************************************************************************

		if(request_method == 'GET'):
			print "in GET method"
			string = req.split(' ')[1].split('/')[1]
			if string == 'scripts':
				print "GET in first if"
				maxvalue = req.split(' ')[1].split('MAX=')[1].split('\n')[0]
				command = "python %s -m %s"%(req.split(' ')[1].split('?')[0].split('/')[2], maxvalue)
				temp = str(req.split(' ')[1].split('?')[0].split('/')[2])
				if os.path.isfile(temp):
					print "GET after os path isfile"
					output = subprocess.check_output(command, shell=True)
					Response.Response(client, '200 OK', 'text/html').SendResponse()
	   				client.sendall(output)
					logging.info("Returned 2 random numbers less than %s; GET!"%(maxvalue))
					client.close()
				else:
					Response.Response(client, '400 Bad Response', 'text/html').SendResponse()
					Response.Response().SendNoSuchFileResponse()
					logging.error("File could not be found; GET!")
					client.close()
			elif string == 'upload':
				print "in upload"
				Response.Response(client, '200 OK', 'text/html').SendResponse()
				Response.Response().SendFormForUpload(client)		
				client.close()
			elif string.split('?')[0] == 'download':
				print "in GET download"
				fileName = string.split('file=')[1].split()[0]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					print fileName
					ServerFunctions.ServerFunctions(client, fileName, self.directory).RetrFile()
					logging.info("Retrieved file %s; GET!"%(fileName))
					client.close()
				elif len(fileName.split('.')) == 1:
					print "GET in third elif"
					Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
					Response.Response().SendCannotUnderstandCommandResponse(client)
					logging.error("Bad command; user tried: %s; GET!"%(string))
					client.close()

			elif string.split('?')[0] == 'sum':
				print "GET in first elif"
				match = re.match('GET .*?.=(.*)&', req)
				if match:
					a = match.group(1)
					match = re.match('GET .*&.=(.*) HTTP', req)
					if match:
						b = match.group(1)
						try:
							a = int(a)
							b = int(b)
						except ValueError:
							Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
							Response.Response().SendBadParametersResponse(client)
							logging.error("Bad parameters for sum; GET!")
							client.close()
						else:
							sumOfBoth = a + b
							Response.Response(client, '200 OK', 'text/html').SendResponse()
							Response.Response().SendSumResponse(client, sumOfBoth)
							logging.info("Found sum of %s and %s; GET!"%(a,b))
							client.close()
			
			elif string == 'files':
				print "GET in second elif"
				fileName = req.split(' ')[1].split('/')[2]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					ServerFunctions.ServerFunctions(client,fileName,self.directory).RetrFile(False)
					logging.info("Retrieved file %s; GET!"%(fileName))
					client.close()
				elif len(fileName.split('.')) == 1:
					print "GET in third elif"
					Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
					Response.Response().SendCannotUnderstandCommandResponse(client)
					logging.error("Bad command; user tried: %s; GET!"%(string))
					client.close()
			else:
				print "GET in else"
				Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
				Response.Response().SendCannotUnderstandCommandResponse(client)
				logging.error("Bad command; user tried: %s; GET!"%(string))
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
					Response.Response(client, '200 OK', 'text/html').SendResponse()
	   				client.sendall(output)
					logging.info("Executed program: %s; POST!"%(req.split(' ')[1].split('?')[0].split('/')[2]))
					client.close()
				else:
					Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
					Response.Response().SendNoSuchFileResponse()
					logging.error("File %s could not be found; POST!"%(req.split(' ')[1].split('?')[0].split('/')[2]))
					client.close()	
			
			elif string == 'sum':
				print "POST in first elif"
				parameters = req.split()[-1]
				string = req.split('&')
				a = string[0].split('=')[-1]
				b = string[1].split('=')
				b = b[1]
				try:
					a = int(a)
					b = int(b)
				except ValueError:
					Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
					Response.Response().SendBadParametersResponse(client)
					logging.error("Bad parameters for sum; POST!"%())
					client.close()
				else:
					sumOfBoth = a + b
					Response.Response(client, '200 OK', 'text/html').SendResponse()
					Response.Response().SendSumResponse(client, sumOfBoth)
					logging.info("Returned sum of %s and %s; POST"%(a,b))
					client.close()
			elif string == 'files':
				print "POST in second elif"
				username = req.split(' ')[1].split('/')[2].split('&')[0].split('=')[1].split('/')[0]
				password = req.split(' ')[1].split('/')[2].split('&')[1].split('=')[1].split('/')[0]
				if username == '' or password == '':
					Response.Response(client, '401 Unauthorized', 'text/html').SendResponse()
					Response.Response().SendBadParametersResponse(client)
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
									credentialsCorrect = True
									ServerFunctions.ServerFunctions(client,fileName,self.directory).RetrFile(False)
									logging.info("Retrieved file %s; POST!"%(fileName))
									if fileName == 'success.png':
										contType = req.split('Content-Type')[2].split(': ')[1].split('\n')[0]
										contType = contType.split('\r')[0]
										fileToUpload = req.split('Content-Type')[2].split(': ')[1].split(contType)[1].split('-----------------------------')[0].split('\r\n\r\n')[1].split('\n\r')[0]
										if contType == 'text/plain':
											ServerFunctions.ServerFunctions().uploadFile('txt', fileToUpload, self.directory)
										elif contType == 'text/x-python':
											ServerFunctions.ServerFunctions().uploadFile('py', fileToUpload, self.directory)
										elif contType == 'image/jpeg':
											ServerFunctions.ServerFunctions().uploadFile('jpg', fileToUpload, self.directory)
										elif contType == 'image/png':
											ServerFunctions.ServerFunctions().uploadFile('png', fileToUpload, self.directory)
									client.close()
							
					if not credentialsCorrect:
						Response.Response(client, '401 Unauthorized', 'text/html').SendResponse()
						Response.Response().SendIncorrectUsernameOrPasswordResponse(client)
						logging.error("User tried incorrect username or password; POST!")
						client.close()
			else:
				print "POST in else"
				Response.Response(client, '400 Bad Request', 'text/html').SendResponse()
				Response.Response().SendCannotUnderstandCommandResponse(client)
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
	if (port>=64000 or port<=1): 
		print("should specify port as parameter!")
		sys.exit()
	if not os.path.isdir(directory):
		print("not a valid directory")
		sys.exit()
		
	print("                      **********SERVER STARTED**********")
	Server('', port, directory).listen()
