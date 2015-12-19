import random 
def gcd(a,b):
    iterations = 0
    while b>0:
        iterations += 1
        a, b = b, a % b
    return a, iterations

def experiment(bits):
    n, experiments, sum = pow(2,bits), 100, 0
    for j in range(experiments):
        a = random.randint(n/2+1,n-1)
        b = random.randint(n/4+1,n/2-1)
        sum += gcd(a,b)[1]
    print sum/(1.0*experiments)

experiment(250); experiment(500); experiment(1000)
