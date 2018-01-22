import numpy as np
import matplotlib.pyplot as plt

f = 4
fi = (7*np.pi)/9
fs = 100
ts = 1.0/fs
a = np.arange(fs)
xn = 0.7*np.sin(2*np.pi*f * a/fs + fi)

f = plt.figure(1)
plt.title('zad1')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.plot(xn)
plt.savefig('lab1zad1')

yn = (3*a-1)/((a**2)+1)
zn = yn * (np.abs(xn)**0.333)
f2 = plt.figure(2)

plt.subplot(2,1,1)
plt.title('zad2')
plt.xlabel('n')
plt.ylabel('z(n)')
plt.plot(a,zn)

vn = xn + (yn/(np.abs(xn)+1.78))
plt.subplot(2,1,2)
plt.xlabel('n')
plt.ylabel('v(n)')
plt.plot(a,vn)
plt.savefig('lab1zad2')



#zadanie 3

fs3 = 1200
prob = fs3 * 3
tt = np.arange(prob)
un = []
for i in tt:
    if i<prob*0.2 and i>=0:
        un.append(0.8*np.sin(20*np.pi*i/fs3))

    elif i>=prob*0.2 and i<prob*0.4:
       un.append((np.float_power(np.e, i/fs3-0.2)) * 0.8 * np.sin(20 * np.pi * i/fs3))

    elif i>=0.4*prob and i<0.6*prob:
        un.append(0.6*np.sin(10*np.pi*i/fs3))

    elif i>=0.6*prob and i<0.8*prob:
        un.append(np.float_power(np.e, i/fs3-0.6) * 0.6*np.sin(10*np.pi*i/fs3))

    elif i>=prob*0.8 and i<prob:
        un.append(np.log2(0.7*i)*0.5*np.sin(40*np.pi*i/fs3))
f4 = plt.figure(4)
plt.title('zad3')
plt.ylabel('u(n)')
plt.xlabel('n')
plt.plot(un)
plt.savefig('lab1zad3')


#zadanie 4

T = 4
fs4 = 10000
prob4 = fs4 * T

n = np.arange(prob4)
s1 = s2 = s3 = 0
S1 = S2 = S3 = 0
for i in n:
    H = np.arange(1, 6)
    s1 += (1/H) * np.sin(H * np.pi/3) * np.sin((np.pi * H * i)/ (0.1 * fs4))
    S1 = s1 * 9/np.pi**2


for i in n:
    H = np.arange(1, 11)
    s2 += (1/H) * np.sin(H * np.pi/3) * np.sin((np.pi * H * i)/ (0.1 * fs4))
    S2 = s2 * 9/np.pi**2

for i in n:
    H = np.arange(1, 16)
    s3 += (1/H) * np.sin(H * np.pi/3) * np.sin((np.pi * H * i)/ (0.1 * fs4))
    S3 = s3 * 9/np.pi**2

f5 = plt.figure(5)
plt.title('zad4 dla H = 5')
plt.ylabel('g(t)')
plt.xlabel('t')
plt.plot(S1)
plt.savefig('lab1zad4H=5')
f6 = plt.figure(6)
plt.title('zad4 dla H = 10')
plt.ylabel('g(t)')
plt.xlabel('t')
plt.plot(S2)
plt.savefig('lab1zad4H=10')
f7 = plt.figure(7)
plt.title('zad4 dla H = 15')
plt.ylabel('g(t)')
plt.xlabel('t')
plt.plot(S3)
plt.savefig('lab1zad4H=15')
plt.show()