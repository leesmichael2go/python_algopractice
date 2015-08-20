#https://www.hackerrank.com/challenges/find-a-string
S = "ABCDCDC"
sub = "CDC"
N = len(S)
n = len(sub)
S = list(S)
sub = list(sub)
matches = 0
for i in range(0, N-n+1):
    if S[i:i+n] == sub:
        matches += 1
print(matches)