use FreezeThaw qw(freeze thaw cmpStr safeFreeze cmpStrHard);
use Data::Dumper;

my $filename = '/home/slavi/Desktop/testfile.txt';
open (my $fh, "<", $filename);

my %testhash = (a => 'asd');
my @testarr = qw(a b c d);

my %grades;
$grades{"asd"}{Mathematics}   = [1,2,3,4,5,6];
$grades{"asd"}{Literature}    = \%testhash;
$grades{"haha"}{Literature}   = $filename;
$grades{"haha"}{Mathematics}  = \@testarr;
$grades{"haha"}{Art}          = 99;

print "$grades{haha}{Literature}\n";
print Dumper(\%grades) . "\n\n";

my $string = freeze( %grades );
print $string . "\n\n";

my %grades2 = thaw $string;
print Dumper(\%grades2) . "\n\n";

