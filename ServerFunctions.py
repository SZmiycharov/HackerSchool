import Response
import re

class ServerFunctions:
	def __init__(self, client = '', fileName = '', directory = ''):
		print "init of ServerFunctions"
		self.client = client
		self.fileName = fileName
		self.directory = directory

	def RetrFile(self, toDownload=True):
			print "RetrFile of ServerFunctions"
			try:		
				filePath = self.directory + '/' + self.fileName
				f = open(filePath, 'rb')
			except IOError:
				errorMsg = "File could not be found!"
				Response.Response(self.client, '400 Bad Request').SendResponse()
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
					Response.Response(self.client, '200 OK', 'text/plain', 'py').SendFileResponse()
				elif(fileType == 'txt'):
					Response.Response(self.client, '200 OK', 'text/plain', 'txt').SendFileResponse()
				elif(fileType == "html"):
					Response.Response(self.client, '200 OK', 'text/html', 'html').SendFileResponse()
				elif(fileType == "php"):
					Response.Response(self.client, '200 OK', 'text/html', 'php').SendFileResponse()
				elif(fileType == 'png'):
					Response.Response(self.client, '200 OK', 'image/png', 'png').SendFileResponse()
				elif(fileType == 'jpg'):
					Response.Response(self.client, '200 OK', 'image/jpeg', 'jpg').SendFileResponse()
				while True:
					fileData = self.f.read()
					if fileData == '': break
					client.sendall(fileData)
				f.close()  
			else:
				if(fileType == 'py'):
					Response.Response(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == 'txt'):
					Response.Response(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == "html"):
					Response.Response(self.client, '200 OK', 'text/html').SendResponse()
				elif(fileType == "php"):
					Response.Response(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == 'png'):
					Response.Response(self.client, '200 OK', 'image/png').SendResponse()
				elif(fileType == 'jpg'):
					Response.Response(self.client, '200 OK', 'image/jpeg').SendResponse()
				
				while True:
					fileData = f.read()
					if fileData == '': break
					self.client.sendall(fileData)
				f.close()

	def uploadFile(self, fileextension, fileToUpload, directory):
		print "uploadfile of ServerFunctions"
		serverFile = directory + '/newfile.' + fileextension
		print serverFile
		f = open(serverFile, 'wb+')
		f.write(fileToUpload)
		f.close()
