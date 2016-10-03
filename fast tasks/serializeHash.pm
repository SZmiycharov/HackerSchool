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
    my %hashToSerialize = %{$_[0]};
    my $fileName = $_[1];
    my $serializedHash = freeze(%hashToSerialize);

    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHashFreezeThaw($){
    my $fileName = $_[0];
    print $fileName . "\n\n";

    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";

    my $serializedHash = '';
    while(my $row = <$fh>){
        chomp $row;
        $serializedHash = $serializedHash.$row;
    }
    close $fh;
    my %hash = thaw $serializedHash;
    return %hash;
}



# **********************            With JSON Module             **********************
sub serializeHashToFileJSON($$){
    my %hashToSerialize = %{$_[0]};;
    my $fileName = $_[1];
    my $serializedHash = encode_json \%hashToSerialize;
    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHashJSON($){
    my $fileName = $_[0];
    print $fileName . "\n\n";

    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";

    my $serializedHash = '';
    while(my $row = <$fh>){
        chomp $row;
        $serializedHash = $serializedHash.$row;
    }
    close $fh;
    my %hash = decode_json $serializedHash;
    return %hash;
}



# **********************            With YAML Module             **********************
sub serializeHashToFileYAML($$){
    my %hashToSerialize = %{$_[0]};;
    my $fileName = $_[1];
    my $serializedHash = Dump(%hashToSerialize);
    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHashYAML($){
    my $fileName = $_[0];
    print $fileName . "\n\n";

    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";
    my $yml = do { local $/; <$fh> };
    my %hash = Load($yml);
    close $fh;
    return %hash;
}



# **********************            With BSON Module             **********************
sub serializeHashToFileBSON($$){
    my %hashToSerialize = %{$_[0]};;
    my $fileName = $_[1];
    my $serializedHash = encode(\%hashToSerialize);
    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHashBSON($){
    my $fileName = $_[0];
    print $fileName . "\n\n";
    my $serializedHash = '';
    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";
    while(my $row = <$fh>){
        chomp ($row);
        $serializedHash = $serializedHash.$row;
    }

    my %hash = decode($serializedHash);
    close $fh;
    return %hash;
}






