class Request:
	def __init__(self, client, returnCode = '200 OK', contenttype = 'text/html', fileExtension = '', http = 'HTTP/1.1'):
		self.client = client
		self.http = http
		self.returnCode = returnCode
		self.contenttype = contenttype
		self.fileExtension = fileExtension

	def SendRequest(self):
		self.client.sendall("""%s %s
Server: SLAVI
Content-Type: %s\n"""%(self.http, self.returnCode, self.contenttype))

	def SendFileRequest():
		client.sendall("""%s %s
Server: SLAVI
Content-Type: %s
Content-Disposition: attachment; filename="file.%s"\n"""%(self.http, self.returnCode, self.contenttype, self.fileExtension))



