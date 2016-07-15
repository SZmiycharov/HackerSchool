use IO::Socket::INET;
 
# auto-flush on socket
$| = 1;
 
# creating a listening socket
my $socket = new IO::Socket::INET (
    LocalHost => '',
    LocalPort => '8080',
    Proto => 'tcp',
    Listen => 5,
    Reuse => 1
);
die "cannot create socket $!\n" unless $socket;
print "server waiting for client connection on port 8888\n";
 
while(1)
{
    # waiting for a new client connection
    my $client_socket = $socket->accept();
 
    # get information about a newly connected client
    my $client_address = $client_socket->peerhost();
    my $client_port = $client_socket->peerport();
    print "connection from $client_address:$client_port\n";
 
    # read up to 1024 characters from the connected client
    my $data = "";
    $client_socket->recv($data, 1024);
    print "received data: $data\n";

    @params = split / /, $data;
    print @params[1];
    #/sum?a=5&b=2
    $data = @params[1];
    @params = split /\?/, $data;
 	$data = @params[1];
 	#a=5&b=2
 	@params = split /&/, $data;
 	my $a = @params[0];
 	my $b = @params[1];

 	@params = split /=/, $a;	
 	$a = @params[1];
 	print $a, "\n";

 	@params = split /=/, $b;	
 	$b = @params[1];
 	print $b, "\n";
 	$sum = $a + $b;
 	$data = ("HTTP/1.1 200 OK\nSERVER: Slavi\nContent-Type: text/html<html><body><p>%s</p></body></html>", $sum);

 	$client_socket->send($data);



    # write response data to the connected client
    $data = "ok", "\n";
    $client_socket->send($data);
 
    # notify client that response has been sent
    shutdown($client_socket, 1);
}
 
$socket->close();