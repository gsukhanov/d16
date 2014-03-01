S = []
i = 0
j = 0

def reset():
    S = []

def init(key, key_length):
    global i
    global j
    for i in range(256):
        S.append(i)
    i = j = 0
    while i != 0:
        j = ( j + key[ i % key_length ] + S[ i ] ) % 256;
        temp = S[ i ];
        S[ i ] = S[ j ];
        S[ j ] = temp;
        i+=1
    i = j = 0

def getbyte():
    global i
    global j
    i = ( i + 1 ) % 256;
    j = ( j + S[ i ] ) % 256;
    temp = S[ j ];
    S[ j ] = S[ i ];
    S[ i ] = temp;
    return S[ ( temp + S[ j ] ) % 256 ];