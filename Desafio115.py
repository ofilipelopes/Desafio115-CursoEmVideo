from Desafio115.modulo import *

try:
    lista = open('lista.txt')
    lista.close()
except FileNotFoundError:
    lista = open('lista.txt', 'w')
    lista.write(f'{"NOME":<45}{"IDADE"}\n')
    lista.close()

while True:
    menu('MENU PRINCIPAL')
    print(f'{amarelo}1{limpar} - {azul}Ver pessoas cadastradas{limpar}')
    print(f'{amarelo}2{limpar} - {azul}Cadastrar nova pessoa{limpar}')
    print(f'{amarelo}3{limpar} - {azul}Sair do sistema{limpar}')
    print('-' * 50)
    opc = opcao()
    while opc not in [1, 2, 3]:
        print(f'{vermelho}Opção inválida! Por favor, digite um número inteiro entre 1 e 3.{limpar}')
        opc = opcao()
    if opc == 1:
        printlist('lista.txt')
    elif opc == 2:
        try:    
            name = input('Nome: ').strip()
            while not name.replace(' ', '').isalpha():
                print(f'{vermelho}Nome inválido! São permitidos apenas letras e espaços.{limpar}')
                name = input('Nome: ').strip()
            age = idade()
            while age == 0:
                print(f'{vermelho}Idade inválida! Por favor digite um número inteiro maior que 0.{limpar}')
                age = idade()
        except KeyboardInterrupt:
            print(f'\n{vermelho}Dados não preenchidos!{limpar}')
            continue
        print(f'Novo registro de {name} adicionado.')
        cadastro('lista.txt', name, age)
    else:
        break
menu('Saindo do sistema... Até logo!')
