lista_de_compras = []

opcao = 1

while opcao != 0:
    print('1 inserir')
    print('2 exluir ')
    print('3 lista ')
    print('4 editar ')

    print('0 sair ')

    opcao = int(input('qual opcao: '))

    if opcao == 1:
        print('inserir')

        item = input('qual item: ')
        lista_de_compras.append(item)
    
        print(lista_de_compras)

    elif opcao == 2:
        print('excluir')
        
        # saber o item
        # encotrar o item
        item = input('qual item deseja exluir: ')
        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            if lista_de_compras[indice] == item:
                print('item excluido', lista_de_compras[indice])
                lista_de_compras.pop(indice)
                break

    elif opcao == 3:
        print('listar')
        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            print(f'{indice} - {lista_de_compras[indice]}')
    
    elif opcao == 4:
        print('editar')
        item = input('qual item deseja edita: ')
        tamanho = len(lista_de_compras)
        for indice in range(tamanho):
            if lista_de_compras[indice] == item:
                novo_item = input('diga o nome item: ')
                lista_de_compras[indice] = novo_item

                print('item editado', lista_de_compras[indice])
            
                break



    elif opcao == 0:
        print('saindo...')

    else:
        print('opcao invalida')
        
    
    

