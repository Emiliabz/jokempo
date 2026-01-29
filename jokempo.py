#Jogo pedra, papel e tesoura

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Vem jogar Jokempo comigo!')
print('-=-'*20)
print('''Suas opcoes:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual eh a sua jogada? '))

print('-='*20)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!')
sleep(1)
print('-='*20)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-'*20)

if jogador == computador:
    print('EMPATE!')
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print('JOGADOR VENCEU!')
else:
    print('COMPUTADOR VENCEU!')
