import numpy as np

def code(msg): #zmiana wiadomosci 4 bitowej na 7
    x7, x6 ,x5, x3 = msg
    x1 = x3 ^ x5 ^ x7
    x2 = x3 ^ x6 ^ x7
    x4 = x5 ^ x6 ^ x7
    s = [x7,x6, x5, x4, x3, x2, x1]
    return s

def decode(message): # naprawa 7 bitowej wiadomosci
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

def dmessage(w): # konwersja z 7 bitowej wiadomosci do 4
        x7, x6, x5, x4, x3, x2, x1 = w
        return [x7, x6, x5, x3]

def chbit(bit): # zmiana losowego bitu w wiadomosci
    r = np.random.randint(0,len(bit))
    bit[r] = bit[r] ^ 1
    return bit

def modPSK(changed, fs, fn): # modulacja PSK
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

def modASK(changed, fs, fn): # modulacja ASK
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

def modFSK(changed, fs, tb, N): # modulacja FSK
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

def sumation(x,fs): # calkowanie do demodulacji
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

def concentr(signal):  # zmiana sygnalu na wiadomosc 7 bitowa
    ss = np.array(signal)
    w = np.split(ss,7)
    syg = []
    for i in range(len(w)):
        if np.count_nonzero(w[i]) == 0:
            syg.append(0)
        else:
            syg.append(1)
    return syg

def reverse(bit):  # zmiana bitow
    bit  = [bit[r] ^ 1 for r in range(len(bit))]
    return bit

def dmodPSK(zp ,fs, fn,h): # demodulacja PSK
    sp = [(np.sin(2 * np.pi * fn * b/ fs)) for b in range(700)]
    psk = np.multiply(zp,sp)
    s = sumation(psk,fs)
    d =demod1(s,h)
    return d

def dmodASK(za ,fs, fn,h): # demodulacja ASK
    sa = [(1 * np.sin(2 * np.pi * fn * b / fs)) for b in range(700)]
    ask = np.multiply(za,sa)
    s = sumation(ask,fs)
    d =demod1(s,h)
    return d

def dmodFSK(zf ,fs,N,tb,h): # demodulacja FSK
    fn1 = (N + 1) / tb
    fn2 = (N + 2) / tb
    sn1 = [np.sin(2 * np.pi * fn1 * b / fs) for b in range(700)]
    sn2 = [np.sin(2 * np.pi * fn2 * b / fs) for b in range(700)]
    xt1 = np.multiply(zf, sn1)
    xt2 = np.multiply(zf, sn2)
    px1 = sumation(xt1,fs)
    px2 = sumation(xt2,fs)
    pt = px1 + px2
    d = demod1(pt, h)
    return d

def check(a,b): # policzenie BER sprawdzam kazdy bit dwoch wiadomosci jesli jest roznica to dodaje 1 do listy potem sunuje i dziele przez ilosc bitow
    c = []
    for i in range(4):
        if a[i] != b[i]:
            c.append(1)
    return sum(c)/4

