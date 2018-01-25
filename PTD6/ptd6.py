from matplotlib import pyplot as plt
import numpy as np

a = [1,0,1,1]

def code(msg):
    x7, x6 ,x5, x3 = msg
    x1 = x3 ^ x5 ^ x7
    x2 = x3 ^ x6 ^ x7
    x4 = x5 ^ x6 ^ x7
    s = [x7,x6, x5, x4, x3, x2, x1]
    return s


def decode(message):
    x7, x6, x5, x4, x3, x2, x1 = message
    x1p = x3 ^ x5 ^ x7
    x2p = x3^ x6 ^ x7
    x4p = x5 ^ x6 ^ x7
    x1k = x1 ^ x1p
    x2k = x2 ^ x2p
    x4k = x4 ^ x4p
    index = x1k + x2k * 2 + x4k * 4
    if index != 0:
        if message[-index] == 0:
            message[-index] = 1
        else:
            message[-index] = 0
    return message

def chbit(bit):
    r = np.random.randint(0,len(bit))
    bit[r] = bit[r] ^ 1
    return bit

def dprint(w):
    x7, x6, x5, x4, x3, x2, x1 = w
    return [x7,x6,x5,x3]

s = code(a)
print('oryginal message: {0} \ncoded message:\n{1}'.format(a,s))
c = chbit(s)
print('random bit changed:')
print(c)
d = decode(c)
print('Repaired signal:')
print(d)
x = dprint(d)
print('encoded signal')
print(x)

