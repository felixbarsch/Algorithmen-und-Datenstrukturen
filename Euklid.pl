#!/usr/bin/perl

# Mit gannzahliger Division
sub ggT {
    my ($a, $b) = @_;
    while ($b) {
        ($a, $b) = ($b, $a % $b);
    }
    return $a;
}

# Ausgabe
print ggT(48, 18)."\n";

