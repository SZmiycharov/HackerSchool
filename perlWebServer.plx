use IO::Socket::INET;
 
# auto-flush on socket
$| = 1;
$port = 8080;
$directory = '/home/slavi/Desktop';

# creating a listening socket
my $socket = new IO::Socket::INET (
    LocalHost => '',
    LocalPort => $port,
    Proto => 'tcp',
    Listen => 5,
    Reuse => 1
);
die "cannot create socket $!\n" unless $socket;
print "\t*******************SERVER STARTED*******************\n";

while(1)
{
    my $client_socket = $socket->accept();
    my $client_address = $client_socket->peerhost();
    my $client_port = $client_socket->peerport();
    print "connection from $client_address:$client_port\n";
 
    my $data = "";
    $client_socket->recv($data, 8192);
    print "received data: $data\n";

    @params = split / /, $data;
    $request_method = @params[0];
    print "req method: $request_method\n";

    $secondPartOfRequest = @params[1];
    @command = split /\?/, $secondPartOfRequest;
    $command = @command[0];
    print "command: $command\n";
    if((command ne '/sum') && (command ne '/files'))
    {
        print "command is not sum or files!\n";
        @command = split /\//, $command;
        $command = @command[1];
        print "now command is: $command\n";
    }

    if ($request_method eq 'GET')
    {
        if ($command eq '/sum')
        {
            $data = @params[1];
            @params = split /\?/, $data;
            $data = @params[1];
            #a=5&b=2
            @params = split /&/, $data;
            my $a = @params[0];
            my $b = @params[1];

            @params = split /=/, $a;    
            $a = @params[1];

            @params = split /=/, $b;    
            $b = @params[1];
            $sum = $a + $b;
            print "$sum\n";

            $data = ("HTTP/1.1 200 OK
            SERVER: Slavi
            Content-Type: text/html\n\n<html>
            <body>
            <p><b>SUM: $sum</b></p>
            </body>
            </html>");
            $client_socket->send($data);
        }

        elsif ($command eq '/files')
        {
            @fileName = split /\?/, $secondPartOfRequest;
            $fileName = @fileName[1];
            print "fileName: $fileName\n";
            @fileType = split /\./, $fileName;
            $fileType = @fileType[1];

            if ($fileType eq 'jpg')
            {
                $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: image/jpeg\n\n";
            }
            elsif ($fileType eq 'py')
            {
                $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/plain\n\n";
            }
            elsif ($fileType eq 'txt')
            {
                $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/plain\n\n";
            }
            elsif ($fileType eq 'png')
            {
                $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: image/png\n\n";
            }
            elsif ($fileType eq 'html')
            {
                $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/html\n\n";
            }
            
            $client_socket->send($header);
            $filePath = "$directory/$fileName";
            print "filePath: $filePath";
            open(my $fh, '<:encoding(UTF-8)', $filePath)
                or die "Could not open file '$fileName' $!";
            binmode($fh);

            while(<$fh>)
            {
                $client_socket->send($_);
            }
        }

        elsif ($command eq 'scripts')
        {
            #$secondPartOfRequest = /scripts/getrandom.py
            @script = split /\//, $secondPartOfRequest;
            $script = @script[2];
            print "script: $script\n";
            $result = `python $script`;
            $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/html\n\n";
            $client_socket->send($header);
            $client_socket->send($result);
        }
        
        shutdown($client_socket, 1);
    }
}
 
$socket->close();