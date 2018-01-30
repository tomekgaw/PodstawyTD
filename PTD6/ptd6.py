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
fn = 2
fs = 100
c = f.code(a)       #zmiana wpisanego sygnalu na ciag bitow
ch = f.chbit(c)     #zamiana losowego bitu w sygnale
mPSK = f.modPSK(ch,fs,fn)      #modulacja sygnalu
noise = np.random.normal(0,1,700)
sPSK = mPSK + noise
dPSK = f.dmodPSK(sPSK,fs,fn,8)  #demodulacja sygnału
backPSK = f.concentr(dPSK)
msgPSK = f.decode(backPSK)
msPSK = f.dmessage(msgPSK)
print(ch)
print(backPSK)
print(msgPSK)
print(f.reverse(msPSK))

  #zmiana wpisanego sygnalu na ciag bitow
print('zmieniony na bity',c)
#zamiana losowego bitu w sygnale
print('zmieniony bit',ch)
mASK = f.modASK(ch,fs,fn)      #modulacja sygnalu
sASK = mASK + noise
dASK = f.dmodASK(sASK,fs,fn,30)  #demodulacja sygnału
backASK = f.concentr(dASK)
print('spowrotem na 7 bitow',backASK)
msgASK = f.decode(backASK)
print('naprawa ',msgASK)
msASK = f.dmessage(msgASK)
print((msASK))

#zmiana wpisanego sygnalu na ciag bitow
print('zmieniony na bity',c)
    #zamiana losowego bitu w sygnale
print('zmieniony bit',ch)
mFSK = f.modFSK(ch,fs,1,1)      #modulacja sygnalu
sFSK = mFSK + noise
dFSK = f.dmodFSK(sFSK,fs,1,1,50)  #demodulacja sygnału
backFSK = f.concentr(dFSK)
print('spowrotem na 7 bitow',backFSK)
msgFSK = f.decode(backFSK)
print('naprawa ',msgFSK)
msFSK = f.dmessage(msgFSK)
print((msFSK))




plt.figure()
plt.subplot(3,1,1)
plt.plot(mFSK)
plt.subplot(3,1,2)
plt.plot(dFSK)
plt.subplot(3,1,3)
plt.plot(sFSK)

plt.figure()
plt.subplot(3,1,1)
plt.plot(mPSK)
plt.subplot(3,1,2)
plt.plot(dPSK)
plt.subplot(3,1,3)
plt.plot(sPSK)

plt.figure()
plt.subplot(3,1,1)
plt.plot(mASK)
plt.subplot(3,1,2)
plt.plot(dASK)
plt.subplot(3,1,3)
plt.plot(sASK)
plt.show()
