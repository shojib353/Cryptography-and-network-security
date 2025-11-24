# define hillman algorithm
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors
    
    
    
    
    
    
    
    
p,g=23,5

q=prime_factors(p-1)

print(q)

for i in q:
    x=(p-1)/i
    z=pow(g,int(x),p)
    
    if z==1:
        raise ValueError(f"g={g} is not premitive root of {p}={p-1}")

a,b=12,21 #2 to p-2

A=pow(g,a,p)
B=pow(g,b,p)

s1=pow(B,a,p)
s2=pow(A,b,p)

if s1==s2:
    print ("key share success full")
else:
    print("not share")

    
    
    
    
    
    
    
    