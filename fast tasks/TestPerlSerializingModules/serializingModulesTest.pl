use warnings;
use strict;
use lib '/home/slavi/Desktop/HackerSchool/fast\ tasks';
use serializeHash;
use Try::Tiny;
use Time::HiRes qw/ time /;

$ARGV[0] or die "You should provide a file path from cmd line!";
my $nested_file = "/home/slavi/Desktop/testfile.txt";
open (my $fh, "<", $nested_file) or die "Could not open $nested_file!";
my %hash_to_nest = (a => 'asd');
my @arr_to_nest = qw(a b c d);
my $helper_num = {a=>'asd'};
my $blessed_var = bless \$helper_num;
$blessed_var = JSON::true;
my %beginning_hash;

$beginning_hash{"a"}{Mathematics}   = [1,2,3,4,5,6, [1,2,3]];
$beginning_hash{"a"}{Literature}    = \%hash_to_nest;
$beginning_hash{"b"}{Literature}   = $fh;
$beginning_hash{"b"}{Mathematics}  = \@arr_to_nest;
$beginning_hash{"b"}{Art}          = $blessed_var;

# %beginning_hash = (
#     "apple"  => "red",
#     "orange" => "orange",
#     "grape"  => "purple",
# );

print "\n*****************************FreezeThawTest*****************************\n";
my $start_time = time;
try{
	testFreezeThaw(\%beginning_hash);
} catch{
	print "caught error: $_\n";
};
my $end_time = time;
my $elapsed_time = $end_time - $start_time;
print "Elapsed time: ".$elapsed_time." ms\n\n";


print "\n*****************************JSONTest*****************************\n";
$start_time = time;
try{
	testJSON(\%beginning_hash);
} catch{
	print "caught error: $_\n";
};
$end_time = time;
$elapsed_time = $end_time - $start_time;
print "Elapsed time: ".$elapsed_time." ms\n\n";


print "\n*****************************YAMLTest*****************************\n";
$start_time = time;
try{
	testYAML(\%beginning_hash);
} catch{
	print "caught error: $_\n";
};
$end_time = time;
$elapsed_time = $end_time - $start_time;
print "Elapsed time: ".$elapsed_time." ms\n\n";


print "\n*****************************BSONTest*****************************\n";
$start_time = time;
try{
	testBSON(\%beginning_hash);
} catch{
	print "caught error: $_\n";
};
$end_time = time;
$elapsed_time = $end_time - $start_time;
print "Elapsed time: ".$elapsed_time." ms\n\n";

close $fh;



