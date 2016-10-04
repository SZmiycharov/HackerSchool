use warnings;
use strict;
use FreezeThaw qw(freeze thaw cmpStr safeFreeze cmpStrHard);
use Data::Dumper;
use JSON;
use YAML;
use BSON qw/encode decode/;


my $document = {
    _id      => BSON::ObjectId->new,
    date     => BSON::Time->new,
    name     => 'James Bond',
    age      => 45,
    amount   => 24587.45,
    badass   => BSON::Bool->true,
    password => BSON::String->new('12345')
};


#**********************            With FreezeThaw Module             **********************
sub serializeHashToFileFreezeThaw($$){
    my ($hash_to_serialize, $file_name) = @_;
    my $serialized_hash = freeze(%$hash_to_serialize);

    open (my $fh, ">", $file_name) or die "Could not open $file_name";
    print $fh $serialized_hash; 
    close $fh;
}

sub deserializeFileTextToHashFreezeThaw($){
    my ($file_name) = @_;

    open (my $fh, '<' ,$file_name) or die "Could not open $file_name";

    my $serialized_hash = '';
    while(my $row = <$fh>){
        chomp $row;
        $serialized_hash = $serialized_hash.$row;
    }
    close $fh;
    my %hash = thaw $serialized_hash;

    return %hash;
}



# **********************            With JSON Module             **********************
sub serializeHashToFileJSON($$){
    my ($hash_to_serialize, $file_name) = @_;
    my $serialized_hash = encode_json $hash_to_serialize;
    open (my $fh, ">", $file_name) or die "Could not open $file_name";
    print $fh $serialized_hash; 
    close $fh;
}

sub deserializeFileTextToHashJSON($){
    my ($file_name) = @_;
    open (my $fh, '<' ,$file_name) or die "Could not open $file_name";

    my $serialized_hash = '';
    while(my $row = <$fh>){
        chomp $row;
        $serialized_hash = $serialized_hash.$row;
    }
    close $fh;
    my $hash = decode_json $serialized_hash;

    return %$hash;
}



# **********************            With YAML Module             **********************
sub serializeHashToFileYAML($$){
    my %hash_to_serialize = %{$_[0]};
    my $file_name = $_[1];
    my $serialized_hash = Dump(%hash_to_serialize);
    open (my $fh, ">", $file_name) or die "Could not open $file_name";
    print $fh $serialized_hash; 
    close $fh;
}

sub deserializeFileTextToHashYAML($){
    my ($file_name) = @_;

    open (my $fh, '<' ,$file_name) or die "Could not open $file_name";
    my $yml = do { local $/; <$fh> };
    my %hash = Load($yml);
    close $fh;

    return %hash;
}



# **********************            With BSON Module             **********************
sub serializeHashToFileBSON($$){
    my ($hash_to_serialize, $file_name) = @_;

    my $serialized_hash = encode($hash_to_serialize);
    open (my $fh, ">", $file_name) or die "Could not open $file_name";
    print $fh $serialized_hash; 
    close $fh;
}

sub deserializeFileTextToHashBSON($){
    my ($file_name) = @_;
    my $serialized_hash = '';

    open (my $fh, '<' ,$file_name) or die "Could not open $file_name";
    while(my $row = <$fh>){
        chomp ($row);
        $serialized_hash = $serialized_hash.$row;
    }

    my $hash = decode($serialized_hash);
    close $fh;

    return %$hash;
}


sub summarizeResults($$){
    my ($beginning_hash, $deserialized_hash) = @_;
    print "beginning hash:\n";
    print Dumper($beginning_hash) . "\n\n";

    print "deserialized_hash:\n";
    print Dumper($deserialized_hash) . "\n\n";

    use Test::Deep;
    cmp_deeply($beginning_hash, $deserialized_hash);
}


# **********************            Test Functions             **********************
sub testFreezeThaw($){
    my ($beginning_hash) = @_;
    serializeHashToFileFreezeThaw($beginning_hash, '/home/slavi/Desktop/test.txt');
    my %deserialized_hash = deserializeFileTextToHashFreezeThaw('/home/slavi/Desktop/test.txt');

    summarizeResults($beginning_hash, \%deserialized_hash);
}

sub testJSON($){
    my ($beginning_hash) = @_;
    serializeHashToFileJSON($beginning_hash, '/home/slavi/Desktop/test.txt');
    my %deserialized_hash = deserializeFileTextToHashJSON('/home/slavi/Desktop/test.txt');

    summarizeResults($beginning_hash, \%deserialized_hash);
}

sub testYAML($){
    my ($beginning_hash) = @_;
    serializeHashToFileYAML($beginning_hash, '/home/slavi/Desktop/test.yml');
    my %deserialized_hash = deserializeFileTextToHashYAML('/home/slavi/Desktop/test.yml');

    summarizeResults($beginning_hash, \%deserialized_hash);  
}

sub testBSON($){
    my ($beginning_hash) = @_;
    serializeHashToFileBSON($beginning_hash, '/home/slavi/Desktop/test.txt');
    my %deserialized_hash = deserializeFileTextToHashBSON('/home/slavi/Desktop/test.txt');

    summarizeResults($beginning_hash, \%deserialized_hash);
}






