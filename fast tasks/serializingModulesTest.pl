use warnings;
use strict;
use lib '/home/slavi/Desktop/HackerSchool/fast\ tasks';
use serializeHash;
use Try::Tiny;

sub testFreezeThaw($){
	my %beginning_hash = %{$_[0]};
	serializeHashToFileFreezeThaw(\%beginning_hash, '/home/slavi/Desktop/test.txt');
	my %deserializedHash = deserializeFileTextToHashFreezeThaw('/home/slavi/Desktop/test.txt');

	print "beginning hash:\n";
	print Dumper(\%beginning_hash) . "\n\n";

	print "deserializedHash:\n";
	print Dumper(\%deserializedHash) . "\n\n";

	use Test::Deep;
	cmp_deeply(\%beginning_hash, \%deserializedHash);
}

sub testJSON($){
	my %beginning_hash = %{$_[0]};
	serializeHashToFileJSON(\%beginning_hash, '/home/slavi/Desktop/test.txt');
	my %deserializedHash = deserializeFileTextToHashJSON('/home/slavi/Desktop/test.txt');

	print "beginning hash:\n";
	print Dumper(\%beginning_hash) . "\n\n";

	print "deserializedHash:\n";
	print Dumper(\%deserializedHash) . "\n\n";

	use Test::Deep;
	cmp_deeply(\%beginning_hash, \%deserializedHash);
}

sub testYAML($){
	my %beginning_hash = %{$_[0]};
	serializeHashToFileYAML(\%beginning_hash, '/home/slavi/Desktop/test.yml');
	my %deserializedHash = deserializeFileTextToHashYAML('/home/slavi/Desktop/test.yml');

	print "beginning hash:\n";
	print Dumper(\%beginning_hash) . "\n\n";

	print "deserializedHash:\n";
	print Dumper(\%deserializedHash) . "\n\n";

	use Test::Deep;
	cmp_deeply(\%beginning_hash, \%deserializedHash);	
}

sub testBSON($){
	my %beginning_hash = %{$_[0]};
	serializeHashToFileBSON(\%beginning_hash, '/home/slavi/Desktop/test.txt');
	my %deserializedHash = deserializeFileTextToHashBSON('/home/slavi/Desktop/test.txt');

	print "beginning hash:\n";
	print Dumper(\%beginning_hash) . "\n\n";

	print "deserializedHash:\n";
	print Dumper(\%deserializedHash) . "\n\n";

	use Test::Deep;
	cmp_deeply(\%beginning_hash, \%deserializedHash);
}



$ARGV[0] or die "You should provide a file path from cmd line!";
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



