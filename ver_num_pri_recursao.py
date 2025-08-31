#----------------------------------------------
# Verificador de números primos usando recursão
#----------------------------------------------
# Se o número for primo e maior que 1999 resulta
# em erro

import time     # Importa o módulo 'time' para medir o tempo do script

# Função recursiva que determina se um número é
# primo ou não.
def primo_calc(n, num = 2):
    if n%num != 0:
        if num + 1 < n/2:
            return primo_calc(n,num + 1)
        else:
            return 'Sim.'
    else:
        return 'Não.'

x = int(input('Insira o número para descobrir se é primo: '))

inicio = time.perf_counter()        # Inicia a contagem do tempo do script

print('O número', x, 'é primo?', primo_calc(x))

fim = time.perf_counter()           # Termina a contagem do tempo do script
print(f"O tempo de execuçao foi: {fim - inicio} segundos")
