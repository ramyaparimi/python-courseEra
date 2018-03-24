def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile={}
    for symbol in "ACGT":
        profile[symbol]=Count(Motifs)[symbol]
        for j in range(k):
            profile[symbol][j]=(profile[symbol][j])/t
    return profile

print(Profile(["AACGTA", "CCCGTT"]))