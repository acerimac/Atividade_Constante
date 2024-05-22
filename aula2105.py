# DESENVOLVEDOR(A) DE BACK-END, E PRECISA DESENVOLVER AS 
# ESTRUTURAS BÁSICAS DO FUNCIONAMENTO DE UM E-COMMERCE
# CRIAR UM SISTEMA DE E-COMMERCE
# PRECISA TER UM FORMULÁRIO CADASTRO
# O USUÁRIO PRECISA VER QUAIS PRODUTOS EXISTEM
# ESCOLHER O PRODUTO 
# ESCOLHER A FORMA DE PAGAMENTO
# MENSAGEM DE DESPEDIDA


# FUNCTION -> LAMBDA FUNCÕES CLASSICAS TAMBÉM
# CONSTANTES
# NOME DO USÁRIO
# ID CODIGO PRODUTO
# CPF DO USUÁRIO




# camis = 'Camiseta Oversized Feminina ID 98945, R$ 80,00'
# calca = 'Calça Cargo Preta Masculina ID 45450, R$ 145,00'
# head = 'Fone de Ouvido Xiaomi ID 21210, R$ 25,00'


#função de boas vindas
def boas_vindas():
    print('Prezado, bom dia. Para acessar as opções em nosso commerce, será necessário um preenchimento de um formulário')
    nome = input('Insira seu nome: ')
    CPF = int(input('Insira seu CPF: '))
    return nome, CPF

#função de opções
def mostrar_opcoes():
    print('''Bem vindo ao nossa loja
      Menu de opções
      (1) - Camiseta Oversized Feminina ID 98945, R$ 80,00
      (2) - Calça Cargo Preta Masculina ID 45450, R$ 145,00
      (3) - Fone de Ouvido Xiaomi ID 21210, R$ 25,00
        ''')

#função de escolher produto
def escolher_produto():
    produto = input('insira aqui qual o produto desejado')
    return produto

#função de escolher pagamento
def escolher_pagamento():
    pgto1 = 'pix'
    pgto2 = 'debito'
    pgto3 =  'crédito'
    print('''Ótima escolha! Agora, insira a forma de pagamento
     (1) - PIX
     (2) - DÉBITO
     (3) - CRÉDITO
      ''')
    escolha = int(input('>>')) 
    return escolha 

#função de processar pagamento
def processar_pagamento(escolha):
    if escolha == 1:
      print('Compra de aprovada com sucesso. Nossa loja agradece pela preferência. Volte sempre!')
    elif escolha == 2:
      print('Compra aprovada com sucesso. Nossa loja agradece pela preferência. Volte sempre!')
    elif escolha == 3:
      print('Compra aprovada com sucesso. Nossa loja agradece pela preferência. Volte sempre!')




boas_vindas()
mostrar_opcoes()
escolher_produto()
escolher_pagamento()
escolha = escolher_pagamento()
processar_pagamento(escolha)



