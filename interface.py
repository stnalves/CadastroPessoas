from dados import *
from arquivo import *
from mensagens import *
from time import sleep


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c, item in enumerate(lista, 1):
        print(f'{cor[3]}{c} - {cor[4]}{item}{cor[0]}')
    print('-'*40)
    sleep(2)

def opcao(lista):
    def cadastro():
        cabecalho('CADASTRANDO PESSOA')
        n = nome()
        i = idade()
        adicionar([[n, i]])

    acoes = [ler, cadastro, exit]

    while True:
        menu(lista)
        try:
            op = int(input(f'{cor[5]}Sua opção: {cor[0]}'))
            if 1 <= op < len(acoes):
                acoes[op - 1]()
            elif op == len(acoes):
                cabecalho('< FIM DO PROGRAMA >')
                acoes[op - 1]()
            else:
                erro('ERRO! Digite uma opção válida.')
        except (ValueError, TypeError):
            erro('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            erro('Entrada cancelada pelo usuário.')
            break
        sleep(2)
