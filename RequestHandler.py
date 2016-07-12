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
import base64
import logging

def HTTPBasicAuthentication(req, cur):
	authorization = req.split('Authorization:')
	credentialsCorrect = False
	if len(authorization) == 2:
		encodedCredentials = req.split('Authorization:')[1].split('\r\n')[0].split(' ')[2]
		decodedCredentials = base64.b64decode(encodedCredentials)
		username = decodedCredentials.split(':')[0]
		password = decodedCredentials.split(':')[1]
		if username == '' or password == '':
				ResponseHeader.ResponseHeader().SendAuthenticationResponse(client)
				logging.info("Wrong username/password; POST!")
				client.close()
		else:
				cur.execute("""SELECT username FROM users""")
				rows = cur.fetchall()
				for row in rows:
					if row[0] == username:
						cur.execute("""SELECT password FROM users""")
						rows = cur.fetchall()
						for row in rows:
							if row[0] == password:
								credentialsCorrect = True
								break
							else: 
								client.close()
					else: 
						client.close()
	return credentialsCorrect

def HandleGET(client, req, directory):
			string = req.split(' ')[1].split('/')[1]
			print "string: %s" %(string)
			if string == 'scripts':
				print "GET in first if"
				maxvalue = req.split(' ')[1].split('MAX=')[1].split('\n')[0]
				if len(req.split(' ')[1].split('?')[0].split('/')[2])>=2:
					command = "python %s -m %s"%(req.split(' ')[1].split('?')[0].split('/')[2], maxvalue)
				temp = str(req.split(' ')[1].split('?')[0].split('/')[2])
				if os.path.isfile(temp):
					print "GET after os path isfile"
					output = subprocess.check_output(command, shell=True)
					ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
	   				client.sendall(output)
					logging.info("Returned 2 random numbers less than %s; GET!"%(maxvalue))
					client.close()
				else:
					ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendNoSuchFileResponse()
					logging.error("File could not be found; GET!")
					client.close()

			elif string == '':
				ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
				client.sendall('''<!DOCTYPE html>
<html>
<body>

<h1 style="color:red;">SLAVI THE BEST :D</h1>


</body>
</html>
''')
				client.close()

			elif string.split('?')[0] == 'download':
				print "in GET download"
				fileName = string.split('file=')[1].split()[0]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					ServerFunctions.ServerFunctions(client, fileName, directory).RetrFile()
					logging.info("Retrieved file %s; GET!"%(fileName))
					client.close()
				else:
					print "GET in third elif"
					ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendCannotUnderstandCommandResponse(client)
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
							ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
							ResponseHeader.ResponseHeader().SendBadParametersResponse(client)
							logging.error("Bad parameters for sum; GET!")
							client.close()
							
						else:
							sumOfBoth = a + b
							ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
							ResponseHeader.ResponseHeader().SendSumResponse(client, sumOfBoth)
							logging.info("Found sum of %s and %s; GET!"%(a,b))
							client.close()
							
					else:
						ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
						ResponseHeader.ResponseHeader().SendBadParametersResponse(client)
						logging.error("Bad parameters for sum; GET!")
						client.close()
						
				else:
					ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendBadParametersResponse(client)
					logging.error("Bad parameters for sum; GET!")
					client.close()
					
			
			elif string == 'files':
				print "GET in second elif"
				fileName = req.split(' ')[1].split('/')[2]
				if len(fileName.split('.')) > 1:
					print "GET in second if"
					ServerFunctions.ServerFunctions(client,fileName,directory).RetrFile(False)
					logging.info("Retrieved file %s; GET!"%(fileName))
					client.close()
					
				else:
					print "GET in third elif"
					ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendCannotUnderstandCommandResponse(client)
					logging.error("Bad command; user tried: %s; GET!"%(string))
					client.close()
					

			else:
				print "GET in else"
				ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
				ResponseHeader.ResponseHeader().SendCannotUnderstandCommandResponse(client)
				logging.error("Bad command; user tried: %s; GET!"%(string))
				client.close()

def HandlePOST(client, req, cur, directory):
			file_requested = req.split(' ')[1].split('\n')[0]
			string = req.split(' ')[1].split('/')[1]
			credentialsCorrect = HTTPBasicAuthentication(req, cur)

			if credentialsCorrect:
				print "credentials are correct!"
				if string == 'scripts':
					print "POST in first if"
					maxvalue = req.split('\n')[-1].split('=')[1]
					print maxvalue
					command = "python %s -m %s"%(req.split(' ')[1].split('?')[0].split('/')[2], maxvalue)
					print command
					temp = str(req.split(' ')[1].split('?')[0].split('/')[2])
					print temp
					if os.path.isfile(temp):
						print "POST after os path isfile"
						output = subprocess.check_output(command, shell=True)
						ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
		   				client.sendall(output)
						logging.info("Executed program: %s; POST!"%(req.split(' ')[1].split('?')[0].split('/')[2]))
						client.close()
						
					else:
						ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
						ResponseHeader.ResponseHeader().SendNoSuchFileResponse()
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
						ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
						ResponseHeader.ResponseHeader().SendBadParametersResponse(client)
						logging.error("Bad parameters for sum; POST!"%())
						client.close()
						
					else:
						sumOfBoth = a + b
						ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
						ResponseHeader.ResponseHeader().SendSumResponse(client, sumOfBoth)
						logging.info("Returned sum of %s and %s; POST"%(a,b))
						client.close()
						

				elif string == 'upload':
					print "in handlepost upload"
					contType = req.split('Content-Type')[2].split(': ')[1].split('\n')[0].split('\r')[0]
					print "contType: %s"%(contType)
					fileToUpload = req.split('\r\n\r\n')[2].split('----')[0].split('\n\r\n')[0]
					if contType == 'text/plain':
						ServerFunctions.ServerFunctions().uploadFile('txt', fileToUpload, directory)
					elif contType == 'text/x-python':
						ServerFunctions.ServerFunctions().uploadFile('py', fileToUpload, directory)
					elif contType == 'image/jpeg':
						ServerFunctions.ServerFunctions().uploadFile('jpg', fileToUpload, directory)
					elif contType == 'image/png':
						ServerFunctions.ServerFunctions().uploadFile('png', fileToUpload, directory)

					ResponseHeader.ResponseHeader(client, '200 OK', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendUploadResponse(client)
					client.close()
					

				elif string == 'files':
					print "POST in second elif"
					fileName = file_requested.split('/')[2]
					ServerFunctions.ServerFunctions(client,fileName,directory).RetrFile(False)
					logging.info("Retrieved file %s; POST!"%(fileName))
					client.close()
					

				else:
					print "POST in else"
					ResponseHeader.ResponseHeader(client, '400 Bad Request', 'text/html').SendResponse()
					ResponseHeader.ResponseHeader().SendCannotUnderstandCommandResponse(client)
					logging.error("Wrong command; user tried: %s; POST"%(string))
					client.close()
			
			else:
				print "Credentials not correct!"
				ResponseHeader.ResponseHeader().SendAuthenticationResponse(client)
				logging.error("User tried incorrect username or password; POST!")
				client.close()
				
				
