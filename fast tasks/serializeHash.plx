use strict;
use warnings;
use Storable;
use Data::Compare;
#use JSON;
use Data::Dumper;
use JSON::XS;

my $file = $ARGV[0];
die "No file supplied!" unless $file;

my $filename = '/home/slavi/Desktop/testfile.txt';
open(my $fh, "<", $filename)
	or die "Can't open < $filename: $!";
print "$fh\n\n";

my %helpertable = (
		 fileche => *$fh,
         feet => {
                  biggest  => 'right',
                  smallest => 'left'
                 },
         legs => {
                  biggest  => 'theirs',
                  smallest => 'them',
                  muscular => 'yes'
                 },
         arr => [1,2,3,4]
     );

my %table = (
         feet => {
                  biggest  => %helpertable,
                  smallest => 'left'
                 },
         legs => {
                  biggest  => 'theirs',
                  smallest => 'them',
                  muscular => 'yes'
                 },
         arr => [1,2,3,4]
     );

#$table{'test'} = $FILE1;

foreach my $k (keys %table){
	print "$k: $table{$k}\n";
}
print "\n";


store \%table, $file;
my %hashref = %{retrieve($file)};
foreach my $k (keys %hashref){
	print "$k: $hashref{$k}\n";
}







# print "\n\nDUMPER:\n";
# print Dumper(\%table);
# open(my $fh, ">", $file);
# print $fh, Dumper(\%table);
# close $fh;


# my $json = encode_json \%table;
# print "$json\n";


# store \%table, $file;
# my $hashref = retrieve($file);
# my %hash = %$hashref;
# print "reference: $hashref\n\n";

# foreach my $k (keys %hash){
# 	print "$k: $hash{$k}\n";
# }



# print 'structures of \%table and \%table2 are ',
#        Compare(\%table, \%table) ? "" : "NOT FUCKING ", "identical.\n";




