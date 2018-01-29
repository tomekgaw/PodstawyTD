from matplotlib import pyplot as plt
import numpy as np
import functions as f
a = [1,0,1,1]



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
# fn = 2
# zp = []
# fs = 100
# c = f.code(a)       #zmiana wpisanego sygnalu na ciag bitow
# ch = f.chbit(c)     #zamiana losowego bitu w sygnale
# mPSK =  f.modPSK(ch,fs,fn)      #modulacja sygnalu
# noise = np.random.normal(0,2,700)
# s = mPSK + noise
# dPSK = f.dmodPSK(s,fs,fn,8)  #demodulacja sygnału
# back = f.concentr(dPSK)
# msg = f.decode(back)
# ms = f.dmessage(msg)
# print(ch)
# print(back)
# print(msg)
# print(f.reverse(ms))

fn = 2
fs = 100
c = f.code(a)  #zmiana wpisanego sygnalu na ciag bitow
print('zmieniony na bity',c)
ch = f.chbit(c)     #zamiana losowego bitu w sygnale
print('zmieniony bit',ch)
mASK = f.modASK(ch,fs,fn)      #modulacja sygnalu
noise = np.random.normal(0,2,700)
s = mASK + noise
dASK = f.dmodASK(s,fs,fn,30)  #demodulacja sygnału
back = f.concentr(dASK)
print('spowrotem na 7 bitow',back)
msg = f.decode(back)
print('naprawa ',msg)
ms = f.dmessage(msg)
print((ms))


plt.subplot(3,1,1)
plt.plot(mASK)
plt.subplot(3,1,2)
plt.plot(dASK)
plt.subplot(3,1,3)
plt.plot(s)
plt.show()
