# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
# We say that position i in k-mers p and q is a mismatch if the symbols at position i of the two strings are not the same.
# The total number of mismatches between strings p and q is called the Hamming distance between these strings.
#  We will let you implement a function to compute this distance, called HammingDistance(p, q).

def HammingDistance(p, q):
    distance=0
    for i in range(0,len(p)):
            if p[i]!=q[i]:
                distance=distance+1
    return distance


print(HammingDistance("GGGCCGTTGGT","GGACCGTTGAC"))