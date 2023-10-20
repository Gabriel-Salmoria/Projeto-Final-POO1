# Trabalho final - Gabriel Salmoria

import verif
from arq_prod import dict_produtos

dict_clientes = {}
lista_clientes = []
lista_clientes_vip = []

class Cliente:
    def __init__(self, cpf, nome_comp, num_cadastro,credito):
        self.cpf = cpf
        self.nome_comp = nome_comp
        self.num_cadastro = num_cadastro
        self.credito = credito
        
    def get_info(self):
         print(f'\nCliente: {self.nome_comp}\nCPF: {self.cpf}\nNúmero de cadastro: {self.num_cadastro}\nCredito: {self.credito}')
    
    def set_cpf(self):
        print(f'CPF atual: {self.cpf}')
        cpf = input('Informe o novo CPF:')
        cpf = verif.verifica_cpf(cpf)
        self.cpf = cpf
        print(f'CPF atualizado! Seu CPF atual é: {self.cpf}')
    
    def set_nome_comp(self):
        from arq_funcionario import dict_funcionarios
        print(f'Nome atual: {self.nome_comp}')
        nome_comp = input('Informe o novo nome completo:')
        while nome_comp in dict_clientes or  nome_comp in dict_funcionarios or nome_comp in dict_produtos:
            nome_comp = input('Nome já utilizado. Digite seu novo nome completo:')
        for key in dict_clientes:
            if dict_clientes[key] == self:
               x = key                
        self.nome_comp = nome_comp
        dict_clientes[nome_comp] = dict_clientes.pop(x)
        print(f'Nome atualizado! Seu nome atual é: {self.nome_comp}')
        
    def set_num_cadastro(self):
        print(f'Número de cadastro atual: {self.num_cadastro}')
        num_cadastro = input('Informe o novo número de cadastro:')
        num_cadastro = verif.verifica_cadastro(num_cadastro)
        self.num_cadastro = num_cadastro
        print(f'Cadastro atualizado! Seu cadastro atual é: {self.num_cadastro}')

    def set_credito(self):
        cred = input('Informe o valor que deseja colocar:')
        cred = verif.verifica_credito(cred)
        self.credito += cred
        print(f'Valor inserido! Seu crédito atual é: R${self.credito}')
    
    def get_produtos(self):
        for i in dict_produtos:
            i = dict_produtos[i]
            i.get_info()
            
    def comprar(self):
        from arq_loja import Mercearia
        prod = input('Digite o produto que deseja comprar:')
        while prod not in dict_produtos:
            prod = input('Erro. Digite o produto que deseja comprar:')
        prod = dict_produtos[prod]
        quant = input('Digite a quantidade que deseja comprar: ')
        quant = verif.verifica_quantidade(quant)
        if self.credito < prod.preco * quant:
            print('Crédito insuficiente. Faça uma recarga.')
        elif quant > prod.quantidade:
            print('Estoque insuficiente. Espere o estoque renovar.')
        else:
            self.credito -= prod.preco * quant
            prod.quantidade -= quant
            Mercearia.caixa += prod.preco * quant
            print(f'\nVocê comprou o produto: {prod.nome} x{quant}')
            print(f'Crédito deduzido de sua conta: R${(prod.preco * quant)}')
            print(f'Saldo atual: R${self.credito}')

       
    def escolha(self):
        while True:
            print(f'\nSelecione o que deseja fazer:')
            print('\n1. Acessar suas informações\n2. Alterar uma de suas informações\n3. Adicionar creditos\n4. Ver os produtos\n5. Comprar um produto\n6. Sair de sua conta')
            x = input('\nEscreva sua escolha:')
            x = verif.verifica_escolha(x,6)
            if x == 1:
                self.get_info()
            elif x == 2:
                print(f'\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nSelecione o que deseja fazer:')
                print('\n1. Alterar CPF\n2. Alterar nome\n3. Alterar número de cadastro\n4. Voltar ao menu anterior')
                y = input('\nInsira sua escolha:')
                y = verif.verifica_escolha(y,4)
                if y == 1:
                    self.set_cpf()
                elif y == 2:
                    self.set_nome_comp()
                elif y == 3:
                    self.set_num_cadastro()
                elif y == 4:
                    continue
            elif x == 3:
                self.set_credito()
            elif x == 4:
                self.get_produtos()
            elif x == 5:
                self.comprar()
            elif x == 6:
                break
            
            a = input('\nDeseja continuar em seu menu? (s/n)\nInsira sua escolha:')
            a = verif.verifica_s_n(a)
            if a == 'n' or a == 'N':
                break   

