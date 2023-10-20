# Trabalho final - Gabriel Salmoria

import verif
from arq_prod import Produto,dict_produtos,lista_produtos
from arq_clientes import Cliente, Cliente_vip, dict_clientes,lista_clientes,lista_clientes_vip
from arq_funcionario import Funcionario, dict_funcionarios,lista_funcionarios

class Loja:
    def __init__(self, lista_produtos, lista_funcionarios, lista_clientes,lista_clientes_vip, caixa):
        self.lista_produtos = lista_produtos
        self.lista_funcionarios = lista_funcionarios
        self.lista_clientes = lista_clientes
        self.lista_clientes_vip = lista_clientes_vip
        self.caixa = caixa

    def get_estoque(self):
        for i in self.lista_produtos:
            i.get_info()
        
    def get_lista_clientes(self):
        for i in self.lista_clientes:
            i.get_info(),'\n'
        for i in self.lista_clientes_vip:
            i.get_info(),'\n'
        
    def get_lista_funcionarios(self):
        for i in self.lista_funcionarios:
            i.get_info(),'\n'
    
    def add_cliente(self):
        cpf1 = input('\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nDigite o CPF do cliente:')
        cpf1 = verif.verifica_cpf(cpf1)
        nome_comp1 = input('Digite o nome do cliente:')
        while nome_comp1 in dict_clientes or  nome_comp1 in dict_funcionarios or nome_comp1 in dict_produtos:
            nome_comp1 = input('Nome já utilizado. Digite o nome do cliente:')    
        x = nome_comp1
        
        num_cadastro1 = input('Digite o cadastro do cliente:')
        num_cadastro1 = verif.verifica_cadastro(num_cadastro1)
        credito1 = input('Digite seu crédito inicial:')
        credito1 = verif.verifica_credito(credito1)

        tipo = input('\nSeu cliente será:\n1. Cliente Normal\n2. Cliente VIP\nDigite sua escolha:')
        tipo = verif.verifica_escolha(tipo,2)
        if tipo == 1:
            nome_comp1 = Cliente(cpf1, nome_comp1,num_cadastro1,credito1)
            dict_clientes[x] = nome_comp1
            self.lista_clientes.append(nome_comp1)

        elif tipo == 2:
            telefone1 = input('Digite o telefone do cliente:')
            telefone1 = verif.verifica_telefone(telefone1)
            endereco1 = input('Digite o endereço do cliente:')
            desconto1 = input('Digite o desconto (em %) que o cliente recebe nas compras:')
            desconto1 = verif.verifica_desconto(desconto1)
            
            nome_comp1 = Cliente_vip(cpf1,nome_comp1,num_cadastro1,credito1,telefone1,endereco1,desconto1)
            dict_clientes[x] = nome_comp1
            self.lista_clientes_vip.append(nome_comp1)
        
    def add_funcionario(self):
        nome_comp1 = input('\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nDigite o nome do funcionário:')
        while nome_comp1 in dict_clientes or  nome_comp1 in dict_funcionarios or nome_comp1 in dict_produtos:
            nome_comp1 = input('Nome já utilizado. Digite o nome do funcionário:')
            
        x = nome_comp1
        
        cpf1 = input('Digite o CPF do funcionário:')
        cpf1 = verif.verifica_cpf(cpf1)

        funcao = input('Escolha a função do seu funcionário.\n1. Atendente\n2. Zelador\n3. Ajudante\nInsira sua escolha:')
        funcao = verif.verifica_escolha(funcao,3)
        if funcao == 1:
            funcao = 'Atendente'
        elif funcao == 2:
            funcao = 'Zelador'
        else:
            funcao = 'Ajudante'
    
        salario = input('Digite o salário do funcionário:')
        salario = verif.verifica_credito(salario)
        
        tempo_empresa = input('Digite o tempo de empresa do funcionário:')
        tempo_empresa = verif.verifica_credito(tempo_empresa)

        nome_comp1 = Funcionario(nome_comp1,cpf1,funcao,salario,tempo_empresa)
        
        dict_funcionarios[x] = nome_comp1
        self.lista_funcionarios.append(nome_comp1)

    def excluir_cliente(self):
        x = input('Insira o cliente que deseja excluir:')
        while x not in dict_clientes:
            x = input('Erro. Insira o funcionário que deseja excluir:')    
        y = dict_clientes[x]
        del dict_clientes[x]
        if y in self.lista_clientes:
            self.lista_clientes.remove(y)
        elif y in self.lista_clientes_vip:
            self.lista_clientes_vip.remove(y)
                
    def excluir_funcionario(self):
        x = input('Insira o funcionário que deseja excluir:')
        while x not in dict_funcionarios:
            x = input('Erro. Insira o funcionário que deseja excluir:')    
        y = dict_funcionarios[x]
        del dict_funcionarios[x]
        self.lista_funcionarios.remove(y)
        
    def excluir_produto(self):
        x = input('Insira o produto que deseja excluir:')
        while x not in dict_produtos:
            x = input('Erro. Insira o produto que deseja excluir:')    
        y = dict_produtos[x]
        del dict_produtos[x]
        self.lista_produtos.remove(y)
            
    def add_produto(self):
        nome1 = input('Coloque o nome do produto:')
        x = nome1
        while nome1 in dict_clientes or  nome1 in dict_funcionarios or nome1 in dict_produtos:
            nome1 = input('Nome já utilizado. Digite o nome do produto:')
            
        preco1 = input('Coloque o preço do produto:')
        preco1 = verif.verifica_credito(preco1)
        cat = input('Coloque a categoria desse item:\n1. Brinquedo\n2. Papelaria\n3. Bijuteria\nInsira sua escolha:')
        cat = verif.verifica_escolha(cat,3)
        if cat == 1:
            cat = 'Brinquedo'
        elif cat == 2:
            cat = 'Papelaria'
        else:
            cat = 'Bijuteria'
        qtd = input('Coloque a quantidade desse produto no estoque:')
        qtd = verif.verifica_quantidade(qtd)
        nome1 = Produto(nome1,preco1,cat,qtd)
        dict_produtos[x] = nome1
        self.lista_produtos.append(nome1)
    
    def set_salario(self):
        x = input('Insira o funcionário para fornecer um aumento:')
        while x  not in dict_funcionarios:
            x = input('Erro. Insira o funcionário para fornecer um aumento:')
        x = dict_funcionarios[x]

        print(f'\nSalário atual do funcionario {x.nome_comp}: R${x.salario}\n')

        salario = input('Coloque o novo salário do funcionário:')
        salario = verif.verifica_credito(salario)
        x.salario = salario

    def get_caixa(self):
        print(f'\nDinheiro em caixa: R${self.caixa}')

    def escolha(self):
        while True:
            print(f'\nSelecione o que deseja fazer:')
            print('\n1. Acessar o estoque\n2. Acessar a lista de clientes\n3. Acessar a lista de funcionários\n4. Adicionar um cliente\n5. Excluir um cliente específico\n6. Adicionar um funcionário\n7. Excluir um funcionário específico\n8. Adicionar produto\n9. Excluir um produto específico\n10. Alterar salário de funcionário específico\n11. Ver dinheiro em caixa\n12. Alterar informações sobre um produto\n13. Sair do login')
            x = int(input('\nEscreva sua escolha:'))
            x = verif.verifica_escolha(x,13)
            if x == 1:
                self.get_estoque()
            elif x == 2:
                self.get_lista_clientes()
            elif x == 3:
                self.get_lista_funcionarios()
            elif x == 4:
                self.add_cliente()
            elif x == 5:
                self.excluir_cliente()
            elif x == 6:
                self.add_funcionario()
            elif x == 7:
                self.excluir_funcionario()
            elif x == 8:
                self.add_produto()
            elif x == 9:
                self.excluir_produto()
            elif x == 10:
                self.set_salario()
            elif x == 11:
                self.get_caixa()
            elif x == 12:
                y = input('Insira o nome do produto:')
                while y not in dict_produtos:
                    y = input('Erro. Insira o nome do produto:')
                y = dict_produtos[y]
                y.escolha()

            elif x == 13:
                break

            a = input('\nDeseja continuar em seu menu? (s/n)\nInsira sua escolha:')
            a = verif.verifica_s_n(a)
            if a == 'n' or a == 'N':
                break
            
Mercearia = Loja(lista_produtos,lista_funcionarios,lista_clientes,lista_clientes_vip,900)
