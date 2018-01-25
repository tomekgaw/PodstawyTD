from matplotlib import pyplot as plt
import numpy as np
import ptd4
from scipy import integrate



#######ASK

sp = []
for _ in range(0,len(ptd4.zp)):
    x = np.sin(2 * np.pi * ptd4.fn / ptd4.fs)
    sp.append(x)

psk = np.multiply(ptd4.zp,sp)
A1za = []
A2za = []
for i in range(0,100):
    A1za.append(np.sin(2 * np.pi * ptd4.fn / ptd4.fs))
    A2za.append( np.sin(np.pi + 2 * np.pi * ptd4.fn / ptd4.fs ))

xd = []
zA = []
n = np.arange(ptd4.M)
d = np.arange(ptd4.fs)
try:
    for b in n:
        s = 0.0
        for x in d:
            if ptd4.data_in[b] == 1:
                zA.append( A1za[x] * ptd4.A1 * np.sin(2 * np.pi * ptd4.fn * x / ptd4.fs))
            else:
                w = A1za[x] * ptd4.A2 * np.sin(2 * np.pi * ptd4.fn * x / ptd4.fs)
                zA.append(w)
            s = s + zA[x]


except:
    pass

y = psk
w = integrate.cumtrapz(psk,initial=0)
print(w)

def demod1(d,h):
    s = []
    it = np.arange(len(d))
    for i in it:
        if d[i] >= h:
            s.append(1)
        else:
            s.append(0)
    return s

# ss =  demod1(new,0.5)

##ASK
h1 = 6

plt.figure()
plt.subplot(3,1,1)
plt.title('demodulacja sygnału ASK dla h = {0}'.format(h1))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(psk,w)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(w)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('m(t)')
# plt.plot(ss)
# plt.savefig('lab5zad1ASK')



##PSK
# h2 = 2
#
# x = np.sin(2 * np.pi * pfn * x / fs)
#
#
# psk = np.multiply(ptd4.zp,ptd4.sp)
#
# m2 = demod1(w,h1)
#
# plt.figure()
# plt.subplot(3,1,1)
# plt.title('demodulacja sygnału PSK dla h = {0}'.format(h2))
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.plot(ask)
# plt.subplot(3,1,2)
# plt.xlabel('t')
# plt.ylabel('p(t)')
# plt.plot(w)
# plt.subplot(3,1,3)
# plt.xlabel('t')
# plt.ylabel('m(t)')
# plt.plot(m)
# plt.savefig('lab5zad1PSK')
plt.show()