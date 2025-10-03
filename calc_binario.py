# Pegar um número inteiro positivo e transformar na forma binária
# loop dividindo o número por 2 e adicionando o resultado a uma string(lista?)

def binario(num):
    """ Essa função pega um número inteiro positivo e transforma em binário """
    string_num = ' '
    while num > 0:
        string_num = str(num%2) + ' ' + string_num
        num = num//2
    return string_num

valor = int(input('Digite o valor a transformar: '))
print(f'{valor} em binário é:')
print('-'*20)
print(binario(valor))
print('-'*20)