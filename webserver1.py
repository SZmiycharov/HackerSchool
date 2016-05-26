import socket
from urlparse import parse_qs, urlparse

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    querystrings = parse_qs(urlparse("http://localhost:8888/hello?a=5&b=6").query,
         keep_blank_values=True)
    querystr1 = querystrings['a']
    querystr1 = map(int, querystr1)
    querystr2 = querystrings['b']
    querystr2 = map(int, querystr2)
    http_response = querystr1[0] + querystr2[0]
    print(http_response)
    result = str(http_response)
    client_connection.sendall(result)
    client_connection.close()