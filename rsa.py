def mod_inverse(a: int, phi: int) -> int:
    a = a % phi
    if a == 0:
        raise ValueError("Inverse does not exist for 0")

    t0, t1 = 0, 1
    r0, r1 = phi, a

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1

    if r0 != 1:
        raise ValueError(f"No modular inverse exists for {a} mod {phi}")

    # Make sure result is positive
    return t0 % phi
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from math import gcd

p,q=1709,1109
n=p*q
phi=(p-1)*(q-1)

e=3

if gcd(e,phi)!=1:
    raise ValueError(f"{e} is not co prime of phi {phi}")
d= mod_inverse(e,phi)

x=30

en=pow(x,e,n)
print(en)
de=pow(en,d,n)
print(de)

pt="hello"

en_pt=[pow(ord(ch),e,n) for ch in pt]

print(en_pt)

de_pt=''.join(chr(pow(i,d,n)) for i in en_pt)

print(de_pt)







