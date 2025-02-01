file = open("enc", 'r')
line = file.readline()

for word in line:
    hlchr = ord(word)
    hchr = hlchr >> 8
    lchr = hlchr % (1 << 8)

    print(chr(hchr), end='')
    print(chr(lchr), end='')

