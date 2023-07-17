from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' SUas Opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a Sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador Jogou {}' .format(itens[computador]))
print('Jogador Jogou {}' .format(itens[jogador]))
print('-=' * 11) 
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Inválida')            
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')

    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Inválida')        

elif computador == 2: 
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Inválida')        