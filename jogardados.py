# Importa o módulo random
import random       
# Define os valores limites do dado
MIN = 1             
MAX = 6
# Define a variável para jogar novamente ou parar de jogar.
roll_again = 'y'    
# Loop para jogar dois dados
while roll_again == 'y':
    print('Lançando os dados...')
    print('Os valores sao:')
    # Sorteia um número inteiro aleatório.
    dado1 = random.randint(MIN, MAX)    
    print(dado1)
    dado2 = random.randint(MIN, MAX)
    print(dado2)
    # Pergunta para jogar novamente ou parar o programa.
    roll_again = input('Jogar os dados novamente? (y/n): ')
