import time

Abc = {
    "a": 12,
    "b": 30,
    "c": 5
}

holdrand = 0

def Srand(seed):
    global holdrand
    holdrand = seed

def Rand():
    global holdrand
    holdrand = (holdrand * 214013 + 2531011)
    return (holdrand >> 16) & 0x7fff

def Xor(data, key):
    encrypt = ""
    for i in range(len(data)):
        for j in range(len(data[i])):
            # Correctly format the key character as a binary string and access the j-th bit
            key_bit = format(ord(key[i % len(key)]), '08b')[j]
            encrypt += str(Hash(ord(data[i][j]) ^ int(key_bit)))
        encrypt += ' '
    return encrypt

def Hash(data):
    return Abc['a']*data**2+Abc['b']*data+Abc['c']

def Permute(data):
    p = [28, 32, 15, 8, 27, 5, 21, 12, 26, 34, 23, 10, 22, 1, 37, 36, 0, 11, 18, 29, 35, 13, 9, 17, 3, 24, 16, 30, 14, 20, 2, 33, 4, 19, 6, 25, 7, 31]
    data = data.split()
    permuted = [data[p[i]] for i in range(len(data))]
    return ' '.join(permuted)

def Encrypt(data, random):
    xored = Xor(data, random)
    encrypted = Permute(xored)
    return encrypted

with open("encrypt", 'r') as f:
    message = f.read().split()

Srand(int(time.time()))
random = str(Rand())
random = [random[i:i+2] + ' ' for i in range(0, len(random), 2)]
encrypt = Encrypt(message, random)
with open("secret", 'w') as f:
    f.write(encrypt)
print("(+) Flag encryption done.")