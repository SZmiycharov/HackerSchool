use strict;
use warnings;
use IO::Socket::INET;
use MIME::Base64;
use DBI;
use threads;
use Scalar::Util qw(looks_like_number);
use Digest::MD5 qw(md5 md5_hex md5_base64);


my $port = 8080;
my $directory = '/home/slavi/Desktop';
$| = 1;
my $portFromCMD = $ARGV[0];
my $dirFromCMD = $ARGV[1];
my $sendingCredentials = 0;

if (looks_like_number($portFromCMD) && $portFromCMD>0 && $portFromCMD<60000)
{
    print "yey took port from CMD!\n";
    $port = $portFromCMD;
    print "port: $port\n";
}
if (-d $dirFromCMD)
{
    print "yeyy dir is correct!!\n";
    $directory = $dirFromCMD;
    print "dir: $directory\n";
}

my $dbh = DBI->connect('dbi:Pg:dbname=httpAuth;host=10.20.1.129','postgres','3111',{AutoCommit=>1,RaiseError=>1,PrintError=>0});
die "cannot connect to database: $!\n" unless $dbh;

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
    die "cannot create socket $!\n" unless $client_socket;
    my $client_address = $client_socket->peerhost();
    my $client_port = $client_socket->peerport();
    print "connection from $client_address:$client_port\n";
    

    my $req = "";
    my $buffer = "";
    while(index($req,"\r\n\r\n") == -1)
    {
        $client_socket->recv($req, 1024);
        print "currentReq: $req\n";
    }
    
    print "*************\n$req\n*************\n";

    my @params = split / /, $req;
    my $request_method = $params[0];
    print "req method: $request_method\n";

    if ($params[1] eq '')
    {
        my $data = ("HTTP/1.1 404 Not Found
                    SERVER: Slavi
                    Content-Type: text/html\n\n<html>
                    <body>
                    <p><b>Bad request!</b></p>
                    </body>
                    </html>");
        $client_socket->send($data);
    }

    my $secondPartOfRequest = $params[1];
    my @command = split /\?/, $secondPartOfRequest;
    my $command = $command[0];

    if ($command ne '/sum' && $command ne '/files' && $command ne '/download' && $command ne '/upload')
    {
        #/scripts/test.py
        @command = split /\//, $command;
        $command = $command[1];
        print "now command is: $command\n";
    }


    if ($request_method eq 'GET')
    {
        if ($command eq '/sum')
        {
            print "in GET sum\n";
            my $data = $params[1];
            my @params = split /\?/, $data;
            $data = $params[1];
            @params = split /&/, $data;
            my $a = $params[0];
            my $b = $params[1];

            @params = split /=/, $a;    
            $a = $params[1];

            @params = split /=/, $b;    
            $b = $params[1];
            
            if (looks_like_number($a) & looks_like_number($b))
                {
                    my $sum = $a+$b;
                    my $data;
                    $data = ("HTTP/1.1 200 OK
                    SERVER: Slavi
                    Content-Type: text/html\n\n<html>
                    <body>
                    <p><b>SUM: $sum</b></p>
                    </body>
                    </html>");
                    $client_socket->send($data);
                }
            else 
            {
                my $data = "HTTP/1.1 404 Not Found
                SERVER: Slavi
                    Content-Type: text/html\n\n<html>
                    <body>
                    <p><b>Bad parameters!</b></p>
                    </body>
                    </html>";
                $client_socket->send($data);
            }
            
        }

        elsif($command eq '/upload')
        {
            print "in upload GET\n";
            my $header = "HTTP/1.1 200 OK
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
            my @file = split /\?/, $secondPartOfRequest;
            my $file = $file[1];
            my @fileName = split /=/, $file;
            my $fileName = $fileName[1];
            print "fileName: $fileName\n";
            my @fileType = split /\./, $fileName;
            my $fileType = $fileType[1];

            my $filePath = "$directory/$fileName";

            my $header;
            if (-f $filePath)
            {
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
                open(my $fh, '<:encoding(UTF-8)', $filePath)
                    or die "Could not open file '$fileName' $!";
                binmode($fh);

                while(<$fh>)
                {
                    $client_socket->send($_);
                }
                close $fh;
            }
            else
            {
                my $data = "HTTP/1.1 404 Not Found
                    SERVER: Slavi
                        Content-Type: text/html\n\n<html>
                        <body>
                        <p><b>No such file!</b></p>
                        </body>
                        </html>";
                $client_socket->send($data);
            }
        }

        elsif ($command eq '/download')
        {
            print "in GET download!\n";
            my @file = split /\?/, $secondPartOfRequest;
            my $file = $file[1];
            my @fileName = split /=/, $file;
            my $fileName = $fileName[1];
            print "fileName: $fileName\n";
            my @fileType = split /\./, $fileName;
            my $fileType = $fileType[1];
            my $header;
            my $filePath = "$directory/$fileName";

            if (-f $filePath)
            {
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
            else
            {
                my $data = "HTTP/1.1 404 Not Found
                    SERVER: Slavi
                        Content-Type: text/html\n\n<html>
                        <body>
                        <p><b>No such file!</b></p>
                        </body>
                        </html>";
                $client_socket->send($data);
            }            
        }

        elsif ($command eq 'scripts')
        {
            print "in GET scripts\n";
            my @script = split /\//, $secondPartOfRequest;
            my $script = $script[2];
            print "script: $script\n";
            if(-e $script)
            {
                my $result = `python $script`;
                my $header = "HTTP/1.1 200 OK
                    SERVER: Slavi
                    Content-Type: text/html\n\n";
                $client_socket->send($header);
                $client_socket->send($result);
            }
            else
            {
                my $data = ("HTTP/1.1 404 Not Found
                    SERVER: Slavi
                    Content-Type: text/html\n\n<html>
                    <body>
                    <p><b>No such file!</b></p>
                    </body>
                    </html>");
                $client_socket->send($data);
            }
            
        }

        else
        {
            my $header = "HTTP/1.1 404 Not Found\nSERVER: Slavi\nContent-type: text/html\n\n";
            $client_socket->send($header);
            my $body = "<html>
            <body>
            <p><b>Server does not support this command!</b></p>
            </body>
            </html>";
            $client_socket->send($body);
        }

        shutdown($client_socket, 1);
    }

    elsif ($request_method eq 'POST')
    {
        print "req method is POST\n";
        my @string = split / /, $req;
        my $string = $string[1];
        @string = split /\//, $string;
        $string = $string[1];

        if ($string eq 'regSucceeded')
        {
            print "in reqSucceeded!\n";
            my @user = split /"username"/,$req;
            my $user = $user[1];
            @user = split /---/,$user;
            $user = $user[0];
            @user = split /\n/, $user;
            $user = $user[2];
            @user = split /\r/, $user;
            $user = $user[0];
            print "user: $user\n";

            my @passw = split /"password"/,$req;
            my $passw = $passw[1];
            @passw = split /---/,$passw;
            $passw = $passw[0];
            @passw = split /\n/, $passw;
            $passw = $passw[2];
            @passw = split /\r/, $passw;
            $passw = $passw[0];
            print "passw: $passw\n";

            my @mail = split /"mail"/,$req;
            my $mail = $mail[1];
            @mail = split /---/,$mail;
            $mail = $mail[0];
            @mail = split /\n/, $mail;
            $mail = $mail[2];
            @mail = split /\r/, $mail;
            $mail = $mail[0];
            print "mail: $mail\n";

            my $hashedPassw = md5_hex($passw);
            print "hashedPassw: $hashedPassw\n";

            my $sth = $dbh->prepare( "INSERT INTO users(username, password, mail) VALUES('$user', '$hashedPassw', '$mail')" );
            my $rv = $sth->execute() or die $DBI::errstr;
            if($rv < 0)
            {
               print $DBI::errstr;
            }
            my $data = "HTTP/1.1 200 OK
            SERVER: Slavi
            Content-Type: text/html\n\n<html>
            <body>
            <p>Registration successful!</p></body</html>";
            $client_socket->send($data);
        }
        else
        {
            my @authorization = split /Authorization:/, $req;
        
            my $authorization = @authorization;
            my $credentialsCorrect = 0;
            if ($authorization == 2)
            {
                print "received credentials\n";
                my @encodedCredentials = split /Authorization:/, $req;
                my $encodedCredentials = $encodedCredentials[1];
                @encodedCredentials = split /\r\n/, $encodedCredentials;
                $encodedCredentials = $encodedCredentials[0];
                @encodedCredentials = split / /, $encodedCredentials;
                $encodedCredentials = $encodedCredentials[2];

                my $decodedCredentials = decode_base64($encodedCredentials);

                my @username = split /:/, $decodedCredentials;
                my $username = $username[0];
                my @password = split /:/, $decodedCredentials;
                my $password = $password[1];
                print "username: $username ; password: $password\n";

                if($username eq '' || $password eq '')
                {
                    $credentialsCorrect = 0;
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
                    OUTER: while(my @row = $sth->fetchrow_array())
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
                                if($row[0] eq md5_hex($password))
                                {
                                    print "password correct!\n";
                                    $credentialsCorrect = 1;
                                    last OUTER;
                                    print "we should not be here!\n\n\n";
                                }
                                else
                                {
                                    print "not correct password!\n";
                                }
                            }
                        }
                        else
                        {
                            print "not correct username!\n";
                        }
                    }
                }
            }

            if ($credentialsCorrect)
            {
                $sendingCredentials = 0;
                print "in post if\n";
                if ($command eq '/sum')
                {
                    my @parameters;
                    my $parameters;
                    print "in sum POST\n";
                    @parameters = split / /, $req;
                    $parameters = $parameters[-1];
                    @parameters = split /\n/, $parameters;
                    $parameters = $parameters[-1];
                    print "params: $parameters***\n";

                    my @numbers;
                    @numbers = split /&/, $parameters;
                    my $a;
                    my @a;
                    $a = $numbers[0];
                    @a = split /=/, $a;
                    $a = $a[1];
                    print "a: $a\n";
                    my $b;
                    my @b;
                    $b = $numbers[1];
                    @b = split /=/, $b;
                    $b = $b[1];
                    print "b: $b\n";
                    my $sum;
                    if (looks_like_number($a) & looks_like_number($b))
                    {
                        $sum = $a+$b;
                        my $data;
                        $data = ("HTTP/1.1 200 OK
                        SERVER: Slavi
                        Content-Type: text/html\n\n<html>
                        <body>
                        <p><b>SUM: $sum</b></p>
                        </body>
                        </html>");
                        $client_socket->send($data);
                    }
                    else 
                    {
                        my $data = "HTTP/1.1 404 Not Found
                        SERVER: Slavi
                            Content-Type: text/html\n\n<html>
                            <body>
                            <p><b>Bad parameters!</b></p>
                            </body>
                            </html>";
                        $client_socket->send($data);
                    }
                        
                }

                elsif($command eq 'scripts')
                {
                    print "in scripts POST\n";
                    my @parameters;
                    my $parameters;
                    @parameters = split / /, $req;
                    $parameters = $parameters[-1];
                    @parameters = split /\n/, $parameters;
                    $parameters = $parameters[-1];

                    my @script;
                    my $script;
                    @script = split /=/, $parameters;
                    $script = $script[1];
                    print "Script: $script\n";
                    if(-e $script)
                    {
                        my $result = `python $script`;
                        my $header = "HTTP/1.1 200 OK
                            SERVER: Slavi
                            Content-Type: text/html\n\n";
                        $client_socket->send($header);
                        $client_socket->send($result);
                    }
                    else
                    {
                        my $data = ("HTTP/1.1 404 Not Found
                        SERVER: Slavi
                        Content-Type: text/html\n\n<html>
                        <body>
                        <p><b>No such file!</b></p>
                        </body>
                        </html>");
                        $client_socket->send($data);
                    }
                    
                }

                elsif ($command eq '/upload')
                {
                    print "in upload POST \n";
                    my @fileToUpload;
                    my $fileToUpload;
                    @fileToUpload = split /\r\n\r\n/, $req;
                    $fileToUpload = $fileToUpload[2];
                    @fileToUpload = split /----/, $fileToUpload;
                    $fileToUpload = $fileToUpload[0];
                    @fileToUpload = split /\n\r\n/, $fileToUpload;
                    $fileToUpload = $fileToUpload[0];
                    print "fileToUpload: $fileToUpload\n";

                    my @contType;
                    my $contType;
                    @contType = split /Content-Type/, $req;
                    $contType = $contType[2];
                    @contType = split /: /, $contType;
                    $contType = $contType[1];
                    @contType = split /\n/, $contType;
                    $contType = $contType[0];
                    @contType = split /\r/, $contType;
                    $contType = $contType[0];
                    print "contType: $contType\n";

                    my $serverfile;
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

                    open(my $fh, '>', $serverfile);
                    binmode($fh);
                    print $fh $fileToUpload;
                    close $fh;

                    my $header = "HTTP/1.1 200 OK
                        SERVER: Slavi
                        Content-Type: image/jpeg\n\n";

                    $client_socket->send($header);
                    open(my $fh2, '<:encoding(UTF-8)', '/home/slavi/Desktop/success.jpg')
                        or die "Could not open file: $!";
                    binmode($fh2);

                    while(<$fh2>)
                    {
                        $client_socket->send($_);
                    }
                    close $fh2;
                } 

                else
                {
                    my $header = "HTTP/1.1 404 Not Found\nSERVER: Slavi\nContent-type: text/html\n\n";
                    $client_socket->send($header);
                    my $body = "<html>
                    <body>
                    <p><b>Server does not support this command!</b></p>
                    </body>
                    </html>";
                    $client_socket->send($body);
                }
            }

            else
            {
                print "credentials not correct!\n";
                print "sendingCredentials: $credentialsCorrect\n";
                if ($sendingCredentials == 0)
                {
                    $sendingCredentials += 1;
                    $client_socket->send("HTTP/1.1 401 Access Denied\nWWW-Authenticate: Basic realm='Authenticate yourself!'\nContent-Length: 0\n\n");
                    shutdown($client_socket, 1);
                }
                else
                {
                    print "sending registration form!\n";
                    $sendingCredentials = 0;
                    $client_socket->send("HTTP/1.1 200 OK\nSERVER: Slavi\nContent-Type: text/html\n\n");
                    $client_socket->send("<form action='http://localhost:8080/regSucceeded' enctype='multipart/form-data' method='post'>
                        <p><b>Sign up</b><br>
                        Username: <input type='text' name='username'></p>
                        Password: <input type='password' name='password'></p>
                        Mail: <input type='text' name='mail'></p>
                        <div>
                        <input type='submit' value='Send'>
                        </div>
                        </form>");
                }
            }
        }

          
    }

    else 
    {
        my $data = ("HTTP/1.1 404 Not Found
                    SERVER: Slavi
                    Content-Type: text/html\n\n<html>
                    <body>
                    <p><b>Server does not support such request method (only POST and GET supported!)</b></p>
                    </body>
                    </html>");
        $client_socket->send($data);
    }
}

$socket->close();