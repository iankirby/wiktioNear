#!/usr/bin/perl

use warnings;
use strict;
use utf8;
use open qw( :std :encoding(UTF-8));
use Data::Dumper qw(Dumper);


#The main script will pass two arguments to this scripts: the file name (always going to be temp.txt), and the name of the english lexical item.

my $filename="$ARGV[0]";
my $english_word="$ARGV[1]";

my $perl_out="perlOut.txt";


open (my $fh,'<: encoding(UTF-8)', $filename) or die "I cannot open $filename $!";


#declare the variable that the whole thing will be read into:
my $plain="";

while (<$fh>){
    $plain=$plain.$_."\"";
}


#In case there are any quotation marks or single quotes, escape them.
$plain=~s/\'/\\\'/g;
$plain=~s/\"/\\\'/g;

my $top='====Translations===='; #I think it was stripped in the python script, but remove it just inc case
my $mid='\{\{trans-mid';
my $bot='\{\{trans-bottom';

#remove top, middle, and bottom tags 
$plain=~s/($top|$mid|$bot)//g;

#this removes the tag for "translation needed"
my $trans_needed='\{\{t-needed\|[^\n]*';
$plain=~s/$trans_needed/\(no translation\)/g;
$plain=~s/\n\}\}[^\n]*\n/\n/g; #Removes the spaces that this creates

#Removes user-input comments
$plain=~s/\<![^\>]*\>//g;

#I'm going to keep all the variables a single cell for the time being.
# HOw should I add a quotation mark to the end of each line...
$plain=~s/^(.*)$/\"/g;

# $plain=~s/\:\s\{\{/, \"\{\{/g;

#Separate into cells
# $plain=~s/\*[^\:]/ ,  /g;
# $plain=~s/\*\:/ , , /g;
print $plain;


# $plain=~s/\{\{t[^\|]*\|[^\|]*\|//g;


# print $plain;
