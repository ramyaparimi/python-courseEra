# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern,Genome):
    Positions=[]
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            Positions.append(i)
    return Positions

print(PatternMatching("ATA","ATATATA"))