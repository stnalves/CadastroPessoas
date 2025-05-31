cor = ('\033[m' ,   # 0 limpa
         '\033[31m' , # 1 vermelho
         '\033[32m' , # 2 verde
         '\033[33m' , # 3 amarelo
         '\033[34m' , # 4 azul
         '\033[36m'   # 5 ciano
         )

def erro(msg):
    print(f'{cor[1]}{msg}{cor[0]}')

def cabecalho(msg):
    print('-'*40)
    print(f'{cor[2]}{msg:^40}{cor[0]}')
    print('-'*40)
