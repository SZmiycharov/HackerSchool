import ResponseHeader
import re
import logging

class ServerFunctions:
	def __init__(self, client = '', fileName = '', directory = ''):
		self.client = client
		self.fileName = fileName
		self.directory = directory

	def RetrFile(self, toDownload=True):
			print "RetrFile of ServerFunctions"
			try:		
				filePath = self.directory + '/' + self.fileName
				print "filePath: %s" %(filePath)
				f = open(filePath, 'rb')
			except IOError:
				errorMsg = "File could not be found!"
				ResponseHeader.ResponseHeader(self.client, '400 Bad Request').SendResponse()
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
			if toDownload:
				if(fileType == 'py'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/plain', 'py').SendFileResponse()
				elif(fileType == 'txt'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/plain', 'txt').SendFileResponse()
				elif(fileType == "html"):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/html', 'html').SendFileResponse()
				elif(fileType == "php"):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/html', 'php').SendFileResponse()
				elif(fileType == 'png'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'image/png', 'png').SendFileResponse()
				elif(fileType == 'jpg'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'image/jpeg', 'jpg').SendFileResponse()
				while True:
					fileData = f.read()
					if fileData == '': break
					self.client.sendall(fileData)
				f.close()  
			else:
				if(fileType == 'py'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == 'txt'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == "html"):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/html').SendResponse()
				elif(fileType == "php"):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'text/plain').SendResponse()
				elif(fileType == 'png'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'image/png').SendResponse()
				elif(fileType == 'jpg'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'image/jpeg').SendResponse()
				elif(fileType == 'gif'):
					ResponseHeader.ResponseHeader(self.client, '200 OK', 'image/gif').SendResponse()

				while True:
					fileData = f.read()
					if fileData == '': break
					self.client.sendall(fileData)
				f.close()

	def uploadFile(self, fileextension, fileToUpload, directory):
		print "uploadfile of ServerFunctions"
		serverFile = directory + '/newfile.' + fileextension
		print "serverFile: %s"%(serverFile)
		f = open(serverFile, 'wb+')
		f.write(fileToUpload)
		f.close()
