import random
from . import ecd_helper as helper

class ECDSA():
    def  __init__(self):        
        self.p = pow(2, 255) - 19
        self.p2 = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
        self.base = 15112221349535400772501151409588531511454012693041857206046113283949847762202, 46316835694926478169428394003475163141307993866256225615783033603165251855960
        super().__init__()
        print("ECDSA Job online ....???")
        self.a = -1; self.d = helper.positiveModulus(-121665 * helper.modInverse(121666, self.p), self.p)
        self.x0 = self.base[0]; self.y0 = self.base[1]
        
    def main(self,opts):
        if opts[0] == 's':
            self._signature(opts[1])
        elif opts[0] == 'v':
            self._verification(opts[1],opts[2],opts[3],opts[4])

    def _signature(self,msg):
        message = helper.convertTextToInt(msg)
        privateKey = random.getrandbits(256) #32 byte secret key
        publicKey = helper.applyDoubleAndAddMethod(self.base, privateKey, self.a, self.d, self.p)
        r = helper.hashing(helper.hashing(message) + helper.hashing(message)) % self.p
        R = helper.applyDoubleAndAddMethod(self.base, r, self.a, self.d, self.p)
        h = helper.hashing(R[0]+publicKey[0]+helper.hashing(message)) % self.p
        s = ( r + h * privateKey)
        hex_s = helper.convertIntToHex(s)
        helper.to_pem_pk(publicKey)
        helper.to_pem_sign(R,s)   
              
    def _verification(self,publicKey,R,s,message):
        R,s = helper.from_pem_sing(R,s)
        publicKey = helper.from_pem_pK(publicKey)
        print(R[0],publicKey[0])
        h = helper.hashing(R[0]+publicKey[0]+helper.hashing(message)) % self.p
        P1 = helper.applyDoubleAndAddMethod(self.base, s, self.a, self.d, self.p)
        P2 = helper.pointAddition(R, helper.applyDoubleAndAddMethod(publicKey, h, self.a, self.d, self.p), self.a, self.d, self.p)
        if P1[0] == P2[0] and P1[1] == P2[1]:
            print("The Signature is valid")
        else:
           print("The Signature violation detected!")

# x = ECDSA()._signature()
# R= b'NTMyODcwNzIwMTAxNDExMDk3NDc1MzIzODQ5MjY3MzI3ODAxNTU4OTU3NTQzMDQ5NDA5Njc5MDAwMjI2MzA2MTA4NDMyMTkyMzgwMg==~~NzI5NDA2OTUyODYxMjk0MTI0NjgwNDc2ODg4MTY4NzUzNzMyMjUwMzk4ODI5NDE2MDgzMzY3NTQ1OTk0MzE2NzU0MTcxNzY0OTY3Mw=='
# s =b'MTUyNjE5OTU1MjE1NDQ2MDUyMDcyNDAyNzM1NDczMjUwNzg5MDMzMzY2MjQwOTA2MjYwNzQ0ODA3MzA0MTQ2NzA4MjU3ODQyMDEyNTQ1NTg3MTkzNDA5MTkwODExODE5ODY3NTQ0ODkwMzM2NDg2NTg2ODg1MDE5MDUwNzAzNDY5NTAxNTUyMjAzMDEzNjU5MjgyMTYwMTA='
# publicKey = b'MTExNjY2MzY3NjAyOTU5MzkyNzEyNzkzMjg1OTM2NzkyODIyNDU3NzMyNDkyNjg2MTgzMjcyNjI0ODgwOTU1OTc3MzE5NjYxMTA5ODc=~~MjMxNTUzMjcxNzIyMjEyMjY2NTk0Mzc5MDc2MTU4OTUxMzI3MjY4NDg2OTgxMDA0OTQzOTI2MjE3MTU5NDIxMTE3ODkyMDU5MDk5NjA='
# message = helper.convertTextToInt("no women no cry")
    
# ECDSA()._verification(publicKey,R,s,message)