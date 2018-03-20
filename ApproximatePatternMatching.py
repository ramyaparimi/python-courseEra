# fill in your PatternMatching() function along with any subroutines that you need.
# fill in your PatternMatching() function along with any subroutines that you need.
def ApproximatePatternMatching(Text, Pattern, d):
    Positions=[]
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i + len(Pattern)], Pattern) <= d:
            Positions.append(i)

    return Positions

def HammingDistance(p, q):
    distance=0
    for i in range(0,len(p)):
            if p[i]!=q[i]:
                distance=distance+1
    return distance

print(ApproximatePatternMatching("CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT","ATTCTGGA",3))
