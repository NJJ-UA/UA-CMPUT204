def bfs(G): # depth in bfs forest
  seen, depth = {}, {}
  for v in G:
    seen[v], depth[v] = False, 0
  print 'bfs order       ',
  for v in sorted(G):
    if not seen[v]:
      explorebfs(G,v,seen,depth)
  print '\nnodes           ',
  for v in sorted(G): print v,
  print '\nbfs forest depth',
  for v in sorted(G): print depth[v],
  print ''

def addtolist(L,v,seen):
  L.append(v); seen[v]=True

def explorebfs(G,v,seen,d):
  Q = []
  addtolist(Q,v,seen)
  while len(Q)>0:
    v = Q.pop(0); print v,
    for nbr in G[v]:
      if not seen[nbr]:
        d[nbr] = 1 + d[v]
        addtolist(Q,nbr,seen)

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''

G = { 'A':['E'],
      'B':['A','C'],
      'C':['G'],
      'D':['C'],
      'E':['B','I'],
      'F':['B','E','G'],
      'G':['D'],
      'H':['D','G','L'],
      'I':['E'],
      'J':['F','I','K'],
      'K':['G','H','J'],
      'L':['K'],
      }

bfs(G)
