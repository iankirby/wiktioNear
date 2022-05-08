#!/usr/bin/perl

use warnings;
use strict;
use utf8;
use open qw( :std :encoding(UTF-8));
use Data::Dumper qw(Dumper);

# my $temp_file="temp.txt";
my $filename="$ARGV[0]";
my $english_word="$ARGV[1]";

my $perl_out="perlOut.txt";


open(my$fh,'<: encoding(UTF-8)', $filename) or die "I cannot open $filename $!";


# my $plain="";
my $plain="";

while(<$fh>){
   $plain=$plain.$_;
}

$plain=~s/\'/\\\'/g;
$plain=~s/\"/\\\'/g;

#these three things be in all of the files, but I don't need them
my $top='====Translations====';
my $mid='\{\{trans-mid';
my $bot='\{\{trans-bottom';
#Remove all of these things
$plain=~s/($top|$mid|$bot)//g;
$plain=~s/\=.\n//g; #removes empty equals signs.

#this removes the tag for "translation needed"
my $trans_needed='\{\{t-needed\|[^\n]*';
$plain=~s/$trans_needed/\(no translation\)/g;
$plain=~s/\n\}\}[^\n]*\n/\n/g; #Removes the spaces that this creates


my @plain_split=split(/\n/,$plain);
my $role=$plain_split[0];
$role=~s/(\{\{trans-top\||\}\})//g;
# print$role;


#Removing the translation top thing from the table.
$plain=~s/\{\{trans-top[^\n]+.\n//g;

#Removes user-input comments
$plain=~s/\<![^\>]*\>//g;

#Removes user-input comments
$plain=~s/\<![^\>]*\>//g;

#this puts a quotation mark before * (It's a place-holder for the )
$plain=~s/\n\*/\n\"\*/g;

#Adds a quotation 
$plain=~s/\s*\n/\"\n/g;

#if there is a single quote (e.g. palatalization), escape sequence it out
$plain=~s/\'/\\\'/g;

#annoying problem
$plain=~s/==\"\n//g;


#To clone the roles so I can have them as discrete cells as well as in independent cells, I'm going to make a copy of the whole string

my $commas=$plain;

$commas=~s/\"\*[^\:]*:/\"/g;
$commas=~s/\"\"\n\"[^\:]*\:/\" \"\n\"/g;

$commas=~s/\,/\" \, \"/g;

# $plain=~s/\"\*\s/$role\, \"/g;

my @by_line=split (m/r?\n/,$plain);

foreach my $by_line(@by_line){
    if ($by_line=~m/\*\:/){ #this is for dialects
        $by_line=~s/\*\:\s/\"$english_word\" \, \"$role\"\, \" \"\, \"/g;
        $by_line=~s/\:\s/\"\, \"/g;
        
    } else{ #this is for independent langauges
        $by_line=~s/\*\s/\"$english_word\" \, \"$role\"\, \"/g;
        $by_line=~s/\:\s/\"\, \" \"\, \"/g;
    }
    $by_line=~s/\:\"/\"\, \" \"\, \" \"/g;
    $by_line=~s/\"\"/\"/g;
}

# print @by_line;

my $index=0;

my $new_plain="";

while ($index<scalar(@by_line)){
    $new_plain=$new_plain.$by_line[$index]."\n";
    $index++;
}

chomp($new_plain);

# print $new_plain;

chomp($commas);
# print $commas;

my @plain_array=split "\n",$new_plain;

my @commas_array=split "\n",$commas;

my @new_array=();

if (scalar(@commas_array)!=scalar(@plain_array)){
    print "Error in $filename $! The length of the arrays is not the same!"; die;
}

my $i=0;

while ($i<scalar(@plain_array)){
    my $temp_str=$plain_array[$i]." \, ".$commas_array[$i];
    push(@new_array,$temp_str);
    $i++;
}

my $out_str=$new_array[0];
my $j=1;

while ($j<scalar(@new_array)){
    $out_str=$out_str."\n".$new_array[$j];
    $j++;
}

# $out_str=~s/\"//g;

#Remove the {{t(+)|lng tag
# $out_str=~s/\{\{t[^t]*\|[^\|]*\|[^\|]//g;

print$out_str;


##this is the code that writes it to a file.
# open my ($write_fh), '>:encoding(UTF-8)', "perlOut.txt" or die "died";
# print $write_fh $out_str;
# close($write_fh);



########################

# print$plain;

# $role=~s/[^\n]*.\n.[^\n]*//g;
# print$role;

# print$plain;

# open my($write_fh), '>:encoding(UTF-8)', "$perl_out" or die "died";
# print $write_fh $plain;
# close($write_fh);


# my @plain=split(/\n/,$plain);
# my $lexical_item=$plain[0];

# print$lexical_item;



# my $i=1; #Start at second item, because the first line is not useful.
# while ($i<=scalar(@plain)){
#     # my $curr=$plain[$i];
#     if ($plain[$i]==$lexical_item){
        
#     }
#     if ($plain[$i]=="="){

#     }
# }

