use IO::Socket::INET;
use MIME::Base64;
use DBI;

# auto-flush on socket
$| = 1;
$port = 8080;
$directory = '/home/slavi/Desktop';


my $dbh = DBI->connect('dbi:Pg:dbname=httpAuth;host=10.20.1.129','postgres','3111',{AutoCommit=>1,RaiseError=>1,PrintError=>0});

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
 
    my $req = "";
    $client_socket->recv($req, 327680);
    print "received req: $req\n";

    @params = split / /, $req;
    $request_method = @params[0];
    print "req method: $request_method\n";

    $secondPartOfRequest = @params[1];
    @command = split /\?/, $secondPartOfRequest;
    $command = @command[0];

    print "command: $command\n";

    if ($command ne '/sum' && $command ne '/files' && $command ne '/download' && $command ne '/upload')
    {
        #/scripts/test.py
        @command = split /\//, $command;
        $command = @command[1];
        print "now command is: $command\n";
    }


    if ($request_method eq 'GET')
    {
        if ($command eq '/sum')
        {
            print "in GET sum\n";
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

        elsif($command eq '/upload')
        {
            print "in upload GET\n";
            $header = "HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/html\n\n";
            $client_socket->send($header);
            $client_socket->send("<html>
            <body>
            <form action='http://localhost:8080/upload' method='post' enctype='multipart/form-data'>
                Select file to upload:
                <input type='file' name='fileToUpload' id='fileToUpload'>
                <input type='submit' value='Upload Image' name='submit'>
            </form>
            </body>
            </html>");
        }

        elsif ($command eq '/files')
        {
            print "in GET files\n";
            @file = split /\?/, $secondPartOfRequest;
            $file = @file[1];
            @fileName = split /=/, $file;
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
            close $fh;
        }

        elsif ($command eq '/download')
        {
            print "in GET download!\n";
            @file = split /\?/, $secondPartOfRequest;
            $file = @file[1];
            @fileName = split /=/, $file;
            $fileName = @fileName[1];
            print "fileName: $fileName\n";
            @fileType = split /\./, $fileName;
            $fileType = @fileType[1];

            if ($fileType eq 'jpg')
            {
                $header = "HTTP/1.1 200 OK\nServer: SLAVI\nContent-Type: image/jpeg\nContent-Disposition: attachment; filename='file.jpg'\n\n";
            }
            elsif ($fileType eq 'py')
            {
                $header = "HTTP/1.1 200 OK\nServer: SLAVI\nContent-Type: image/jpeg\nContent-Disposition: attachment; filename='file.py'\n\n";
            }
            elsif ($fileType eq 'txt')
            {
                $header = "HTTP/1.1 200 OK\nServer: SLAVI\nContent-Type: image/jpeg\nContent-Disposition: attachment; filename='file.txt'\n\n";
            }
            elsif ($fileType eq 'png')
            {
                $header = "HTTP/1.1 200 OK\nServer: SLAVI\nContent-Type: image/jpeg\nContent-Disposition: attachment; filename='file.png'\n\n";
            }
            elsif ($fileType eq 'html')
            {
                $header = "HTTP/1.1 200 OK\nServer: SLAVI\nContent-Type: image/jpeg\nContent-Disposition: attachment; filename='file.html'\n\n";
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
            close $fh;
        }

        elsif ($command eq 'scripts')
        {
            print "in GET scripts\n";
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

    elsif ($request_method eq 'POST')
    {
        print "**********\n$req*****************\n";
        my @authorization = split /Authorization:/, $req;
        $credentialsCorrect = 0;
        my $authorization = @authorization;
        OUTER: if ($authorization == 2)
        {
            my @encodedCredentials = split /Authorization:/, $req;
            my $encodedCredentials = @encodedCredentials[1];
            @encodedCredentials = split /\r\n/, $encodedCredentials;
            $encodedCredentials = @encodedCredentials[0];
            @encodedCredentials = split / /, $encodedCredentials;
            $encodedCredentials = @encodedCredentials[2];

            $decodedCredentials = decode_base64($encodedCredentials);

            my @username = split /:/, $decodedCredentials;
            $username = @username[0];
            my @password = split /:/, $decodedCredentials;
            $password = @password[1];
            print "username: $username ; password: $password\n";

            if(username eq '' || password eq '')
            {
                $credentialsCorrect = 0;
                last OUTER;
            }
            else
            {
                print "gonna execute query!\n";

                my $stmt = qq(SELECT username FROM users;);
                my $sth = $dbh->prepare( $stmt );
                my $rv = $sth->execute() or die $DBI::errstr;
                if($rv < 0)
                {
                   print $DBI::errstr;
                }
                while(my @row = $sth->fetchrow_array())
                {
                    if ($row[0] eq $username)
                    {
                        print "username correct!\n";
                        my $stmt = qq(SELECT password FROM users;);
                        my $sth = $dbh->prepare( $stmt );
                        my $rv = $sth->execute() or die $DBI::errstr;
                        if($rv < 0)
                        {
                           print $DBI::errstr;
                        }
                        while(my @row = $sth->fetchrow_array())
                        {
                            if($row[0] eq $password)
                            {
                                print "password correct!\n";
                            }
                        }
                    }
                }



                $query = $dbh->prepare("SELECT username FROM users");
                $result = $query->execute();
                print "result from query: $result \n";
            }
        }


        print "req method is POST\n";
        if (0)
        {
            print "in post if\n";
            if ($command eq '/sum')
            {
                print "in sum POST\n";
                @parameters = split / /, $req;
                $parameters = @parameters[-1];
                @parameters = split /\n/, $parameters;
                $parameters = @parameters[-1];
                print "params: $parameters***\n";

                @numbers = split /&/, $parameters;
                $a = @numbers[0];
                @a = split /=/, $a;
                $a = @a[1];
                print "a: $a\n";

                $b = @numbers[1];
                @b = split /=/, $b;
                $b = @b[1];
                print "b: $b\n";
                $sum = $a+$b;

                $data = ("HTTP/1.1 200 OK
                SERVER: Slavi
                Content-Type: text/html\n\n<html>
                <body>
                <p><b>SUM: $sum</b></p>
                </body>
                </html>");
                $client_socket->send($data);
            }

            elsif($command eq 'scripts')
            {
                print "in scripts POST\n";
                @parameters = split / /, $req;
                $parameters = @parameters[-1];
                @parameters = split /\n/, $parameters;
                $parameters = @parameters[-1];
                @script = split /=/, $parameters;
                $script = @script[1];
                print "Script: $script\n";
                
                $result = `python $script`;
                $header = "HTTP/1.1 200 OK
                    SERVER: Slavi
                    Content-Type: text/html\n\n";
                $client_socket->send($header);
                $client_socket->send($result);
            }

            elsif ($command eq '/upload')
            {
                print "in upload POST \n";
                @fileToUpload = split /\r\n\r\n/, $req;
                $fileToUpload = @fileToUpload[2];
                @fileToUpload = split /----/, $fileToUpload;
                $fileToUpload = @fileToUpload[0];
                @fileToUpload = split /\n\r\n/, $fileToUpload;
                $fileToUpload = @fileToUpload[0];
                print "fileToUpload: $fileToUpload\n";

                @contType = split /Content-Type/, $req;
                $contType = @contType[2];
                @contType = split /: /, $contType;
                $contType = @contType[1];
                @contType = split /\n/, $contType;
                $contType = @contType[0];
                @contType = split /\r/, $contType;
                $contType = @contType[0];
                print "contType: $contType\n";

                if($contType eq 'text/plain')
                {
                    $serverfile = "$directory/newfile.txt";
                }
                elsif($contType eq 'text/x-python')
                {
                    $serverfile = "$directory/newfile.py";
                }
                elsif($contType eq 'text/html')
                {
                    $serverfile = "$directory/newfile.html";
                }
                elsif($contType eq 'image/jpeg')
                {
                    $serverfile = "$directory/newfile.jpg";
                }
                elsif($contType eq 'image/png')
                {
                    $serverfile = "$directory/newfile.png";
                }

                open(my $fh, '>', $serverfile) or die "Could not open file '$serverfile': $!\n";
                binmode($fh);
                print $fh $fileToUpload;
                close $fh;

                $header = "HTTP/1.1 200 OK
                    SERVER: Slavi
                    Content-Type: image/jpeg\n\n";

                $client_socket->send($header);
                open(my $fh, '<:encoding(UTF-8)', '/home/slavi/Desktop/success.jpg')
                    or die "Could not open file '$fileName' $!";
                binmode($fh);

                while(<$fh>)
                {
                    $client_socket->send($_);
                }
                close $fh;
            } 
        }

        else
        {
            print "in post else\n";
            $client_socket->send("HTTP/1.1 401 Access Denied
WWW-Authenticate: Basic realm='Authenticate yourself!'
Content-Length: 0\n\n");
        }
    }
}
 
$socket->close();