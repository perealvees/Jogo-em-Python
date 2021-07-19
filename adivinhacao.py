print('____________________________________')
print('|                                  |')
print('| Bem vindo ao Jogo de Adivinhação |')
print('|__________________________________|\n')

numero_secreto = 42

chute_str = input('Digite um número: ')
print('Você digitou', chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print('Acertô miseravi!')
else:
    if(chute > numero_secreto):
        print('Você errou! Seu chute foi maior que o número secreto.')
    elif(chute < numero_secreto):
        print('Você errou! Seu chute foi menor que o número secreto.')

print('Fim de jogo')