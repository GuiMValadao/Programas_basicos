# Pede um número inteiro ao usuário
num = input('Insira o valor a ser obtido o fatorial: ')
# Loop para checar se é inteiro:
if num.isnumeric():
    num_int =  int(num)
    fat = int(num)
    # Checa se o número é zero. Se for, então o fatorial é 1.
    if num_int == 0:
        fat = 1
    else:
        # Se o número não é zero, procede para calcular o fatorial
        while num_int > 2:                      # Como o fatorial vai estar multiplicando o número atual
            fat = fat*(num_int-1)               # pelo atual menos 1 só precisamos calcular até num_int == 3,
            num_int -= 1                        # ou num_int > 2
    print ('O fatorial de ', int(num), 'é ', fat)
else:
    print('Erro!! Insira um número inteiro.')
