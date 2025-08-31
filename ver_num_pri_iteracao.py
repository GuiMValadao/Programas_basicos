#----------------------------------------------
# Verificador de números primos usando iteração
#----------------------------------------------
# Limite não observado (pelo menos 49999)

import time

# Pedir o alcance desejado ao usuário
primo = int(input('Digite o número a verificar: '))
inicio = time.perf_counter()
j = 0           # Variavel para verificar se todas as divisões foram feitas

for i in range(2,(primo+1)//2):
    if primo%i == 0:
        print(primo, 'Não é número primo')
        break
    else:
        j +=1
if j == (primo-2)//2:
    print(primo, 'é primo')
fim = time.perf_counter()
print(f"O tempo de execução foi: {fim - inicio} segundos")
