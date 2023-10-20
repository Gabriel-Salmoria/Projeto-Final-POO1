# Trabalho final - Gabriel Salmoria

from verif import verifica_s_n
from arq_clientes import dict_clientes
from arq_funcionario import dict_funcionarios
from arq_loja import Mercearia


while True:
    x = input('\n\n\n\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nColoque seu ID aqui:')
    while x not in dict_clientes and x not in dict_funcionarios and x != 'Admin':
        x = input('Erro. Coloque seu ID aqui:')
        
    if x == 'Admin':
        x = Mercearia
        print(f'\n\n\n\n-=-=-=--=-=-=-=-=-=-=-=\n\nBem Vindo, Admin!')
        x.escolha()
            
    elif x in dict_clientes:
        x = dict_clientes[x]
        print(f'\n\n\n\n-=-=-=--=-=-=-=-=-=-=-=\n\nBem Vindo {x.nome_comp}!')
        x.escolha()

    elif x in dict_funcionarios:
        x = dict_funcionarios[x]
        print(f'\n\n\n\n-=-=-=--=-=-=-=-=-=-=-=\n\nBem Vindo {x.nome_comp}!')
        x.escolha()

    a = input('\nDeseja escolher outro usuário? (s/n)\nInsira sua escolha:')
    a = verifica_s_n(a)
    
    if a == 'n' or a == 'N':
        break

