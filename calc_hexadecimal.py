# Pegar um número inteiro positivo e transformar na forma binária
# loop dividindo o número por 2 e adicionando o resultado a uma string(lista?)

def hexadecimal(num):
    """ Essa função pega um número inteiro positivo e transforma em hexadecimal """
    string_num = ''
    transf = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while num > 0:
        if num%16<10:
            string_num = str(num%16) + ' ' + string_num
        else:
            string_num = str(transf[num%16]) + ' ' + string_num
        num = num//16
    return string_num

valor = int(input('Digite o valor a transformar: '))
print(f'{valor} em hexadecimal é:')
print('-'*20)
print(hexadecimal(valor))
print('-'*20)