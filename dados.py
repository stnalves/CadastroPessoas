from mensagens import *

def nome():
    while True:
        n = str(input('Nome: ')).strip().title()
        if all(palavra.isalpha() for palavra in n.split()):
            return n
        else:
            erro('ERRO AO CADASTRAR O NOME')
            
def idade():
    while True:
        try:
            num = int(input('Idade: '))
            return num
        except (ValueError, TypeError):
            erro('ERRO! Por favor, digite uma idade válida.')
        except KeyboardInterrupt:
            erro('Entrada de idade cancelada pelo usuário.')
            return 0
