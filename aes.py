# Irreducible polynomial for AES: x^8 + x^4 + x^3 + x + 1
MOD_POLY = 0x11B

# Multiply two numbers in GF(2^8)
def gf_mul(a: int, b: int) -> int:
    result = 0
    for _ in range(8):
        if b & 1:
            result ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xFF  # keep it 8-bit
        if hi_bit_set:
            a ^= 0x1B  # reduction by x^8 + x^4 + x^3 + x + 1
        b >>= 1
    return result

# Find multiplicative inverse in GF(2^8)
def gf_inv(a: int) -> int:
    if a == 0:
        return 0  # 0 has no inverse
    
    result = 1
    base = a
    for _ in range(254):  # a^(254) = a^(-1) in GF(2^8)
        result = gf_mul(result, base)
    return result

# Example usage
inp ="0x3d"
val=int(inp[2:],16)
inv = gf_inv(val)
print(f"Value: 0x{val:02X}")
print(f"Inverse: 0x{inv:02X}")


A=[
    [1,0,0,0,1,1,1,1],
    [1,1,0,0,0,1,1,1],
    [1,1,1,0,0,0,1,1],
    [1,1,1,1,0,0,0,1],
    [1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,0,0],
    [0,0,1,1,1,1,1,0],
    [0,0,0,1,1,1,1,1],
    
    ]
    
D=[1,1,0,0,0,1,1,0]


B=[0]*8
X=[0]*8

B=[int(i) for i in f'{inv:08b}']
print(B)
B=B[::-1]
print(B)

C=[0]*8

for i in range(8):
    v=0
    for j in range(8):
        v^=A[i][j]&B[j]
    C[i]=v
print(C)

for i in range(8):
    X[i]=C[i]^D[i]
    
print(X[::-1])
X=X[::-1]

out_str=''.join(str(i) for i in X)

decimal=int(out_str,2)
print(decimal)

hex_value=hex(decimal)
print(hex_value)



    






