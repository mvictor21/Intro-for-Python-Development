nc = str(input('Digite seu nome e sobrenome: '))
div = nc.split()
sn = ' '.join(div[1:])
print('Olá {}! Achei seu sobrenome {} muito bonito!'.format(div[0], sn))