def solveknapsack(val,wt,W):
  n = len(val)
  K = [[0 for j in xrange(n+1)] for w in xrange(W+1)]
  for j in range(1,n+1):
    for w in range(W+1):
      if wt[j-1]>w: K[w][j] = K[w][j-1]
      else: K[w][j] = max(K[w][j-1], K[w-wt[j-1]][j-1]+val[j-1])
