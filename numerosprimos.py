# Pedir o alcance desejado ao usuario
alcance = input('Digite o número máximo a verificar: ')
# Loop para garantir que é número positivo e inteiro
if alcance.isnumeric():
    alcance = int(alcance)      # Definir alcance como número fixo
    # Loop para garantir que o alcance é maior que 2
    if 2 < alcance:
        # Loop variando o número i, que procuramos saber se é primo
        for i in range(2,alcance+1):
            # Loop para variar o número j que é o denominador.
            for j in range (2,i+1):         # Colocar o máximo de j em i+1 permite
                if i%j == 0 and i != 2:     # obter 2 como número primo.
                    break
                else:
                    j += 1                  # Isso faz que j varie e que j máximo seja
                    if j == i or i == 2:    # igual ao i a cada loop em i.
                        print(i, end=' ')
            i += 1
        print('')
    else:
        print('Erro, o alcance deve ser maior que dois')    # Erro por inserir 1 ou negativos.
else:
    print('Erro, insira um número inteiro.')                # Erro por inserir letras ou floats.
