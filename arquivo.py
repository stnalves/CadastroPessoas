from mensagens import *

def adicionar(lista, nome_arq='dados.txt'):
    with open(nome_arq, 'a', encoding='utf-8') as arquivo:
        for pessoa in lista:
            nome, idade = pessoa
            arquivo.write(f'{nome}, {idade}\n')

def ler(nome_arq='dados.txt'):
    cabecalho('PESSOAS CADASTRADAS')
    try:
        with open(nome_arq, 'r', encoding='utf-8') as arquivo:
            for pessoa in arquivo:
                nome, idade = pessoa.strip().split(', ')
                print(f'{nome:<30}{idade:>5} anos')
    except FileNotFoundError:
        erro('Nenhuma pessoa foi cadastrada anteriormente.')
