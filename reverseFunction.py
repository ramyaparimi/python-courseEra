# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    x=""
    for i in Pattern:
        x=i+x
    return x



print(Reverse("AAAACCCGGT"))