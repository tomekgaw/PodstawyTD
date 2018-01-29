from matplotlib import pyplot as plt
import numpy as np
import ptd4copy as ptd4
from itertools import accumulate

#######PSK
sp = [(np.sin(2 * np.pi * ptd4.fn * b/ ptd4.fs)) for b in range(1500)]
psk = np.multiply(ptd4.zp,sp)
def sumation(x):
    xd = suma = 0
    xt = []
    for _ in np.arange(ptd4.M):
        suma = 0
        for _ in np.arange(ptd4.fs):
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

# h1 =10
# xt = sumation(psk)
# ss =  demod1(xt,h1)
# plt.figure()
# plt.subplot(3,1,1)
# plt.title('demodulacja sygnału PSK dla h = {0}'.format(h1))
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.plot(psk)
# plt.subplot(3,1,2)
# plt.xlabel('t')
# plt.ylabel('p(t)')
# plt.plot(xt)
# plt.subplot(3,1,3)
# plt.xlabel('t')
# plt.ylabel('m(t)')
# plt.plot(ss)
# plt.savefig('lab5zad1PSK')
#
# ###############ASK
# sa = [ptd4.A2 * np.sin(2 * np.pi * ptd4.fn * b / ptd4.fs) for b in range(1500)]
# h2 = 35
# ask = np.multiply(ptd4.za,sp)
# s1 = sumation(ask)
# m2 = demod1(s1,h2)
#
# plt.figure()
# plt.subplot(3,1,1)
# plt.title('demodulacja sygnału ASK dla h = {0}'.format(h2))
# plt.xlabel('t')
# plt.ylabel('x(t)')
# plt.plot(ask)
# plt.subplot(3,1,2)
# plt.xlabel('t')
# plt.ylabel('p(t)')
# plt.plot(s1)
# plt.subplot(3,1,3)
# plt.xlabel('t')
# plt.ylabel('m(t)')
# plt.plot(m2)
# plt.savefig('lab5zad1ASK')
#
# ################################FSK
#
# sn1 = [np.sin(2 * np.pi * ptd4.fn1 * b / ptd4.fs) for b in range(1500)]
# sn2 = [np.sin(2 * np.pi * ptd4.fn2 * b / ptd4.fs) for b in range(1500)]
# xt1 = np.multiply(ptd4.zf,sn1)
# xt2 = np.multiply(ptd4.zf,sn2)
# px1 = sumation(xt1)
# px2 = sumation(xt2)
#
# pt = px1 + px2
# h3 = 23
# m3 = demod1(pt,h3)
#
# plt.figure()
# plt.subplot(2,1,1)
# plt.title('FSK x1(t) i px1(t)')
# plt.xlabel('t')
# plt.ylabel('x1(t)')
# plt.plot(xt1)
# plt.subplot(2,1,2)
# plt.xlabel('t')
# plt.ylabel('px2(t)')
# plt.plot(px1)
# plt.savefig('lab5FSKxt')
# plt.figure()
# plt.subplot(2,1,1)
# plt.title('FSK x2(t) i px2(t)')
# plt.xlabel('t')
# plt.ylabel('x1(t)')
# plt.plot(xt2)
# plt.subplot(2,1,2)
# plt.xlabel('t')
# plt.ylabel('px2(t)')
# plt.plot(px2)
# plt.savefig('lab5FSKpxt')
# plt.figure()
#
# plt.subplot(2,1,1)
# plt.title('demodulacja sygnału FSK dla h = {0}'.format(h3))
# plt.xlabel('t')
# plt.ylabel('p(t)')
# plt.plot(pt)
# plt.subplot(2,1,2)
# plt.xlabel('t')
# plt.ylabel('m(t)')
# plt.plot(m3)
# plt.savefig('lab5FSKmtpt')
#
# plt.show()