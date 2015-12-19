import random
def compositeWitness(w,n,verbose): # miller rabin
  # is w witness for n composite ?
  assert 1==n%2
  s,z = 0, n-1
  while (0== z%2):
    s+=1
    z/=2
  y = pow(w,z,n)
  for j in range(s):
    z = (y*y)%n
    if z == 1 and y !=1 and y != n-1:
      if verbose: print w, 'yields root', y
      return True  # yes, composite
    y = z
  if (z != 1):
    if verbose: print w, '  fails Fermat'
    return True    # yes, composite
  return False       # no, probably prime

def isComposite(n,t,verbose): # t tries to show composite
  if verbose: print n,
  knownComposite = False
  tries = 0
  while (not knownComposite) and (tries < t):
    tries += 1
    a = random.randint(2,n-2)
    knownComposite = compositeWitness(a,n,verbose)
    if verbose and not knownComposite: print a,
  return knownComposite

def primetest(n,t):
  if isComposite(n,t,True):
    print n,'composite'
  else:
    print n,'prime\nProb >= 1.0 -', pow(.25,t)

x=2327701575478432041568051112953132364253959630107925231126314751166886247680031277741025955350572733728820350613741853299629071579082142435470464410781973089465538548735539586873606902277269805728639

y=4455150050241084211380418206396093885965329102785162045912774353570323307393258540221313160825849347159767744245701131071510923556002383329778455288729216887042409330796749411493829108116716299737273
primetest(x,5)

print 'b----------------------'

primetest(y,200)
