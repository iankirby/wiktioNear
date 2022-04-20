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

#Taking the file name as the 'role', and creating a variable for the actual 
my $role=substr($filename,0,-4);
my $out_name=$role."v2.3Cleaned.txt";
$role="\"".$role."\"";

#plain is a string is the file content
my $plain="";


#read it in row by row
while (my $row=<$fh>){
    $plain=$plain.$row;
}

$plain=~s/\'/\\\'/g;
$plain=~s/\"/\\\'/g;

#these three things be in all of the files, but I don't need them
my $top='====Translations====';
my $mid='\{\{trans-mid';
my $bot='\{\{trans-bottom';
#Remove all of these things
$plain=~s/($top|$mid|$bot)//g;

#this removes the tag for "translation needed"
my $trans_needed='\{\{t-needed\|[^\n]*';
$plain=~s/$trans_needed/\(no translation\)/g;
$plain=~s/\n\}\}[^\n]*\n/\n/g; #Removes the spaces that this creates

#The variable $title will have the actual data. 'plain' is now the variable that will keep the first three columns
#update: wait what is this?  I don't actually use it elsewhere...
my $title=$plain;

# getting ride of wiki tags for translations
$plain=~s/\{\{[^\n]*\n//;
$plain=~s/(\{\{t\|[^\|]*\||\'\'|\}\})//g;
$plain=~s/\{\{t\+[^\|]*\|[^\|]*\|//g;


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


# $plain=~s/\{\{qualifier\|/\{qualifier /g;


#To clone the roles so I can have them as discrete cells as well as in independent cells, I'm going to make a copy of the whole string

my $commas=$plain;

$commas=~s/\"\*[^\:]*:/\"/g;
$commas=~s/\"\"\n\"[^\:]*\:/\" \"\n\"/g;

$commas=~s/\,/\" \, \"/g;

# $plain=~s/\"\*\s/$role\, \"/g;

my @by_line=split (m/r?\n/,$plain);

foreach my $by_line(@by_line){
    if ($by_line=~m/\*\:/){ #this is for dialects
        $by_line=~s/\*\:\s/$role\, \" \"\, \"/g;
        $by_line=~s/\:\s/\"\, \"/g;
        
    } else{ #this is for independent langauges
        $by_line=~s/\*\s/$role\, \"/g;
        $by_line=~s/\:\s/\"\, \" \"\, \"/g;
    }
    $by_line=~s/\:\"/\"\, \" \"\, \" \"/g;
    $by_line=~s/\"\"/\"/g;
}

# print @by_line;



################### 

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
    my $temp_str=$plain_array[$i]."\, ".$commas_array[$i];
    push(@new_array,$temp_str);
    $i++;
}

my $out_str=$new_array[0];
my $j=1;

while ($j<scalar(@new_array)){
    $out_str=$out_str."\n".$new_array[$j];
    $j++;
}

# print $out_str;

open my ($write_fh), '>:encoding(UTF-8)', "$out_name" or die "died";
print $write_fh $out_str;
close($write_fh);

# print $new_array[-2];

# print (@by_line);




# print $plain;
