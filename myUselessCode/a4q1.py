import random

def genseq(n):
  S = []
  for _ in range(n): S.append(random.randint(1,n))
  return S

def longest(S):
  L= [1]
  for k in range(1,len(S)):
    mymax = 0
    for j in range(k):
      if S[j]<S[k]: mymax = max(mymax,L[j])
    L.append(1+mymax)
  return L

S = genseq(20); print S
S=[8,3,2,7,4,9,1,11,5]
L = longest(S); print L
