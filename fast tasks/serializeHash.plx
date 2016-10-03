use FreezeThaw qw(freeze thaw cmpStr safeFreeze cmpStrHard);
use Data::Dumper;

package MyClass;

sub new {
   my ($class_name) = @_;
   my $new_instance = {};
   bless $new_instance, $class_name;
   return $new_instance;
}

sub set {
   my ($self, $name, $value) = @_;
   $self->{$name} = $value;
}

sub get {
   my ($self, $name) = @_;
   return $self->{$name};
}


package main;

sub serializeHashToFile($$){
    my %hashToSerialize = %{$_[0]};;
    my $fileName = $_[1];
    my $serializedHash = freeze(%hashToSerialize);

    open (my $fh, ">", $fileName) or die "Could not open $fileName";
    print $fh $serializedHash; 
    close $fh;
}

sub deserializeFileTextToHash($){
    my $fileName = $_[0];
    print $fileName . "\n\n";

    open (my $fh, '<' ,$fileName) or die "Could not open $fileName";

    $serializedHash = '';
    while(my $row = <$fh>){
        chomp $row;
        $serializedHash = $serializedHash.$row;
    }
    close $fh;
    my %hash = thaw $serializedHash;
    return %hash;
}


@ARGV[0] or die "You should provide a file path from cmd line!";


my $nestedFile = "/home/slavi/Desktop/testfile.txt";

open (my $fh, "<", $nestedFile) or die "Could not open $nestedFile!";

my %hashToNest = (a => 'asd');
my @arrToNest = qw(a b c d);

my $blessedVar = MyClass->new;
$blessedVar->set('age', 30);

my %grades;
$grades{"a"}{Mathematics}   = [1,2,3,4,5,6];
$grades{"a"}{Literature}    = \%hashToNest;
$grades{"b"}{Literature}   = $nestedFile;
$grades{"b"}{Mathematics}  = \@arrToNest;
$grades{"b"}{Art}          = $blessedVar;

serializeHashToFile(\%grades, '/home/slavi/Desktop/test.txt');
my %deserializedHash = deserializeFileTextToHash('/home/slavi/Desktop/test.txt');

print "beginning hash:\n";
print Dumper(\%grades) . "\n\n";


print "deserializedHash:\n";
print Dumper(\%deserializedHash) . "\n\n";
use Test::Deep;
cmp_deeply(\%grades, \%deserializedHash);



