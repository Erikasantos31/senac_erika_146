'sistema para cadastro de produto'

'''Você foi contratado para ddesenvolver um sistemas de cadastro de produtos para determinada loja, que deve ser capaz de armazenar 
informações como nome, categoria, preco e quantidade em estoque. O sistema deve oferecer um menu interativo com as seguintes opções:

1) cadastro de novo produto;
2) editar dados de um produto;
3) exluir um produto;
4) listar todos produtos cadastrados;
5) sair do sistema;

'''
opcao = 1
lista_produtos = [
    {'nome': 'limao', 'categoria': 'fruta', 'preco': 1.99, 'qtd_estoque': 50 }, 
    {'nome': 'manga','categoria': 'fruta', 'preco': 4.99, 'qtd_estoque': 80 }, 
    {'nome': 'macarrao', 'categoria': 'não precivél', 'preco': 2.89, 'qtd_estoque': 100 }, 
    {'nome': 'arooz', 'categoria': 'não precivél', 'preco': 25.99, 'qtd_estoque': 200 }, 
    {'nome': 'farinha', 'categoria': 'não precivél', 'preco': 3.99, 'qtd_estoque': 150 }
]

sub_opcao = 0
tipo = ''
nome_valor = ''

while opcao != 5:
    
    print('------------------MENU PRINPAL--------------------')
    print(                                                    )
    print('1. CADASTRAR                                      ')
    print('2. EDITAR DADOS DE UM PRODUTO                     ')
    print('3. EXCLUIR UM PRODUTO                             ')
    print('4. LISTAR TODOS PRODUTOS CADASTRADO               ')
    print('5. SAIR DO SISTEMA                                ')

    print('-'*50)
    print() 

    opcao = int(input('opcao desejada: '))
    print()
    nome = ()
    categoria = ()
    preco = ()
    qtd_estoque = ()

    if opcao == 1 :
        print('1.CADASTRAR')

        print('-'*50)
        #nome, categoria, preco e quantidade em estoque
        
        nome = str(input('nome: '))
        categoria = str(input('categoria: '))
        preco =float(input('preco: '))
        qtd_estoque =int(input('quantidade de estoque: '))

        produto = {
            'nome': nome,
            'categoria': categoria,
            'preco': preco,
            'qtd_estoque': qtd_estoque
        }

        lista_produtos.append(produto)
        print(lista_produtos)

    if opcao == 2 :
        print('2.EDITAR DADOS DE UM PRODUTO: ')

        for i in range(len(lista_produtos)): 
            print(f'{i} - {lista_produtos[i]}')
            
        indice = int(input("qual produto voce deseja edital? "))
        print(lista_produtos[indice])


        while sub_opcao != 5:
        
     #submenu
            print('-'*100)

            print()
            
            print('----SUBMENU----')
            print('1. NOME: ')
            print('2. CATEGORIA: ')
            print('3. PRECO: ')
            print('4. QTD_ESTOQUE: ')
            print('5. VOLTAR AO MENU PRINPAL: ')

            sub_opcao = int(input('qual opção que deseja editar:? '))

            if sub_opcao > 0 and sub_opcao <= 5:
                match sub_opcao:
                    case 1:
                        tipo = 'nome'
                        novo_valor = input(" informe o nome: ")
                    case 2:
                        tipo = 'categoria'
                        novo_valor = input(" informe a categoria: ")
                    case 3: 
                        tipo = 'preco'
                        novo_valor = input(" informe o novo preco: ")
                    case 4: 
                        tipo = 'qtd_estoque'
                        novo_valor = input("informe a qtd_estoque: ")
                    case 5:
                        print('voltar ao menu principal')
                        break

                lista_produtos[indice][tipo] = novo_valor
                print(lista_produtos[indice])
                
            else:
                print(" Valor do indice invalido")
                
                for i in range(len(lista_produtos)):
                    print(f"{i} - {lista_produtos} '\n' ")

    print('-'*100)

    if opcao == 3:
        print('3. EXCLUIR UM PRODUTO')
        
        
        for i in list(lista_produtos):
            print(f"{i} - {lista_produtos} '\n' ")
      
            print(" Excluir produto".center(50, '-'))
            print()
            #recebendo a posição do produto
            indice = int(input('informe o indice do produto que deseja excluir: '))
    
            #Validando indice
            if indice >= 0 and indice < len(lista_produtos):
                
                #executando e alteração de valor
                del(lista_produtos[indice])
        
            else:
                print('valor do indice invalido')

            #exibindo a lista 
            for i in range(len(lista_produtos)):
                print(f'{i} - {lista_produtos} ')

       
    if opcao == 4:
        print('4. LISTAR TODOS PRODUTOS CADASTRADO: ')

        for i in range(len(lista_produtos)):
            print(f'{i} - {lista_produtos} \n' )

        
    if opcao == 5:
        print('Saindo do sistema ')
