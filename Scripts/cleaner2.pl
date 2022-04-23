#!/usr/bin/perl

use warnings;
use strict;
use utf8;

use open qw( :std :encoding(UTF-8));
use Data::Dumper qw(Dumper);


#check to see if there is a command line argument; die if not 

if ($#ARGV<0){
    print "Requires the text as a command line argument\n"; die;
}

#reading the file in the command line argument
my $filename="$ARGV[0]";
open(my$fh,'<: encoding(UTF-8)',$filename) or die "can't open file $filename $!";

#plain is a string is the file content
my $plain="";

#read it in row by row
while (my $row=<$fh>){
    $plain=$plain.$row;
}

# print $plain;

# my $string="The food is in the salad bar";
# my $food="food";
# $string=~m/$food/;
# my $in="in";
# print "Before: $`\n";
# print "Matched $&\n";
# print "After $'";


my @spl=split('\n',$plain);
# print$spl[1];

my $i=0;
my $str="";
while ($i<5){
    if ($spl[$i]=~m/'='/){
        $i=$i+1;
    } elsif($spl[$i]=~m/\{\{trans-top\}/){
        print $spl[$i];$i=$i+1;
    } else{
        $str=$str.$spl[$i]."\n";$i=$i+1;
    }
    
}
print $str;

# $plain=~m/[^\{\{trans\-top\|][^\}\}][^\n]/;
# print"$&";
# print $plain;
# print"$'";