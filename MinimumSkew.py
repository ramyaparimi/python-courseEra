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
    return Skew

# generate an empty list positions
# set a variable equal to SkewArray(Genome)
# find the minimum value of all values in the skew array
# range over the length of the skew array and add all positions achieving the min to positions
# Genome as input and returning all integers i minimizing Skew[i] for Genome. Then add this function to Replication.py.
# (Hint: make sure to call Skew(Genome) as a subroutine, and keep in mind that Python has a built-in min function in addition to max.)

def MinimumSkew(Genome):
    positions=[]
    skew_array=SkewArray(Genome)
    mini_value=min(dict.values(skew_array))
    for value in skew_array:
        if skew_array[value]==mini_value:
            positions.append(value)
    return positions

print(MinimumSkew("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"))

