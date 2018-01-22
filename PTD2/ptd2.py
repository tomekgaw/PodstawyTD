import matplotlib.pyplot as plt
import numpy as np
import ptd1


# zadanie 1
def dft(signal):
    N = len(signal)
    outim = []
    outre = []
    output = []
    for k in range(N):
        sumim = 0.0
        sumre = 0.0
        for n in range(N):
            angle = 2 * np.pi * k * n/N
            sumre += signal[n] * np.sin(angle) + signal[n]*np.cos(angle)
            sumim += -signal[n] * np.sin(angle) + signal[n]*np.cos(angle)
        outim.append(sumim)
        outre.append(sumre)
        output.append(np.sqrt(outim[k]**2 + outre[k]**2))
    return output


# zad2

plt.figure(1)
plt.subplot(3,1,1)
plt.title('widma amplutidowe zad1 i zad2')
plt.ylabel('X(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.xn))
plt.subplot(3,1,2)
plt.ylabel('Z(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.zn))
plt.subplot(3,1,3)
plt.ylabel('V(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.vn))
plt.savefig('lab2zad1a')

plt.figure(2)
plt.title('widmo amplitudowe zad 3')
plt.ylabel('U(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.un))
plt.savefig('lab2zad1b')

plt.figure(3)
plt.title('widmo amplitudowe zad 4 H = 5')
plt.ylabel('G(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.S1))
plt.savefig('lab2zad1c')

plt.figure(4)
plt.title('widmo amplitudowe zad 4 H = 10')
plt.ylabel('G(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.S2))
plt.savefig('lab2zad1d')

plt.figure(5)
plt.title('widmo amplitudowe zad 4 H = 15')
plt.ylabel('G(n)')
plt.xlabel('n')
plt.plot(dft(ptd1.S3))
plt.savefig('lab2zad1e')

T = 1
fs = 1024
Ts = T * fs
n = np.arange(500)
zn = np.sin(200*np.pi*n/fs) + 0.5*np.sin(350*np.pi*n/fs)
plt.subplot(2,1,1)
plt.title('widmo amplitudowe sygnału z(n)')
plt.ylabel('z(n)')
plt.xlabel('n')
plt.plot(n, zn,'k-')

F = np.fft.fft(zn)
plt.subplot(2,1,2)
plt.ylabel('Z(n)')
plt.xlabel('n')
plt.plot(abs(F))
plt.savefig('lab2zad3')
plt.show()