class Cliente_vip(Cliente):
    def __init__(self, cpf, nome_comp, num_cadastro,credito, telefone,endereco, desconto):
        super().__init__(cpf, nome_comp, num_cadastro,credito)
        self.telefone = telefone
        self.endereco = endereco
        self.desconto = desconto
        
    def get_info(self):
         print(f'\nCliente VIP: {self.nome_comp}\nCPF: {self.cpf}\nNúmero de cadastro: {self.num_cadastro}\nCredito: {self.credito}\nTelefone para contato: {self.telefone}\nEndereço: {self.endereco}\nDesconto em compras: {self.desconto}%')
    
    def set_cpf(self):
        return super().set_cpf()

    def set_nome_comp(self):
        return super().set_nome_comp()

    def set_num_cadastro(self):
        return super().set_num_cadastro()
    
    def set_credito(self):
        return super().set_credito()

    def set_telefone(self):
        print(f'Telefone atual: {self.telefone}')
        telefone = input('Coloque o novo telefone aqui:')
        telefone = verif.verifica_telefone(telefone)
        self.telefone = telefone
        print(f'Telefone atualizado! Seu telefone atual é: {self.telefone}')
        
    def set_endereco(self):
        print(f'Endereço atual: {self.endereco}')
        endereco = input('Coloque o novo endereço aqui:')
        self.endereco = endereco
        print(f'Endereço atualizado! Seu endereço atual é: {self.endereco}')

    def get_produtos(self):
        return super().get_produtos()
            
    def comprar(self):
        from arq_loja import Mercearia
        prod = input('Digite o produto que deseja comprar:')
        while prod not in dict_produtos:
            prod = input('Erro. Digite o produto que deseja comprar:')
        prod = dict_produtos[prod]
        quant = input('Digite a quantidade que deseja comprar: ')
        quant = verif.verifica_quantidade(quant)
        if self.credito < prod.preco * quant:
            print('Crédito insuficiente. Faça uma recarga.')
        elif quant > prod.quantidade:
            print('Estoque insuficiente. Espere o estoque renovar.')
        else:
            self.credito -= (prod.preco * quant) * (100 - self.desconto)/100
            prod.quantidade -= quant
            Mercearia.caixa += (prod.preco * quant) * (100 - self.desconto)/100
            print(f'\nVocê comprou o produto: {prod.nome} x{quant}')
            print(f'Crédito deduzido de sua conta: R${(prod.preco * quant) * (100 - self.desconto)/100}')
            print(f'Saldo atual: R${self.credito}')
            
    def escolha(self):
        while True:
            print(f'\nSelecione o que deseja fazer:')
            print('\n1. Acessar suas informações\n2. Alterar uma de suas informações\n3. Adicionar creditos\n4. Ver os produtos\n5. Comprar um produto\n6. Sair de sua conta')
            x = input('\nEscreva sua escolha:')
            x = verif.verifica_escolha(x,6)
            if x == 1:
                self.get_info()
            elif x == 2:
                print(f'\n-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=\n\nSelecione o que deseja fazer:')
                print('\n1. Alterar CPF\n2. Alterar nome\n3. Alterar número de cadastro\n4. Alterar telefone\n5. Alterar endereço\n6. Voltar ao menu anterior')
                y = int(input('\nInsira sua escolha:'))
                y = verif.verifica_escolha(y,6)
                if y == 1:
                    self.set_cpf()
                elif y == 2:
                    self.set_nome_comp()
                elif y == 3:
                    self.set_num_cadastro()
                elif y == 4:
                    self.set_telefone()
                elif y == 5:
                    self.set_endereco()
                elif y == 6:
                    continue
            elif x == 3:
                self.set_credito()
            elif x == 4:
                self.get_produtos()
            elif x == 5:
                self.comprar()
            elif x == 6:
                break
            
            a = input('\nDeseja continuar em seu menu? (s/n):')
            a = verif.verifica_s_n(a)
            if a == 'n' or a == 'N':
                break  

Gabriel = Cliente(11111111111, 'Gabriel Salmoria', 1111 ,100)
dict_clientes['Gabriel Salmoria'] = Gabriel
lista_clientes.append(Gabriel)

Sofia = Cliente_vip(22222222222, 'Sofia Almeida', 2222, 250.5, 4988990011, 'Minha casa', 5)
dict_clientes['Sofia Almeida'] = Sofia
lista_clientes_vip.append(Sofia)