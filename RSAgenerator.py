from Crypto.PublicKey import RSA

private_key = RSA.generate(2048)
f = open('privateKey.pem', 'wb')
f.write(private_key.exportKey('PEM'))
public_key = private_key.publickey()
f1 = open('publicKey.pem', 'wb')
f1.write(public_key.exportKey('PEM'))
f.close()
f1.close()

#file = open('keys/publicKey.pem', 'rb')
#key = RSA.importKey(file.read())
#int = 1 

file = 'keys/publicKey.pem'
key = ''
with open(file, 'r') as keyfile:
    key = RSA.importKey(keyfile.read())
keyPair = key
print(key)