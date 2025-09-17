######################################
# JOGO DE PEDRA, PAPEL OU TESOURA
######################################

print('#'*50)
print('#--Bem vindo ao jogo de pedra, papel, tesoura!--#')
print('#'*50)

# Variáveis para permitir jogar/reiniciar sem precisar executar o programa novamente.
jogo = input('Quer jogar?(s/n): ')
x = False

# Loop para iniciar o jogo ou sair. É repetido posteriormente, pode ser transformado em uma função.
while not x:
    if jogo == 'n':
        jogo = False
        x = True        
    elif jogo == 's':
        jogo = True
        x = True
    else:
        jogo = input('Quer jogar? Digite s ou n: ')

# Loop principal do jogo
while jogo:        
    opcoes = ('pedra', 'papel', 'tesoura')
    print(f'Escolha entre {opcoes}')
    
    # Pedir de entrada duas variáveis para dois jogadores e normaliza. Poderia ser outra função
    escolha_jogador1 = input('Jogador 1 deve escolher: ')
    escolha_jogador2 = input('Jogador 2 deve escolher: ')
    print('-'*40)
    
    escolha_jogador1 = escolha_jogador1.lower().strip( )
    escolha_jogador2 = escolha_jogador2.lower().strip( )
    
    # Garante que as entradas estão nas opções.
    while (escolha_jogador1 and escolha_jogador2) not in opcoes:
        print('Uma das escolhas foi inválidas! Digite "pedra", "papel" ou "tesoura"')
        escolha_jogador1 = input('Jogador 1 deve escolher: ')
        escolha_jogador2 = input('Jogador 2 deve escolher: ')    
    
    # Compara as respostas e identifica o ganhador.
    if escolha_jogador1 == escolha_jogador2:
        print('&'*20)
        print('Empate!')
        print('&'*20)
        
    elif ((escolha_jogador1 == 'pedra' and escolha_jogador2 == 'tesoura') or
        (escolha_jogador1 == 'tesoura' and escolha_jogador2 == 'papel') or
        (escolha_jogador1 == 'papel' and escolha_jogador2 == 'pedra')):
        print('1!'*20)
        print('Jogador 1 venceu!')
        print('1!'*20)
        
    else:
        print('2!'*20)
        print('Jogador 2 venceu!')
        print('2!'*20)
    
    print('-'*40)
    print(f'Jogador 1 escolheu {escolha_jogador1}')
    print(f'Jogador 2 escolheu {escolha_jogador2}')
        
    # Repetição da seção. Transformar em função simplificaria e tornaria mais elegante.
    jogo = input('Quer jogar novamente?(s/n)')
    x = False
    while not x:
        if jogo == 'n':
            jogo = False
            x = True        
        elif jogo == 's':
            jogo = True
            x = True
        else:
            jogo = input('Quer jogar? Digite s ou n): ')
print('-'*40)            
print('Até a próxima!')