from matplotlib import pyplot as plt
import numpy as np

A1 = 0.5
A2 = 1
fn = 2
fs = 100 # musi byc wieksze niz 2x fn
M = 15 # ilosc bitow do przeslania
tb = 1 #czas trwania bitu w sekundach
N = 1

fn1 = (N+1)/tb
fn2 = (N+2)/tb

data_in = [1,1,0,0,1,0,1,0,1,1,1,0,1,0,0]
# data_in = np.random.randint(2, size=M) ## losowe tworzenie tablicy z 0 lub 1 przy rozmiarze M podawanym wczesniej
# dlatego wykresy są różne cały czas
############## ASK
za = []
n = np.arange(M)
d = np.arange(fs)
for b in n:
    for x in d:
        if data_in[b] == 0:
            za.append( A1 + np.sin(2 * np.pi * fn * x / fs))
        else:
            za.append(A2  + np.sin(2 * np.pi * fn * x / fs))
###################FSK
zf = []
n = np.arange(M)
d = np.arange(fs)
for b in n:
    for x in d:
        if data_in[b] == 0:
            zf.append(np.sin(2 * np.pi * fn1 * x / fs))
        else:
            zf.append(np.sin(2 * np.pi * fn2 * x / fs))
###################PSK
zp = []
n = np.arange(M)
d = np.arange(fs)
for b in n:
    for x in d:
        if data_in[b] == 0:
            zp.append(np.sin(2 * np.pi * fn * x / fs))
        else:
            zp.append(np.sin(np.pi + 2 * np.pi * fn * x / fs))

plt.figure(1)
plt.subplot(3,1,1)
plt.title('zadanie 1 modulacje kolejno od góry: ASK, FSK, PSK')
plt.xlabel('t')
plt.ylabel('za(t)')
plt.plot(za)
plt.subplot(3,1,2)
plt.xlabel('t')
plt.ylabel('zf(t)')
plt.plot(zf)
plt.subplot(3,1,3)
plt.xlabel('t')
plt.ylabel('zp(t)')
plt.plot(zp)
# plt.savefig('lab4zad1')

# F1 = np.fft.fft(za)
# F2 = np.fft.fft(zf)
# F3 = np.fft.fft(zp)
# f3 =  plt.figure(2)
# plt.subplot(3,1,1)
# plt.title('widma amplitudowe od góry ASK, FSK, PSK')
# plt.ylabel('Za(t)')
# plt.xlabel('t')
# plt.plot(abs(F1))
# plt.subplot(3,1,2)
# plt.ylabel('Zf(t)')
# plt.xlabel('t')
# plt.plot(abs(F2))
# plt.subplot(3,1,3)
# plt.ylabel('Zp(t)')
# plt.xlabel('t')
# plt.plot(abs(F3))
# plt.savefig('lab4zad2widma')


# M = ('ASK','FSK','PSK')
# def decyb(signal):
#     DB = [20 * np.log10(np.abs(signal))]
#     minim = np.amin(DB)
#     maxim = np.amax(DB)
#     w = ((maxim-3.0)-minim)
#     print('Wartość minimalna: {0}\nwartość maksymalna: {1}\noszacowana szerokość: {2}'.format(minim,maxim,w))
#
# print('ASK')
# decyb(F1)
# print('FSK')
# decyb(F2)
# print('PSK')
# decyb(F3)
#
#
#
#
plt.show()