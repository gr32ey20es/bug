bytes = [
	106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
	0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
	0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o143, 0o61,
	'9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
]

length = len(bytes)

ctf = \
    [chr(bytes[i]) for i in range(0, 3*length//4)] + \
    [bytes[i] for i in range(3*length//4, length)]
print(''.join(ctf))
