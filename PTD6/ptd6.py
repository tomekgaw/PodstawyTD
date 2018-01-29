from matplotlib import pyplot as plt
import numpy as np
import ptd5
import ptd4copy as ptd4
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

# s = code(a)
# print('oryginal message: {0} \ncoded message:\n{1}'.format(a,s))
# c = chbit(s)
# print('random bit changed:')
# print(c)
# d = decode(c)
# print('Repaired signal:')
# print(d)
# x = dprint(d)
# print('encoded signal')
# print(x)



############## kodowanie
s2 = code(a)
fn = 2
zp = []
fs = 100

def sumation(x):
    xd = suma = 0
    xt = []
    for _ in np.arange(7):
        suma = 0
        for _ in np.arange(fs):
            suma += x[xd]
            xt.append(suma)
            xd = xd + 1
    return xt

def demod1(d,h):
    s = []
    it = np.arange(len(d))
    for i in it:
        if d[i] >= h:
            s.append(1)
        else:
            s.append(0)
    return s

cbit = chbit(s2)
n = np.arange(7)
d = np.arange(fs)
for b in n:
    for x in d:
        if cbit[b] == 0:
            zp.append(np.sin(2 * np.pi * fn * x / fs))
        else:
            zp.append(np.sin(np.pi + 2 * np.pi * fn * x / fs))

sp = [(np.sin(2 * np.pi * fn * b/ fs)) for b in range(700)]
psk = np.multiply(zp,sp)
s = sumation(psk)
d = demod1(s,4)
dd = np.array(d)
w = np.split(dd,7)
syg = []
for i in range(7):
    if np.sum(w[i])<50:
        syg.append(1)
    else:
        syg.append(0)
print('sygnal na wejsciu')
print(a)
print('zmiana wartosci losowego bitu')
print(s2)
print('modulacja sygnalu')
print(zp)
print('sygnal zdemudolwany')
print(syg)
print('dekoder')
print(dprint(decode(syg)))
plt.figure()
plt.subplot(2,1,1)
plt.title('sygnal p(t) i m(t) demodulacja PSK')
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(s)
plt.subplot(2,1,2)
plt.xlabel('t')
plt.ylabel('m(t)')
plt.plot(d)
plt.savefig('lab6rys')
plt.show()

