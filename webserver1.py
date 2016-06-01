import socket
import re

# Standard socket stuff:
host = '' # do we need socket.gethostname() ?
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#change socket behaviour - to be able to reconnect faster
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024) # get the request, 1kB max
    print req
    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
    match = re.match('GET .*?a=(\d+)', req)
    if match:
        a = match.group(1)
        print "a: " + a
    match = re.match('GET .*&b=(\d+)', req)
    if match:
        b = match.group(1)
        print "b: " + b
	sumOfBoth = int(a) + int(b)
	print "a + b = %d" % (sumOfBoth)
        csock.sendall("""HTTP/1.0 200 OK
Content-Type: text/html
<html>
<head>
<title>Success</title>
</head>
<body>
Boo!
</body>
</html>
""")
    else:
        # If there was no recognised command then return a 404 (page not found)
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")

    csock.close()