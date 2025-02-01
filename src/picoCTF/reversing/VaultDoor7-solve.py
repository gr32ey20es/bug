def intToBytes(x):
    return [
        x >> 24,
        (x % (1 << 24)) >> 16,
        (x % (1 << 16)) >> 8,
        x % (1 << 8)
    ]

def intToString(x):
    return [chr(y) for y in intToBytes(x)]

arr = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293296, 842413104, 1684157793]

print(''.join([''.join(intToString(x)) for x in arr]))
