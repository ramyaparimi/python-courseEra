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

print(SkewArray("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"))



