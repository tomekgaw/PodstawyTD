import numpy as np
import matplotlib.pyplot as plt

# Fs musi byc takie samo dla wszystkich sygnalow
Fn = 250
Fm = 10
Fs = 200
Am = 1
Ka = [0.3,7,36]
Kp = [1.9,3,39]
t = np.arange(Fs)
mt = Am * np.sin(2 * np.pi * Fm * t / Fs)
# AM ###################################################
za1 = (Ka[0] * mt + 1) * np.cos(2 * np.pi * Fn * t / Fs)
za2 = (Ka[1] * mt + 1) * np.cos(2 * np.pi * Fn * t / Fs)
za3 = (Ka[2] * mt + 1) * np.cos(2 * np.pi * Fn * t / Fs)
# PM ###################################################
zp1 = np.cos(2 * np.pi * Fn * t / Fs + Kp[0] * mt)
zp2 = np.cos(2 * np.pi * Fn * t / Fs + Kp[1] * mt)
zp3 = np.cos(2 * np.pi * Fn * t / Fs + Kp[2] * mt)

# f1 = plt.figure(1)
# plt.plot(mt)
# plt.title('sygnał informacyjny')
# plt.ylabel('m(t)')
# plt.xlabel('t')
# plt.savefig('lab3sygnalSin')
# f2 =  plt.figure(2)
# plt.subplot(3,1,1)
# plt.title('modulacja AM dla Ka = 0.3')
# plt.ylabel('za(t)')
# plt.xlabel('t')
# plt.plot(za1)
# plt.subplot(3,1,2)
# plt.title('modulacja AM dla Ka = 7')
# plt.ylabel('za(t)')
# plt.xlabel('t')
# plt.plot(za2)
# plt.subplot(3,1,3)
# plt.title('modulacja AM dla Ka = 36')
# plt.ylabel('za(t)')
# plt.xlabel('t')
# plt.plot(za3)
# plt.savefig('lab3modulacjaAM')
#
# f3 =  plt.figure(3)
# plt.subplot(3,1,1)
# plt.title('modulacja PM dla Kp = 1.9')
# plt.ylabel('zp(t)')
# plt.xlabel('t')
# plt.plot(zp1)
# plt.title('modulacja PM dla Kp = 3')
# plt.ylabel('zp(t)')
# plt.xlabel('t')
# plt.subplot(3,1,2)
# plt.title('modulacja PM dla Kp = 39')
# plt.ylabel('zp(t)')
# plt.xlabel('t')
# plt.plot(zp2)
# plt.subplot(3,1,3)
# plt.title('modulacja PM dla Kp = 38')
# plt.ylabel('zp(t)')
# plt.xlabel('t')
# plt.plot(zp3)
# plt.savefig('lab3modulacjaPM')
#


f2 =  plt.figure(1)
plt.subplot(3,1,1)
plt.title('widmo amplitudowe modulacji AM dla Ka = 0.3')
plt.ylabel('Za(t)')
plt.xlabel('t')
F1 = np.fft.fft(za1)
plt.plot(abs(F1))
plt.subplot(3,1,2)
plt.title('widmo amplitudowe modulacji AM dla Ka = 7')
plt.ylabel('Za(t)')
plt.xlabel('t')
F2 = np.fft.fft(za2)
plt.plot(abs(F2))
plt.subplot(3,1,3)
plt.title('widmo amplitudowe modulacji dla Ka = 36')
plt.ylabel('Za(t)')
plt.xlabel('t')
F3 = np.fft.fft(za3)
plt.plot(abs(F3))
plt.savefig('lab3widmoAM')

f3 =  plt.figure(3)
plt.subplot(3,1,1)
plt.title('widmo amplitudowe modulacji PM dla Kp = 1.9')
plt.ylabel('Zp(t)')
plt.xlabel('t')
F4 = np.fft.fft(zp1)
plt.plot(abs(F4))
plt.title('widmo amplitudowe modulacji PM dla Kp = 3')
plt.ylabel('Zp(t)')
plt.xlabel('t')
plt.subplot(3,1,2)
plt.title('widmo amplitudowe modulacji PM dla Kp = 39')
plt.ylabel('Zp(t)')
plt.xlabel('t')
F5 = np.fft.fft(zp2)
plt.plot(abs(F5))
plt.subplot(3,1,3)
plt.title('modulacja PM dla Kp = 38')
plt.ylabel('zp(t)')
plt.xlabel('t')
F6 = np.fft.fft(zp3)
plt.plot(abs(F6))
plt.savefig('lab3widmoPM')


FF = [F1,F2,F3,F4,F5,F6]

def decyb(signal):
    DB = [20 * np.log10(np.abs(signal))]
    minim = np.amin(DB)
    maxim = np.amax(DB)
    w = ((maxim-3.0)-minim)
    print('Wartość minimalna: {0}\nwartość maksymalna: {1}\noszacowana szerokość: {2}'.format(minim,maxim,w))

for i in FF:
    decyb(i)


plt.show()