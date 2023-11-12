import hashlib
import base64

def convertTextToInt(text):
    encode_text = text.encode('utf-8')
    hex_text = encode_text.hex()
    int_text = int(hex_text,16)
    return int_text

def convertIntToHex(decimal_number):
    hexadecimal_value = hex(decimal_number)
    return hexadecimal_value
def hashing(message):
    hash_message = int(hashlib.sha512(str(message).encode("utf-8")).hexdigest(),16)
    return hash_message

def gcd(a,b):
    while a !=0:
        a, b = b % a, a
    return b

def positiveModulus(a,p):
    if a < 0:
        a = (a + p * int(abs(a)/p) + p) % p
    return a

def modInverse(a,m):
    if a < 0:
        a = (a + m * int(abs(a)/m) + m) % m
    
    if gcd(a,m) != 1:
        return None
    
    u1,u2,u3 = 1,0,a 
    v1,v2,v3 = 0,1,m 
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def applyDoubleAndAddMethod(P,k,a,d,mod):
    additionPoint = (P[0],P[1])
    kAsBinary = bin(k)
    kAsBinary = kAsBinary[2:len(kAsBinary)] 
    for i in range(1,len(kAsBinary)):
        currentBit = kAsBinary[i: i+1]
        additionPoint = pointAddition(additionPoint, additionPoint, a, d, mod)
        if currentBit == '1':
            additionPoint = pointAddition(additionPoint, P, a, d, mod)      
    return additionPoint  

def pointAddition(P,Q,a,d,mod):
    x1 = P[0]; y1=P[1]
    x2 = Q[0]; y2=Q[1]
    x3 = (((x1*y2 + y1*x2) % mod) * modInverse(1+d*x1*x2*y1*y2,mod))%mod 
    y3 = (((y1*y2 - a*x1*x2) % mod) * modInverse(1- d*x1*x2*y1*y2, mod)) % mod
    return x3,y3

def to_pem_pk(publicKey):
    x = base64.b64encode(str(publicKey[0]).encode('ascii'))
    y = base64.b64encode(str(publicKey[1]).encode('ascii'))
    z = bytes(str("~~").encode())
    pub_key = x+ z+ y
    print(f'-----BEGIN PUBLIC KEY-----\n{pub_key}\n-----END PUBLIC KEY-----\n')

def to_pem_sign(R,s):
    RI = base64.b64encode(str(R[0]).encode('ascii'))
    RII = base64.b64encode(str(R[1]).encode('ascii'))
    z = bytes(str("~~").encode())
    sI = base64.b64encode(str(s).encode('ascii'))
    print(f'-----SIGNATURE-----\n{RI+z+RII}\n{sI}\n-----END -----\n')

def from_pem_pK(pub_key):
    
    puk = pub_key.split(b'~~')
    publicKey=[]
    publicKey.append(int(base64.b64decode(puk[0].decode())))
    publicKey.append(int(base64.b64decode(puk[1].decode())))
    return publicKey

def from_pem_sing(RII,s):
    RI = RII.split(b'~~')
    R=[]
    R.append(int(base64.b64decode(RI[0].decode())))
    R.append(int(base64.b64decode(RI[1].decode())))
    s = int(base64.b64decode(s.decode()))
    return tuple(R),s
# from ecdsa import SigningKey, NIST384p
# sk = SigningKey.generate(curve=NIST384p)
# sk_string = sk.to_string()
# sk2 = SigningKey.from_string(sk_string, curve=NIST384p)
# print(sk_string.hex())
# print(sk2.to_string().hex())