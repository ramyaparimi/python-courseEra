def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n // 2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n // 2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i - 1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i + (n // 2) - 1] == symbol:
            array[i] = array[i] + 1
    return array


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count

print(FasterSymbolArray("AAAAGGGG","A"))

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    x=""
    for i in Pattern:
        x=i+x
    return x

def Complement(Pattern):
    x=""
    for i in Pattern:
        if i=="A":
            x=x+"T"
        elif i=="T":
            x=x+"A"
        elif i=="G":
            x=x+"C"
        else:
            x=x+"G"
    return x

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern,Genome):
    Positions=[]
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            Positions.append(i)
    return Positions

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

