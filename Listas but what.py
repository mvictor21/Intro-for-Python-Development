from random import choice
nome = input('Escreva o nome de um filme: \n')
if(len(nome) < 3):
    print('Done')
else:
    lista = nome.split()
    c = int(1)
    while(c < 3):
        s = choice(lista)
        c = len(s)
    print(nome.replace(s,'Done'))