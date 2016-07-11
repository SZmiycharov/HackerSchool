import Request
import re

class ServerFunctions:
	def __init__(self, client = '', fileName = '', directory = ''):
		print "init of ServerFunctions"
		self.client = client
		self.fileName = fileName
		self.directory = directory
	def test(self):
		print "yolo"

	def RetrFile(self, toDownload=True):
			print "RetrFile of ServerFunctions"
			try:		
				filePath = self.directory + '/' + self.fileName
				f = open(filePath, 'rb')
			except IOError:
				errorMsg = "File could not be found!"
				Request.Request(self.client, '400 Bad Request').SendRequest()
				self.client.sendall("""
					<html>
					<body>
					<p><b> %s </b></p>
					</body>
					</html>""" % (errorMsg))
				logging.error("File %s could not be found!"%(self.fileName))
				self.client.close()
				return
			match = re.match('.*\.(.*)', self.fileName)
			fileType = match.group(1)
			print fileType
			if toDownload:
				if(fileType == 'py'):
					Request.Request(self.client, '200 OK', 'text/plain', 'py').SendFileRequest()
				elif(fileType == 'txt'):
					Request.Request(self.client, '200 OK', 'text/plain', 'txt').SendFileRequest()
				elif(fileType == "html"):
					Request.Request(self.client, '200 OK', 'text/html', 'html').SendFileRequest()
				elif(fileType == "php"):
					Request.Request(self.client, '200 OK', 'text/html', 'php').SendFileRequest()
				elif(fileType == 'png'):
					Request.Request(self.client, '200 OK', 'image/png', 'png').SendFileRequest()
				elif(fileType == 'jpg'):
					Request.Request(self.client, '200 OK', 'image/jpeg', 'jpg').SendFileRequest()
				while True:
					fileData = self.f.read()
					if fileData == '': break
					client.sendall(fileData)
				f.close()  
			else:
				if(fileType == 'py'):
					Request.Request(self.client, '200 OK', 'text/plain').SendRequest()
				elif(fileType == 'txt'):
					Request.Request(self.client, '200 OK', 'text/plain').SendRequest()
				elif(fileType == "html"):
					Request.Request(self.client, '200 OK', 'text/html').SendRequest()
				elif(fileType == "php"):
					Request.Request(self.client, '200 OK', 'text/plain').SendRequest()
				elif(fileType == 'png'):
					Request.Request(self.client, '200 OK', 'image/png').SendRequest()
				elif(fileType == 'jpg'):
					Request.Request(self.client, '200 OK', 'image/jpeg').SendRequest()
				
				while True:
					fileData = f.read()
					if fileData == '': break
					self.client.sendall(fileData)
				f.close()