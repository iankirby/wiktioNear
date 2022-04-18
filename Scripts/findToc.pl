#/usr/bin/perl

use strict;
use warnings; use utf8;

#First, verify that there is a command line argument.
if ($#ARGV<0){die "Requires a command line argument";}

#Read the file in as a command line argument
my $filename="$ARGV[0]";
$filename="../FilesOut/".$filename;
open (my $fh, '<: encoding(UTF-8)', $filename) or die "Cannot open $filename $!";

my $raw="";

while (my $row=<$fh>){$raw=$raw.$row;}

#print $raw;

my @lines =split (m\r?\n, $raw);
# print @lines;
print scalar(@lines);

my $line="";
my $eng="";
# my $pattrn=

# foreach $line (@lines){
#     if ($line=~m/\#English\"/){
#         print $line;
#     }
# }

# print $eng;