# Trabalho final - Gabriel Salmoria

import verif

dict_produtos = {}
lista_produtos = []

class Produto:
    def __init__(self, nome, preco, categoria, quantidade):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade    
    
    def get_info(self):
        print(f'\nProduto: {self.nome}\nPreço: R${self.preco}\nCategoria: {self.categoria}\nQuantidade em estoque: {self.quantidade}')

    def set_nome(self):
        nome1 = input('Coloque o novo nome do produto:')
        while nome1 in dict_produtos:
            nome1 = input('Nome já utilizado. Digite o nome do produto:')
        for key in dict_produtos:
            if dict_produtos[key] == self:
               x = key                
        self.nome = nome1
        dict_produtos[nome1] = dict_produtos.pop(x)
        print(f'Nome atualizado! Seu nome atual do produto é: {self.nome}')
    
    def set_preco(self):
        print(f'Preço atual: R${self.preco}')
        preco = input('Informe o novo preço:')
        preco = verif.verifica_credito(preco)
        self.preco = preco

    def set_categoria(self):
        print(f'Categoria atual: {self.categoria}')
        cat = input('Coloque a nova categoria desse item:\n1. Brinquedo\n2. Papelaria\n3. Bijuteria\nInsira sua escolha:')
        cat = verif.verifica_escolha(cat,3)
        if cat == 1:
            self.categoria = 'Brinquedo'
        elif cat == 2:
            self.categoria = 'Papelaria'
        elif cat == 3:
            self.categoria = 'Bijuteria'

    def set_estoque(self):
            print(f'Quantidade atual em estoque: R${self.quantidade}')
            quant = input('Informe a nova quantidade em estoque:')
            quant = verif.verifica_credito(quant)
            self.quantidade = quant
            
    def escolha(self):
                print(f'Selecione o que deseja fazer:')
                z = input('\n1. Alterar o nome do produto.\n2. Alterar o preço do produto\n3. Adicionar uma quantidade ao estoque\n4. Alterar a categoria do produto\nInsira sua escolha:')
                z = verif.verifica_escolha(z,3)
                if z == 1:
                    self.set_nome()
                elif z == 2:
                    self.set_preco()
                elif z == 3:
                    self.set_estoque()
                else:
                    self.set_categoria()
                    
x = Produto('Boneca', 12.0, 'Brinquedo', 100)
dict_produtos['Boneca'] = x
lista_produtos.append(x)