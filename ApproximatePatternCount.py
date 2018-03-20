# Copy your PatternCount function from the previous step below this line
def ApproximatePatternCount(Pattern,Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i + len(Pattern)], Pattern) <= d:
            count = count+1
    return count


def HammingDistance(p, q):
    distance=0
    for i in range(0,len(p)):
            if p[i]!=q[i]:
                distance=distance+1
    return distance


print(ApproximatePatternCount("GAGG","TTTAGAGCCTTCAGAGG",2))