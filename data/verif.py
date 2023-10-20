# Trabalho final - Gabriel Salmoria

def verifica_escolha(entrada, tamanho):
    try:
        entrada = int(entrada)
        if 0 < entrada <= tamanho:
            return int(entrada)
        else:
            entrada = input('Erro. Insira sua escolha:')
            return verifica_escolha(entrada, tamanho)
    except ValueError:
        entrada = input('Erro. Insira sua escolha:')
        return verifica_escolha(entrada, tamanho)

def verifica_cpf(entrada):
    try:
        entrada = int(entrada)
        if len(str(entrada)) == 11:
            return int(entrada)
        else:
            entrada = input('Erro. Insira seu CPF:')
            return verifica_cpf(entrada)
        
    except ValueError:
        entrada = input('Erro. Insira seu CPF:')
        return verifica_cpf(entrada)
    
def verifica_cadastro(entrada):
    try:
        entrada = int(entrada)
        if len(str(entrada)) == 4:
            return int(entrada)
        else:
            entrada = input('Erro. Insira seu cadastro:')
            return verifica_cadastro(entrada)
    except ValueError:
        entrada = input('Erro. Insira seu cadastro:')
        return verifica_cadastro(entrada)
    
def verifica_desconto(entrada):
    try:
        entrada = float(entrada)
        if 0 <= entrada <= 100:
            return float(entrada)
        else:
            entrada = input('Erro. Insira seu desconto:')
            return verifica_desconto(entrada)
    except ValueError:
        entrada = input('Erro. Insira seu desconto:')
        return verifica_desconto(entrada)

def verifica_credito(entrada):
    try:
        entrada = float(entrada)
        if entrada > 0:
            return float(entrada)
        else:
            entrada = input('Erro. Insira seu crédito:')
            return verifica_credito(entrada)    
    except ValueError:
        entrada = input('Erro. Insira seu crédito:')
        return verifica_credito(entrada)
    
def verifica_telefone(entrada):
    try:
        entrada = int(entrada)
        if len(str(entrada)) == 9 or len(str(entrada)) == 8:
            return int(entrada)
        else:
            entrada = input('Erro. Insira seu telefone:')
            return verifica_telefone(entrada)
    except ValueError:
        entrada = input('Erro. Insira seu telefone:')
        return verifica_telefone(entrada)

def verifica_quantidade(entrada):
    try:
        entrada = int(entrada)
        if entrada > 0:
            return int(entrada)
        else:
            entrada = input('Erro. Insira sua quantidade:')
            return verifica_quantidade(entrada)
    except ValueError:
        entrada = input('Erro. Insira sua quantidade:')
        return verifica_quantidade(entrada)

def verifica_s_n(entrada):
    if entrada == 's' or entrada == 'n' or entrada == 'S' or entrada == 'N':
        return entrada
    else:
        entrada = input('Erro. Insira sua escolha novamente. (s/n):')
        return verifica_s_n(entrada)

def nomeando(entrada):
    if ' ' in entrada:
        index = entrada.index(' ')
        return entrada[:index]
    else:
        return entrada

