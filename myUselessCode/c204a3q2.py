import math
def mst(n): # based on:
    if n<=1:
        return 0

    return n-1+mst(math.floor(float(n)/2))+mst(math.ceil(float(n)/2))

for i in range(0,8):
    print(mst(10**i))

for i in range(0,8):
    print(math.ceil(math.log(math.factorial(10**i),2)))
