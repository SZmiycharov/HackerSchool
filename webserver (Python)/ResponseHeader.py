import logging
import webserver1

class ResponseHeader:
	def __init__(self, client = '', returnCode = '200 OK', contenttype = 'text/html', fileExtension = 'txt', http = 'HTTP/1.1'):
		self.client = client
		self.http = http
		self.returnCode = returnCode
		self.contenttype = contenttype
		self.fileExtension = fileExtension

	def SendResponse(self):
		self.client.sendall("""%s %s
Server: SLAVI
Content-Type: %s\n\n"""%(self.http, self.returnCode, self.contenttype))


	def SendFileResponse(self):
		self.client.sendall("""%s %s
Server: SLAVI
Content-Type: %s
Content-Disposition: attachment; filename="file.%s"\n\n"""%(self.http, self.returnCode, self.contenttype, self.fileExtension))

	def SendAuthenticationResponse(self, client):
		client.sendall("""HTTP/1.1 401 Access Denied
WWW-Authenticate: Basic realm='Authenticate yourself!'
Content-Length: 0\n\n""")

	def SendIncorrectUsernameOrPasswordResponse(self, client):
		client.sendall("""
		<html>
		<body>
		<p><b> Incorrect username or password! </b></p>
		</body>
		</html>""")

	def SendCannotUnderstandCommandResponse(self, client):
		client.sendall("""
				<html>
				<body>
				<p><b> Web server cannot understand command! </b></p>
				<p>Should be sum, files or scripts</p>
				</body>
				</html>""")

	def SendBadParametersResponse(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> BAD PARAMETERS! </b></p>
			</body>
			</html>""")

	def SendSumResponse(self, client, sumOfBoth):
		client.sendall("""
			<html>
			<body>
			<p><b> sum: %d </b></p>
			</body>
			</html>""" % (sumOfBoth))

	def SendUploadResponse(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> Upload complete!  </b></p>
			<p> %s files uploaded already! </p
			</body>
			</html>"""%(webserver1.Server.UploadedFiles))

	def SendNoSuchFileResponse(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> NO SUCH FILE! </b></p>
			</body>
			</html>""")

	def SendBadFileType(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> Server cannot handle this file type! </b></p>
			</body>
			</html>""")

	def SendFormForUpload(self, client):
		client.sendall("""<form action="http://localhost:8080/upload" enctype="multipart/form-data" method="post">
<p>Please specify a file, or a set of files:<br>
<input type="file" name="datafile"></p>
<div>
<input type="submit" value="Send">
</div>
</form>""")	

	def SendRegistrationForm(self, client):
		client.sendall("""<form action="http://localhost:8080/regSucceeded" enctype="multipart/form-data" method="post">
<p><b>Sign up</b><br>
Username: <input type="text" name="username"></p>
Password: <input type="password" name="password"></p>
Mail: <input type="text" name="mail"></p>
<div>
<input type="submit" value="Send">
</div>
</form>""")

	def SendSuccessfulSignUp(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> You signed up successfuly!! </b></p>
			</body>
			</html>""")

	def SendUnsuccessfulSignUp(self, client):
		client.sendall("""
			<html>
			<body>
			<p><b> Code was incorrect! You failed! </b></p>
			</body>
			</html>""")

	def SendCodeForm(self, client):
		client.sendall("""<form action="http://localhost:8080/code" enctype="multipart/form-data" method="post">
<p><b>Check your email for code and enter it:</b><br>
Code: <input type="code" name="code"></p>
<div>
<input type="submit" value="Send">
</div>
</form>""")









