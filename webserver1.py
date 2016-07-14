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
import ResponseHeader
import ServerFunctions
import RequestHandler
import ssl
import asyncore

ssl_keyfile = "/home/slavi/Desktop/HackerSchool/ssl_key"
ssl_certfile = "/home/slavi/Desktop/HackerSchool/ssl_cert"

logging.basicConfig(format='%(asctime)s %(message)s',filename='/home/slavi/Desktop/webserver1.log',level=logging.DEBUG )
try:
	conn = psycopg2.connect("dbname='httpAuth' user='slavi' host='localhost' password='3111'")
except:
	print "Unable to connect to the database"
cur = conn.cursor()

ssl_keyfile = "/home/slavi/Desktop/Tasks-Telebid/ssl_key"
ssl_certfile = "/home/slavi/Desktop/Tasks-Telebid/ssl_cert"


class ListenToClient(asyncore.dispatcher_with_send):
	directory = '/home/slavi/Desktop'
	def handle_read(self):
		while True:
			try:
				req = ''
				data = ''
				req = self.recv(8192)
				request_method = req.split(' ')[0]
				print req
			except:
				sys.stderr.write("Fail with socket\n\n") 

			if(request_method == 'GET'):
				print "in GET method"
				RequestHandler.HandleGET(self, req, directory)	
			elif(request_method == 'POST'):
				print "in POST method"
				RequestHandler.HandlePOST(self, req, cur, conn, directory)	
			else:
				self.sendall("Cannot recognize request method <should be POST or GET>!")
				logging.error("Could not recognize request!")
				self.close()

class Server(asyncore.dispatcher):
    SendingCredentials = 0
    DownloadedFiles = 0	
    UploadedFiles = 0
    authenticationCode = 0
    def __init__(self, host = '', port = 8080, directory = '/home/slavi/Desktop', clienttimeout = 60, socklisten = 5):
    	asyncore.dispatcher.__init__(self)
    	self.host = host
    	self.port = port
    	self.directory = directory
    	self.clienttimeout = clienttimeout
    	self.socklisten = socklisten

    	self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    	self.set_reuse_addr()
    	self.bind((host,port))
    	self.listen(self.socklisten)
    
    def handle_accept(self):
    	client,address = self.accept()
    	client = ssl.wrap_socket(client,
                                 server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key")
    	handler = ListenToClient(client) 		    
			
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
			sys.exit(0)
	    	elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-f", "--directory"):
			directory = arg
		else:
			print 'webserver1.py -p <port> -f <directory>'
			sys.exit(0)
	port = int(port)
	if (port>=65000 or port<=1): 
		print("should specify port as parameter!")
		sys.exit(0)
	if not os.path.isdir(directory):
		print("not a valid directory")
		sys.exit(0)
		
	print("                      **********SERVER STARTED**********")
	server = Server('')
	asyncore.loop()
