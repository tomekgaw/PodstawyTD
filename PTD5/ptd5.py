from matplotlib import pyplot as plt
import numpy as np
import ptd4
from scipy import integrate

#######ASK




def demod1(d,h):
    s = []
    it = np.arange(len(w))
    for i in it:
        if d[i] >= h:
            s.append(1)
        else:
            s.append(0)
    return s

##ASK
h1 = 2
ask = np.multiply(ptd4.za,ptd4.sa)
y = ask
w = integrate.cumtrapz(ask,y)
m = demod1(w,h1)

plt.figure()
plt.subplot(3,1,1)
plt.title('demodulacja sygnału ASK dla h = {0}'.format(h1))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(ask)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(w)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('m(t)')
plt.plot(m)
plt.savefig('lab5zad1ASK')



###PSK
h2 = 2



psk = np.multiply(ptd4.zp,ptd4.sp)
print(ptd4.zp)
print(ptd4.sp)
y = ask
# w = integrate.cumtrapz(psk,y)
m2 = demod1(w,h1)

plt.figure()
plt.subplot(3,1,1)
plt.title('demodulacja sygnału PSK dla h = {0}'.format(h2))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(ask)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.plot(w)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('m(t)')
plt.plot(m)
plt.savefig('lab5zad1PSK')
plt.show()