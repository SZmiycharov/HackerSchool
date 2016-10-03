use FreezeThaw qw(freeze thaw cmpStr safeFreeze cmpStrHard);
use Data::Dumper;
# use 5.010;
# use BSON qw/encode decode/;
use JSON;
use YAML;


#**********************            With FreezeThaw Module             **********************
# sub serializeHashToFile($$){
#     my %hashToSerialize = %{$_[0]};;
#     my $fileName = $_[1];
#     my $serializedHash = freeze(%hashToSerialize);

#     open (my $fh, ">", $fileName) or die "Could not open $fileName";
#     print $fh $serializedHash; 
#     close $fh;
# }

# sub deserializeFileTextToHash($){
#     my $fileName = $_[0];
#     print $fileName . "\n\n";

#     open (my $fh, '<' ,$fileName) or die "Could not open $fileName";

#     $serializedHash = '';
#     while(my $row = <$fh>){
#         chomp $row;
#         $serializedHash = $serializedHash.$row;
#     }
#     close $fh;
#     my %hash = thaw $serializedHash;
#     return %hash;
# }



# **********************            With JSON Module             **********************
# sub serializeHashToFile($$){
#     my %hashToSerialize = %{$_[0]};;
#     my $fileName = $_[1];
#     my $serializedHash = encode_json \%hashToSerialize;
#     open (my $fh, ">", $fileName) or die "Could not open $fileName";
#     print $fh $serializedHash; 
#     close $fh;
# }

# sub deserializeFileTextToHash($){
#     my $fileName = $_[0];
#     print $fileName . "\n\n";

#     open (my $fh, '<' ,$fileName) or die "Could not open $fileName";

#     $serializedHash = '';
#     while(my $row = <$fh>){
#         chomp $row;
#         $serializedHash = $serializedHash.$row;
#     }
#     close $fh;
#     my %hash = decode_json $serializedHash;
#     return %hash;
# }



# **********************            With YAML Module             **********************
sub serializeHashToFile($$){
    my %hashToSerialize = %{$_[0]};;
    my $fileName = $_[1];
    my $serializedHash = Dump(%hashToSerialize);
    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHash($){
    my $fileName = $_[0];
    print $fileName . "\n\n";

    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";
    my $yml = do { local $/; <$fh> };
    my %hash = Load($yml);
    close $fh;
    return %hash;
}

@ARGV[0] or die "You should provide a file path from cmd line!";
my $nestedFile = "/home/slavi/Desktop/testfile.txt";
open (my $fh, "<", $nestedFile) or die "Could not open $nestedFile!";
my %hashToNest = (a => 'asd');
my @arrToNest = qw(a b c d);
my $helperNum = 10;
my $blessedVar = bless \$helperNum;
my %beginning_hash;

$beginning_hash{"a"}{Mathematics}   = [1,2,3,4,5,6, [1,2,3]];
$beginning_hash{"a"}{Literature}    = \%hashToNest;
$beginning_hash{"b"}{Literature}   = $fh;
$beginning_hash{"b"}{Mathematics}  = \@arrToNest;
$beginning_hash{"b"}{Art}          = $blessedVar;

serializeHashToFile(\%beginning_hash, '/home/slavi/Desktop/test.yml');
my %deserializedHash = deserializeFileTextToHash('/home/slavi/Desktop/test.yml');

print "beginning hash:\n";
print Dumper(\%beginning_hash) . "\n\n";


print "deserializedHash:\n";
print Dumper(\%deserializedHash) . "\n\n";

use Test::Deep;
cmp_deeply(\%beginning_hash, \%deserializedHash);



