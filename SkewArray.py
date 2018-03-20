"""Given a string Genome, we can form its skew array by setting Skew[0] equal to 0, and then ranging﻿ through the genome.
At position i of Genome, if we encounter an A or a T, we set Skew[i+1] equal to Skew[i];
if we encounter a G, we set Skew[i+1] equal to Skew[i]+1; if we encounter a C, we set Skew[i+1] equal to Skew[i-1]-1."""

def SkewArray(Genome):
    Skew={}
    Skew[0]=0
    for i in range(0,len(Genome)):
        if Genome[i]=="A":
            Skew[i+1]=Skew[i]
        elif Genome[i]=="T":
            Skew[i+1]=Skew[i]
        elif Genome[i]=="G":
            Skew[i+1]=Skew[i]+1
        elif Genome[i]=="C":
            Skew[i+1]=Skew[i]-1
    Value=list(dict.values(Skew))
    return Value


print(SkewArray("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))

