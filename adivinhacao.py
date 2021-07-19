print('____________________________________')
print('|                                  |')
print('| Bem vindo ao Jogo de Adivinhação |')
print('|__________________________________|\n')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

  while (total_de_tentativas > 0):
    print('Tentativa:', total_de_tentativas)
    chute_str = input('Digite um número: ')
    print('Você digitou:', chute_str,'.')
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if(acertou):
        print('Acertô miseravi!')
    else:
        if(maior):
            print('Você errou! Seu chute foi maior que o número secreto.')
        elif(menor):
            print('Você errou! Seu chute foi menor que o número secreto.')

    total_de_tentativas = total_de_tentativas -1


print('Fim de jogo')