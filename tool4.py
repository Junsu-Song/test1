import sys

def mer(l1, l2, n):
    if n == 1:
        return l2

    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)
    return mer(l1, ltmp, n-1)
            
l1 = ["A", "G", "C", "T"]
l2 = ["A", "G", "C", "T"]
n = int(sys.argv[1])

print(mer(l1, l2, n))


