import random

def GibbsSampler(Dna, k, t, N):
    motifs=RandomMotifs(Dna,k,t)
    BestMotifs=motifs

    i = random.randint(1,t-1)
    for j in range(1,N):
        del motifs[i]
        profile=ProfileWithPseudocounts(motifs)
        Motif_i=ProfileGeneratedString(Dna[i],profile,k)
        motifs.insert(i,Motif_i)
        if Score(motifs)<=Score(BestMotifs):
            return BestMotifs


def RandomizedMotifSearch(Dna, k, t):

    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def Count(Motifs):
    count = {}  # initializing the count dictionary
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
    profile = {}
    for symbol in "ACGT":
        profile[symbol] = Count(Motifs)[symbol]
        for j in range(k):
            profile[symbol][j] = (profile[symbol][j]) / t
    return profile


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Score(Motifs):
    score = 0
    k = len(Motifs[0])
    t = len(Motifs)
    consensus = Consensus(Motifs)
    for i in range(t):
        for j in range(k):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score


def Pr(Text, ProfileWithPseudocounts):
    # insert your code here
    p = 1
    for char in range(len(Text)):
        p = p * ProfileWithPseudocounts[Text[char]][char]
    return p


def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    mostprobable_pattern = ""
    max_prob = -1
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]

        if Pr(Pattern, Profile) > max_prob:
            max_prob = Pr(Pattern, Profile)
            mostprobable_pattern = Pattern
    return mostprobable_pattern


def GreedyMotifSearch(Dna,k,t):
    BestMotifs=[]
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "TACG":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def PseudoCount(Motifs):
    Pseudo_Count = {}  # initializing the count dictionary
    # your code here
    k = len(Motifs[0])
    for symbol in "ATGC":
        Pseudo_Count[symbol] = []
        for j in range(k):
            Pseudo_Count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            Pseudo_Count[symbol][j] += 1
    return Pseudo_Count


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile_Pseudocounts = {}
    for symbol in "ATGC":
        profile_Pseudocounts[symbol] = PseudoCount(Motifs)[symbol]
        num_ele=len(PseudoCount(Motifs))
        for j in range(k):
            profile_Pseudocounts[symbol][j] = profile_Pseudocounts[symbol][j]/(t+num_ele)
    return profile_Pseudocounts


def ProfileMostProbablePattern(Text, k, ProfileWithPseudocounts):
    mostprobable_pattern = ""
    max_prob = -1

    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]

        if Pr(Pattern, ProfileWithPseudocounts) > max_prob:
            max_prob = Pr(Pattern, ProfileWithPseudocounts)
            mostprobable_pattern = Pattern

    return mostprobable_pattern

def GreedyMotifSearchWithPseudocounts(Dna,k,t):
    BestMotifs=[]
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def Motifs(Profile,Dna):
    k=len(Profile['A'])
    t=len(Dna)
    prob_pattern=[]
    for i in range(len(Dna)):
        pattern=ProfileMostProbablePattern(Dna[i],k,Profile)
        prob_pattern.append(pattern)

    return prob_pattern


def RandomMotifs(Dna, k, t):
    random_motif=[]
    for i in range(t):
        d_string = len(Dna[0])
        s = random.randint(1, (d_string - k))
        random_kmer=Dna[i][s:s+k]
        random_motif.append(random_kmer)
    return random_motif


def Normalize(Probabilities):
    val=Probabilities.values()
    total_val=sum(val)
    for key,value in Probabilities.items():
        value=value/total_val
        Probabilities[key]=value
    return Probabilities


def WeightedDie(Probabilities):
    p=random.uniform(0,1)
    total=0
    for key,value in Probabilities.items():
        total+=value
        if p<=total:
            return key



def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


k=8
t=5
N=100
Dna=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
    'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
    'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
    'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
    'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

print(GibbsSampler(Dna,k,t,N))