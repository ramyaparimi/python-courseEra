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

print(ReverseComplement("CCAGATC"))