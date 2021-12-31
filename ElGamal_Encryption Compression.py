#Nishaant Goswamy
#Student ID: 31415001
from random import randrange
import cryptAlg as crypt
from CompressDecompress import CompressEncodedText, Print_Encrypted_Decrypt_Stmt


def Gen_Mask(sender, pubKy, k , p ):
    mask = crypt.Square_And_Multiply(pubKy,k, p)

    while mask == 1:
        new_k = randrange(1,100)
        mask = crypt.Square_And_Multiply(pubKy,new_k, p)
        if mask != 1:
            k = new_k
            print(sender+"'s new k value: ", k)
            break
    return mask, k


print("This is ElGamal Encryption")
p = int(input("Enter a prime value p: "))

if not crypt.primeCheck(p): quit()

a = int(input("User A enter private key a: "))
b = int(input("User B enter private key b: "))
k = int(input("Select secret key k: "))

g = crypt.Generator((p - 1), p)
print("Generator g: ", g)

pubA_key = crypt.Square_And_Multiply(g,a, p)
print("A's Public Key: ", pubA_key)

pubB_key = crypt.Square_And_Multiply(g,b, p)
print("B's Public Key: ", pubB_key)

maskA,ka = Gen_Mask("A",pubB_key, k, p)
maskB,kb = Gen_Mask("B", pubA_key, k, p)

print("A's Mask:", maskA)
print("B's Mask:", maskB)


reciever =str(input("Encryption, select which user to send the message: ")).upper().strip()

if reciever == "B":
    mask = maskA
    k = ka
    q = p - 1 - b

elif reciever == "A":
    mask = maskB
    k = kb
    q = p - 1 - a

Hint = crypt.Square_And_Multiply(g,k,p)

R = crypt.Square_And_Multiply(Hint, q, p)

msg = input("Enter the message string: ").lower().strip()
NumList, size = CompressEncodedText(msg)

decryptedNumList = []
encryptedNumList = []



for enc_num in NumList:
    enc_num = int(enc_num)

    print("***Encryption Process***")
    print("key: ", k)
    print("Mask: ",mask)
    print("Msg num encrypting: ", enc_num)

    if enc_num > p:
        print("Msg_Num bigger than p. Aborted")
        quit()


    Ciphertext = (enc_num * mask) % p
    print("CipherText: ", Ciphertext)
    encryptedNumList.append(str(Ciphertext).zfill(size))


    print("Hint:", Hint)

    print("***Decryption Process***")

    print("q:", q)
    print("Opener: ", R)

    DecryptNum = (Ciphertext*R)%p
    print("Decrypted Message: ", DecryptNum)
    decryptedNumList.append(str(DecryptNum).zfill(size))

    if enc_num == DecryptNum:
        print('Success Decrypted Message Matches Original Message!\n')

Print_Encrypted_Decrypt_Stmt(encryptedNumList, decryptedNumList, msg)











