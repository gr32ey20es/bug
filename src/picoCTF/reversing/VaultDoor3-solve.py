ctf = 'jU5t_a_sna_3lpm18gb41_u_4_mfr340'
pas = ['' for i in range(32)]

for i in range(8):
    pas[i] = ctf[i]

for i in range(8, 16):
    pas[23-i] = ctf[i]

for i in range(16, 32, 2):
    pas[46-i] = ctf[i]

for i in range(17, 32, 2):
    pas[i] = ctf[i]

print(''.join(pas))
