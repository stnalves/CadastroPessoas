from mensagens import *

def nome():
    while True:
        try:
            n = str(input('Nome: ')).strip().title()
            if n and all(palavra.isalpha() for palavra in n.split()):
                return n
            else:
                erro('ERRO AO CADASTRAR O NOME')
        except KeyboardInterrupt:
            erro('\nEntrada de nome cancelada pelo usuário')
            
def idade():
    while True:
        try:
            num = int(input('Idade: '))
            return num
        except (ValueError, TypeError):
            erro('ERRO! Por favor, digite uma idade válida.')
        except KeyboardInterrupt:
            erro('\nEntrada de idade cancelada pelo usuário.')
            return None
