from matplotlib import pyplot as plt
import numpy as np
import ptd4copy as ptd4
from itertools import accumulate



#######PSK

sp = []
n = np.arange(ptd4.M)
d = np.arange(ptd4.fs)
for b in n:
    for s in d:
        x = np.sin(2 * np.pi * ptd4.fn * s/ ptd4.fs)
        sp.append(x)

psk = np.multiply(ptd4.zp,sp)
def sumation(x):
    n = np.arange(ptd4.M)
    d = np.arange(ptd4.fs)
    suma = 0
    xt = []
    for i in n:
        suma = 0
        for j in d:
            suma += x[j]
            xt.append(suma)
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


h1 = 4
xt = sumation(psk)
ss =  demod1(xt,h1)
plt.figure()
plt.subplot(3,1,1)
plt.title('demodulacja sygnału PSK dla h = {0}'.format(h1))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(psk)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(xt)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('m(t)')
plt.plot(ss)
plt.savefig('lab5zad1PSK')


sa = []
for _ in n:
    for s in d:
        sa.append(ptd4.A2 * np.sin(2 * np.pi * ptd4.fn * s / ptd4.fs))


h2 = 3

ask = np.multiply(ptd4.za,sp)
s1 = sumation(ask)
m2 = demod1(s1,h2)

plt.figure()
plt.subplot(3,1,1)
plt.title('demodulacja sygnału PSK dla h = {0}'.format(h2))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(ask)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(s1)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('m(t)')
plt.plot(m2)
plt.savefig('lab5zad1ASK')
plt.show()