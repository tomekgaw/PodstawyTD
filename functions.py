import numpy as np


def code(msg):
    x7, x6 ,x5, x3 = msg
    x1 = x3 ^ x5 ^ x7
    x2 = x3 ^ x6 ^ x7
    x4 = x5 ^ x6 ^ x7
    s = [x7,x6, x5, x4, x3, x2, x1]
    return s


def decode(message):
    x7, x6, x5, x4, x3, x2, x1 = message
    x1p = x3 ^ x5 ^ x7
    x2p = x3^ x6 ^ x7
    x4p = x5 ^ x6 ^ x7
    x1k = x1 ^ x1p
    x2k = x2 ^ x2p
    x4k = x4 ^ x4p
    index = x1k + x2k * 2 + x4k * 4
    if index != 0:
        if message[-index] == 0:
            message[-index] = 1
        else:
            message[-index] = 0
    return message

def dmessage(w):
        x7, x6, x5, x4, x3, x2, x1 = w
        return [x7, x6, x5, x3]


def chbit(bit):
    r = np.random.randint(0,len(bit))
    bit[r] = bit[r] ^ 1
    return bit


def modPSK(changed, fs, fn):
    zp = []
    n = np.arange(7)
    d = np.arange(fs)
    for b in n:
        for x in d:
            if changed[b] == 0:
                zp.append(np.sin(2 * np.pi * fn * x / fs))
            else:
                zp.append(np.sin(np.pi + 2 * np.pi * fn * x / fs))
    return zp


def modASK(changed, fs, fn):
    A1 = 0.5
    A2 = 4
    M = 7
    za = []
    n = np.arange(M)
    d = np.arange(fs)
    for b in n:
        for x in d:
            if changed[b] == 0:
                za.append(A1 * np.sin(2 * np.pi * fn * x / fs))
            else:
                za.append(A2 * np.sin(2 * np.pi * fn * x / fs))
    return za

def modFSK(changed, fs, tb, N):
    fn1 = (N + 1) / tb
    fn2 = (N + 2) / tb
    zf = []
    n = np.arange(7)
    d = np.arange(fs)
    for b in n:
        for x in d:
            if changed[b] == 0:
                zf.append(np.sin(2 * np.pi * fn1 * x / fs))
            else:
                zf.append(np.sin(2 * np.pi * fn2 * x / fs))

    return zf

def sumation(x,fs):
    xd = suma = 0
    xt = []
    for _ in np.arange(7):
        suma = 0
        for _ in np.arange(fs):
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


def concentr(signal):
    ss = np.array(signal)
    w = np.split(ss,7)
    syg = []
    for i in range(len(w)):
        if np.count_nonzero(w[i]) == 0:
            syg.append(0)
        else:
            syg.append(1)
    return syg

def reverse(bit):
    bit  = [bit[r] ^ 1 for r in range(len(bit))]
    return bit

def dmodPSK(zp ,fs, fn,h):
    sp = [(np.sin(2 * np.pi * fn * b/ fs)) for b in range(700)]
    psk = np.multiply(zp,sp)
    s = sumation(psk,fs)
    d =demod1(s,h)
    return d

def dmodASK(za ,fs, fn,h):
    sa = [(1 * np.sin(2 * np.pi * fn * b / fs)) for b in range(700)]
    ask = np.multiply(za,sa)
    s = sumation(ask,fs)
    d =demod1(s,h)
    return d

def dmodFSK(zp ,fs, fn,h):
    sp = [(np.sin(2 * np.pi * fn * b/ fs)) for b in range(700)]
    psk = np.multiply(zp,sp)
    s = sumation(psk,fs)
    d =demod1(s,h)
    return d