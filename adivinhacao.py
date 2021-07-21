import random

print('____________________________________')
print('|                                  |')
print('| Bem vindo ao Jogo de Adivinhação |')
print('|__________________________________|\n')

numero_secreto = random.randrange(1,101) #gera numero entre 0.0 1.0
total_de_tentativas = 0
pontos = 1000

print('Escolha o nivel da dificuldade:')
print('(1)Fácil (2)Médio (3)Dificil')

nivel = int(input("Defina o nivel!"))

if (nivel == 1):
        total_de_tentativas = 20
elif(nivel == 2):
        total_de_tentativas = 10
else:
        total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute >100 ):
        print('Você deve digitar um numero entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Acertô miseravi! Você fez {} pontos!".format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    if(maior):
        print('O seu número foi maior que o número secreto.')
    if(rodada == total_de_tentativas):
            print("O número secreto era {} e você fez {} pontos!".format(numero_secreto, pontos))
    elif(menor):
            print("O seu chute foi menor do que o número secreto!")
    if(rodada == total_de_tentativas):
            print('O numero secreto era {}. Você conseguiu {} pontos!'.format(numero_secreto, pontos))

print("Fim do jogo !")