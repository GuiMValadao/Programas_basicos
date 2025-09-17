#------------------------------------------------------------
# Jogo de adivinhção - agora usando funções
#------------------------------------------------------------
import random

jogo = True
adivinhacao = 0
def replay():
    """Função para iniciar/reiniciar o jogo."""
    global jogo
    x = False
    while not x:
        if jogo == 's':
            jogo = True
            x = True
            return jogo
        elif jogo == 'n':
            jogo = False
            x = True
            return jogo
        else:
            jogo = input('Escolha "s" para jogar e "n" para sair.')
            x = False
        
def inicio(i = 0):
    """Função para iniciar/reiniciar o jogo."""
    global jogo
    if i == 0:
        i += 1
        print('-'*50)
        print('Bem-vindo ao jogo de adivinhação de números!')
        print('-'*50)
        jogo = str(input('Quer jogar? (s/n)' ))
        comecar = replay()
        return comecar, i
    else:
        i += 1
        jogo = str(input('Quer jogar novamente? (s/n) '))
        comecar = replay()
        return comecar, i
    
def tentativa(resposta):
    """Função para obter input do usuário."""
    global adivinhacao
    adivinhacao = input('Dê seu palpite entre 1 e 20: ')
    chec_num()
    if adivinhacao == '-1':
        adivinhacao = cheat(resposta)
    return adivinhacao

def chec_num():
    """Função para garantir que foi inserido um número e que ele está entre 0 e 21."""
    global adivinhacao
    while not((adivinhacao.isnumeric() and
                0 < int(adivinhacao) <= 20) or
        adivinhacao == '-1'):
        adivinhacao = input('Por favor, insira um numero inteiro de 1 a 20: ')
    return adivinhacao

def cheat(resposta):
    """Para roubar, obtendo a resposta sem perder uma chance."""
    global  adivinhacao
    if adivinhacao == '-1':
        print('o numero correto e ', resposta)
        adivinhacao = input('Dê seu palpite entre 1 e 20: ')
        chec_num()
        cheat(resposta)
        return adivinhacao
    return None

def vitoria(resposta, chances, guess):
    """Função que verifica se o usuário acertou."""
    if guess == resposta:
        print('Parabéns! Você acertou!')
        print('Você precisou de', 5 - chances,
              'tentativas para vencer!')
        print('-'*50)
        return True
    else:
        return False
    
def errado(chances, teste2, resposta):
    """Função que verifica se o usuário errou."""
    chances -= 1
    if chances == 0:
        print('Que pena, você perdeu... ')
        print('O número correto era ', resposta)
        return chances
    elif ((teste2 == resposta - 1) or
          (teste2 == resposta + 1)):
        print('Errado. Sua adivinhação passou perto.')
        return chances
    elif teste2 < resposta:
        print('Errado. Tente um número maior.')
        return chances
    else:
        print('Errado. Tente um número menor.')
    return chances

def loop_jogo():
    """Função definindo o loop principal do jogo"""
    global jogo
    jogo = inicio()[0]
    while jogo == True:

        resposta = random.randint(1, 20)
        chances = 4

        # Permite ao usuario tentar novamente até ficar sem chances
        while chances > 0:
            guess = int(tentativa(resposta))

            # Verifica se o jogador adivinhou corretamente.
            if not vitoria(resposta, chances, guess):
                chances = errado(chances, guess, resposta)
                print('-'*50)
            else:
                break
        jogo = inicio(1)[0]

# Código rodando o jogo
loop_jogo()
print('-'*50)
print('Fim de jogo.')