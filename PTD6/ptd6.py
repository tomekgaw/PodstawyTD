from matplotlib import pyplot as plt
import numpy as np
import functions as f
a = [1,0,1,1]
b = [1,0,0,1]
fn = 2
fs = 100
################### zad 1
# s = f.code(a)
# print('oryginal message: {0} \ncoded message:\n{1}'.format(a,s))
# c = f.chbit(s)
# print('random bit changed:')
# print(c)
# d = f.decode(c)
# print('Repaired signal:')
# print(d)
# x = f.dmessage(d)
# print('encoded signal')
# print(x)

########################### zad2

s = f.code(a)
c = f.chbit(s)
mPSKzad2 = f.modPSK(c,fs,fn)
dPSKzad2 = f.dmodPSK(mPSKzad2,fs,fn,8)
backPSK = f.concentr(dPSKzad2)
msgPSK = f.decode(backPSK)
msPSK = f.dmessage(msgPSK)
print(f.reverse(msPSK))

# ############## zad 3
# data = {0:{'ASK':[],'PSK':[],'FSK':[]}}
# fn = 2
# fs = 100
# tablePSK = []
# tableASK = []
# tableFSK = []
# # print('zad3 PSK')
# for _ in range(100):
#     c = f.code(a)  # zmiana wpisanego sygnalu na ciag bitow
#     noise = np.random.normal(0, 15, 700) # szum (środek, wartość, ilość próbek)
#     ch = f.chbit(c)  # zamiana losowego bitu w sygnale
#     mPSK = f.modPSK(ch,fs,fn)      #modulacja sygnal
#     sPSK = mPSK + noise             # dodanie szumu do zmodulowanego sygnalu
#     dPSK = f.dmodPSK(sPSK,fs,fn,8)      # demodulacja sygnalu
#     backPSK = f.concentr(dPSK)          # spowrotem 7 bitow
#     msgPSK = f.decode(backPSK)          # poprawianie bledow
#     msPSK = f.dmessage(msgPSK)          # wypisanie przeslanej wiadomosci
#
#     tablePSK.append(f.check(a, msPSK)) # obliczanie BSK
#
#     if a == f.reverse(msPSK):           # obliczanie ilosci udanych przeslan wiadomosci
#         data[0]['PSK'].append(1)
#     else:
#         data[0]['PSK'].append(0)
#     # print('zad3 ASK')
#     mASK = f.modASK(ch,fs,fn)      #modulacja sygnalu
#     sASK = mASK + noise
#     dASK = f.dmodASK(sASK,fs,fn,30)  #demodulacja sygnału
#     backASK = f.concentr(dASK)
#     msgASK = f.decode(backASK)
#     msASK = f.dmessage(msgASK)
#
#     tableASK.append(f.check(a, msASK))
#
#     if a == (msASK):
#         data[0]['ASK'].append(1)
#     else:
#         data[0]['ASK'].append(0)
#
#
#     # print('zad3 FSK')
#     mFSK = f.modFSK(ch,fs,1,1)      #modulacja sygnalu
#     sFSK = mFSK + noise
#     dFSK = f.dmodFSK(sFSK,fs,1,1,50)  #demodulacja sygnału
#     backFSK = f.concentr(dFSK)
#     msgFSK = f.decode(backFSK)
#     msFSK = f.dmessage(msgFSK)
#
#     tableFSK.append(f.check(a, msFSK))
#
#     if a == f.reverse(msFSK):
#         data[0]['FSK'].append(1)
#     else:
#         data[0]['FSK'].append(0)


# print(sum(data[0]['ASK']))
# print(sum(data[0]['PSK']))
# print(sum(data[0]['FSK']))
#
# print(sum(tableASK)/100)
# print(1 -sum(tablePSK)/100)
# print(1 -sum(tableFSK)/100)

##rysunki do ustalenia h

# plt.figure()
# plt.subplot(3,1,1)
# plt.title('FSK')
# plt.plot(mFSK)
# plt.subplot(3,1,2)
# plt.plot(dFSK)
# plt.subplot(3,1,3)
# plt.plot(sFSK)
#
# plt.figure()
# plt.subplot(3,1,1)
# plt.title('PSK')
# plt.plot(mPSK)
# plt.subplot(3,1,2)
# plt.plot(dPSK)
# plt.subplot(3,1,3)
# plt.plot(sPSK)
#
# plt.figure()
# plt.subplot(3,1,1)
# plt.title('ASK')
# plt.plot(mASK)
# plt.subplot(3,1,2)
# plt.plot(dASK)
# plt.subplot(3,1,3)
# plt.plot(sASK)
# plt.show()
