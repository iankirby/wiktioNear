#!/usr/bin/perl

use warnings;
use strict;
use utf8;
use open qw( :std :encoding(UTF-8));
use Data::Dumper qw(Dumper);


#The main script will pass two arguments to this scripts: the file name (always going to be temp.txt), and the name of the english lexical item.

my $filename="$ARGV[0]";
my $english_word="$ARGV[1]";


open (my $fh,'<: encoding(UTF-8)', $filename) or die "I cannot open $filename $!";


#declare the variable that the whole thing will be read into:
my $plain="";

while (<$fh>){
    $plain=$plain.$_;
}


#In case there are any quotation marks or single quotes, escape them.
$plain=~s/\'/\\\'/g;
$plain=~s/\"/\\\'/g;



print $plain;
# print length(<$plain>);