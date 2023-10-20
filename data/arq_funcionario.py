# Trabalho final - Gabriel Salmoria

import verif
from arq_prod import dict_produtos
from arq_clientes import dict_clientes

dict_funcionarios = {}
lista_funcionarios = []

class Funcionario:
    def __init__(self, nome_comp, cpf, funcao, salario, tempo_empresa):
        self.cpf = cpf
        self.nome_comp = nome_comp
        self.funcao = funcao
        self.salario = salario
        self.tempo_empresa = tempo_empresa

    def get_info(self):
        print(f'\nFuncionário: {self.nome_comp}\nCPF: {self.cpf}\nFunção: {self.funcao}\nSalário: {self.salario}\nTempo na empresa: {self.tempo_empresa} Meses')

    def set_cpf(self):
        print(f'CPF atual: {self.cpf}')
        cpf = input('Informe o novo CPF:')
        cpf = verif.verifica_cpf(cpf)
        self.cpf = cpf
        print(f'CPF atualizado! Seu CPF atual é: {self.cpf}')
    
    def set_nome_comp(self):
        print(f'Nome atual: {self.nome_comp}')
        nome_comp = input('Informe o novo nome completo:')
        while nome_comp in dict_clientes or  nome_comp in dict_funcionarios or nome_comp in dict_produtos:
            nome_comp = input('Nome já utilizado. Digite o novo nome completo:')
            
        for key in dict_funcionarios:
            if dict_funcionarios[key] == self:
               x = key
                               
        self.nome_comp = nome_comp
        dict_funcionarios[nome_comp] = dict_funcionarios.pop(x)
        print(f'Nome atualizado! Seu nome atual é: {self.nome_comp}')
    
    def set_funcao(self):
        print(f'\nFunção atual: {self.funcao}\n')
        funcao = input('Escolha a sua nova função.\n1. Atendente\n2. Zelador\n3. Ajudante\nInsira sua escolha:')
        funcao = verif.verifica_escolha(funcao,3)
        if funcao == 1:
            funcao = 'Atendente'
        elif funcao == 2:
            funcao = 'Zelador'
        else:
            funcao = 'Ajudante'
        self.funcao = funcao
        
    def set_tempo_empresa(self):
        print(f'Tempo de empresa atual: {self.tempo_empresa}')
        tempo_empresa = input('Coloque o tempo de empresa atualizado:')
        tempo_empresa = verif.verifica_cadastro(tempo_empresa)
        self.tempo_empresa = tempo_empresa
        
    def escolha(self):
        from arq_loja import Mercearia
        while True:
            print(f'\nSelecione o que deseja fazer:')
            print('\n1. Acessar suas informações\n2. Alterar uma de suas informações\n3. Ver os produtos\n4. Adicionar um produto\n5. Excluir um produto específico\n6. Sair de sua conta')
            x = input('\nEscreva sua escolha:')
            x = verif.verifica_escolha(x,6)
            if x == 1:
                self.get_info()
            elif x == 2:
                print(f'\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nSelecione o que deseja fazer:')
                print('\n1. Alterar CPF\n2. Alterar nome\n3. Alterar função\n4. Voltar ao menu anterior')
                y = input('\nInsira sua escolha:')
                y = verif.verifica_escolha(y,4)
                if y == 1:
                    self.set_cpf()
                elif y == 2:
                    self.set_nome_comp()
                elif y == 3:
                    self.set_funcao()
                elif y == 4:
                    continue
            elif x == 3:
                Mercearia.get_estoque()
            elif x == 4:
                Mercearia.add_produto()
            elif x == 5:
                Mercearia.excluir_produto()
            elif x == 6:
                break
                
            a = input('\nDeseja continuar em seu menu? (s/n):')
            a = verif.verifica_s_n(a)
            if a == 'n' or a == 'N':
                break  
            
x = Funcionario('Jonas da Silva', 33333333333, 'Atendente', 2000, 5)
dict_funcionarios['Jonas da Silva'] = x
lista_funcionarios.append(x)