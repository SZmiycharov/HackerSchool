use strict;
use warnings;
use 5.010;
use BSON qw/encode decode/;
use Cpanel::JSON::XS qw(encode_json decode_json);

my $filename = '/home/slavi/Desktop/testfile.txt';
open (my $fh, '<:encoding(UTF-8)', $filename);


my $student = {
    name => 'Foo Bar',
    file => $fh,
    gender => undef,
    classes => [
        'Chemistry',
        'Math',
        'Litreture',
    ],
    address => {
        city => 'Fooville',
        planet => 'Earth',
    },
};
 
my $student_json = encode_json $student;
print "$student_json\n\n";

my $hash_ref = decode_json $student_json;

my %hash = %$hash_ref;

print "Reference: $hash_ref\n\n";
print "Dereferenced:\n";
foreach my $k (keys %hash) {
    if ($hash{$k}){
        print "$k: $hash{$k}\n"; 
    } else{
        print "$k: null\n";
    }

    
}

close $fh;
