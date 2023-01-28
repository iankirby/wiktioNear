#!/usr/bin/perl

use strict;
use warnings;

my $x="Hello what're you talking about?";

$x=~s/[^(?=Hello)]//;
print$x;