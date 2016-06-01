import socket
import re

host = '' 
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#change socket behaviour - to be able to reconnect faster
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
#don't queue requests - listen for only 1
sock.listen(1) 

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024) # get the request, 1kB max
    print req
    # address should be sth like GET /move?a=20&b=3 HTTP/1.1

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
	print "\n"
        csock.sendall("""HTTP/1.1 200 OK
Content-Type: text/html
<html>
<head>
<title>Success</title>
</head>
<body>
YEY!
</body>
</html>
""")
    else:
        # If there was no recognised command then return a 404 (page not found)
        print "Returning 404"
        csock.sendall("HTTP/1.1 404 Not Found\r\n")

    csock.close()