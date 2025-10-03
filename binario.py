# Pegar um número inteiro positivo e transformar na forma binária
# loop dividindo o número por 2 e adicionando o resultado a uma string(lista?)

def binario(num):
    """ Essa função pega um número inteiro positivo e transforma em binário """
    string_num = ''
    while num > 0:
        if num % 2 == 0:
            string_num = '0' + string_num
        else:
            string_num = '1' + string_num
        num = num//2
    return string_num
print(binario(37))