vermelho = '\033[31m'
amarelo = '\033[33m'
azul = '\033[34m'
limpar = '\033[m'


def idade():
    try:
        age = int(input('Idade: '))
        return age
    except (TypeError, ValueError):
        return 0


def menu(msg=''):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


def cadastro(file, nome, idade):
    arquivo = open(file, 'a')
    arquivo.write(f'{nome:<47}{idade}\n')
    arquivo.close()


def printlist(file):
    menu('PESSOAS CADASTRADAS')
    arquivo = open(file)
    for line in arquivo.readlines():
        print(line, end='')
    arquivo.close()


def opcao():
    try:
        opc = int(input(f'{amarelo}Sua opção: {limpar}'))
        return opc
    except (TypeError, ValueError):
        return 0
