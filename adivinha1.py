#-----------------------------------------------------
# ADIVINHA - PSEUDOCÓDIGO
# Iniciar um loop para permitir jogar novamente.
    # Gerar um números aleatório para ser adivinhado.
    # Iniciar loop do jogo:
        # Pedir input do usuário para adivinhar o número.
        # Permitir que o usuário roube, obtendo a resposta
        # sem perder uma chance ao digitar '-1'.
        # Comparar o input com o número aleatório gerado.
            # Se o input é '-1', retorna a resposta certa para
            # o usuário e pede nova adivinhação sem perder uma chance.
            # Se o input e número gerado forem iguais, usuário venceu.
            # Caso contrário, usuário errou.
                # Se chances = 0, usuário perdeu.
                # Se não, comparar se o número adivinhado é
                # menor ou maior ou +-1 e dizer ao usuário.
                # Retornar ao início para pedir novo input
                # e diminuir número de chances em 1.
    # Perguntar se o usuário quer jogar novamente.
        # Se sim ('s'), retornar 'chances' para 4 e sortear novo número.
        # Se não, terminar o loop e seguir para o fim do programa.
# Exibe 'Fim de jogo.' (Fim do programa).
#---------------------------------------------------------------
# CÓDIGO
# Importa a biblioteca 'random', que gera números em uma sequência pseudo-aleatória.
import random

jogo = True

# Inicia primeiro um loop que permite novo jogo
while jogo == True:
    print('Bem-vindo ao jogo de adivinhação de números!')
    print('Você tem 4 chances para adivinhar.')
    resposta = random.randint(1, 20)
    chances = 4
    # Inicia o loop para adivinhação
    while chances > 0:
        adivinhacao = int(input('Dê seu palpite entre 1 e 20: '))
        # Para roubar, obtendo a resposta sem perder uma chance
        if adivinhacao == -1:
            print('O número correto é ', resposta)
        # Verifica se o jogador adivinhou corretamente.
        elif adivinhacao == resposta:
            print('Parabéns! Você acertou!')
            print('Você precisou de', 5 - chances,
                  'tentativas para vencer!')
            break
        # Se o usuario errou a adivinhação, remove uma chance
        # e se chances = 0, informa que o usuário perdeu e qual a
        # resposta correta:
        else:
            chances -= 1
            print('Você tem {} chances restantes.'.format(chances))
            if chances == 0:
                print('Que pena, você perdeu... ')
                print('O número correto era ', resposta)
                break
            elif ((adivinhacao == resposta - 1) or
                  (adivinhacao == resposta + 1)):
                print('Errado. Sua adivinhação passou perto.')
            elif adivinhacao < resposta:
                print('Errado. Tente um número maior.')
            else:
                print('Errado. Tente um número menor.')

    # Pergunta se o usuário que jogar novamente.
    # Recomeça o jogo apenas se o usuário retornar 's'.
    jogo = input('Quer jogar novamente?(s/n) ')     # Note que 'jogo' era Booleano, aqui 
    if jogo == 's':                                 # torna-se String, e na sequência  
        jogo = True                                 # Booleano novamente
    else:
        jogo  = False

print('Fim de jogo.')

