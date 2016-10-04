use warnings;
use strict;
use lib '/home/slavi/Desktop/HackerSchool/fast\ tasks';
use serializeHash;
use Try::Tiny;


$ARGV[0] or die "You should provide a file path from cmd line!";
my $nested_file = "/home/slavi/Desktop/testfile.txt";
open (my $fh, "<", $nested_file) or die "Could not open $nested_file!";
my %hash_to_nest = (a => 'asd');
my @arr_to_nest = qw(a b c d);
my $helper_num = 10;
my $blessed_var = bless \$helper_num;
my %beginning_hash;

$beginning_hash{"a"}{Mathematics}   = [1,2,3,4,5,6, [1,2,3]];
$beginning_hash{"a"}{Literature}    = \%hash_to_nest;
$beginning_hash{"b"}{Literature}   = $fh;
$beginning_hash{"b"}{Mathematics}  = \@arr_to_nest;
$beginning_hash{"b"}{Art}          = $blessed_var;

print "************FreezeThawTest************\n";
my $start_time = [Time::HiRes::gettimeofday()];
try{
	testFreezeThaw(\%beginning_hash);
} catch{
	print "caught error: $_";
};
my $diff = Time::HiRes::tv_interval($start_time);
print "Elapsed time: $diff ms\n";
print "\n\n";

print "************JSONTest************\n";
$start_time = [Time::HiRes::gettimeofday()];
try{
	testJSON(\%beginning_hash);
} catch{
	print "caught error: $_";
};
$diff = Time::HiRes::tv_interval($start_time);
print "Elapsed time: $diff ms\n";
print "\n\n";

print "************YAMLTest************\n";
$start_time = [Time::HiRes::gettimeofday()];
try{
	testYAML(\%beginning_hash);
} catch{
	print "caught error: $_";
};
$diff = Time::HiRes::tv_interval($start_time);
print "Elapsed time: $diff ms\n";
print "\n\n";

print "************BSONTest************\n";
$start_time = [Time::HiRes::gettimeofday()];
try{
	testBSON(\%beginning_hash);
} catch{
	print "caught error: $_";
};
$diff = Time::HiRes::tv_interval($start_time);
print "Elapsed time: $diff ms\n";
print "\n\n";

close $fh;



