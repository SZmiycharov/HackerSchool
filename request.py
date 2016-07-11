class Request:
	def __init__(self, client, returnCode = '200 OK', contenttype = 'text/html', fileExtension = 'txt', http = 'HTTP/1.1'):
		self.client = client
		self.http = http
		self.returnCode = returnCode
		self.contenttype = contenttype
		self.fileExtension = fileExtension

	def SendRequest(self):
		print "SUPER"
		self.client.sendall("""%s %s
Server: SLAVI
Content-Type: %s\n\n"""%(self.http, self.returnCode, self.contenttype))

	def SendFileRequest(self):
		print "YEYYYY"
		print("""%s %s
Server: SLAVI
Content-Type: %s
Content-Disposition: attachment; filename='file.%s'\n"""%(self.http, self.returnCode, self.contenttype, self.fileExtension))
		self.client.sendall("""%s %s
Server: SLAVI
Content-Type: %s
Content-Disposition: attachment; filename="file.%s"\n
"""%(self.http, self.returnCode, self.contenttype, self.fileExtension))





