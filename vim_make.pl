#!/usr/bin/perl

use strict;
use warnings;

my $num_arg = @ARGV;
if ($num_arg > 2) {die "\n\thow to usage: vsim_make.pl <use_verilog_vector> <enter chip tck> \n\n";}
my $use_vfile = $ARGV[0];
my $tck = $ARGV[1];
my $netlist_path_ref = "........xxxxx";
my $netlist_path_new = "....xxxx";
my @vlines;
my $ref_path = ",,,,,,dddd";

#########
#handle: gen. new.v and .run file for new vector
#########
my @titles = split(/\./, $use_vfile);
my $titlename = $titles[0];
system "cp ${ref_path}check_dr.v ${titlename}_tb.v";
system "cp ${ref_path}run_fn ${titlename}.run"


######
#handle: *.v files
######
open FH3, "${titlename}_tb.v" || die "$!\n";
    my @line3 = <FH3>;
close FH3;

open FH3, ">${titlename}_tb.v" || die "$!\n";
    foreach my $vline (@line3)
        {
            if($vline =~ /^([\/*]+)(.*)/){
                print FH3 "$vline";
                next;
            }elsif($vline =~ /^(\`include)\s${netlist_path_ref}\s(.*)/)
                {
                    print FH3 "\`include \"\.\/${titlename}\.v\"\n";
            }else{
                print FH3 "$vline";
            }
        }
close FH3;

#####
#handle *.run files
#####

open FH4, "${titlename}.run" || die "$!\n";
    my @line4 = <FH4>;
close FH4

open FH4, ">{titlename}.run" || die "$!\n";
    foreach my $vline4 (@line4)
    {
        $vline4 =~ s/check_dr/${titlename}_tb/g;
        print FH4 "vline4";
        print "vline4";
    }
close FH4




