'''
Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Exponenciação
* 6. Raiz quadrada
* 7. Porcentagem
* 8. Resto da divisão
* 9. Divisão de inteiro
* 0 .Sair do programa 

*********************************************************************
Informe a opção desejada:

A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 0.
'''
opcao = ""


def soma1(a,b):
    c = a + b
    return c 

def subtracao(a,b):
    c = a - b
    return c

def multiplicacao(a,b):
    c = a * b
    return c

def divisao(a,b):
    c = a / b
    return c

def exponenciacao(a,b):
    c = a ** b
    return c

def raiz_quadrada(a):
    c = a ** (1/2)
    return c

def porcentagem(a,b):
    c = a * b / 100
    return c

def resto_da_divisao(a,b):
    c = a % b
    return c

def divisao_de_inteiro(a, b):
    c = a // b
    return c


while opcao != 0: 
   
    print('-----------------------CALCULADORA--------------------------')
    print()
    print('QUAL CALCULO DESEJA FAZER                                  #')
    print()
    print('1. Adição:                                                 #')
    print('2. Subtração:                                              #')
    print('3. Multiplicação:                                          #')
    print('4. Divisão:                                                #')
    print('5. Exponenciação:                                          #')
    print('6. Raiz quadrada:                                          #')
    print('7. Porcentagem                                             #')
    print('8. Resto da divisão:                                       #')
    print('9. Divisão de inteiro:                                     #')
    print('0 .Sair do programa:                                       #')
    print()
    print('-'*60)
    print()

    opcao = int(input('informe qual opção você deseja: '))
    # num1 = int(input('informe um numero: '))
    # num2 = int(input('informe outro numero: '))
    print('-'*60)
    
    if opcao == 1:
        print('ADIÇÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = soma1(num1 , num2)
        print()
        print(resultado, 'é o resultado da sua adição! ')



    elif opcao == 2:
        print('SUBTRAÇÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = subtracao(num1 , num2)
        print()
        print(resultado,'é o resultado da sua subtração! ')

    
    elif opcao == 3:
        print('MULTIPLICAÇÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = multiplicacao(num1 , num2)
        print()
        print(resultado, 'é o resultado da sua multiplicação! ')

    elif opcao == 4:
        print('DIVISÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = divisao(num1, num2)
        print()
        print(resultado,'é o resultado da sua divisão! ')

    elif opcao == 5:
        print('EXPONENCIAÇÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = exponenciacao(num1, num2)
        print()
        print(resultado,'é o resultado sua exponenciação! ')

    elif opcao == 6:
        print('RAIZ QUADRADA: ')
        print()
        num = int(input('informe um numero: '))
        resultado = raiz_quadrada(num)
        print()
        print(resultado, 'é o resultado da sua raiz quadrada! ')

    elif opcao == 7:
        print('PORCENTAGEM: ')
        print()
        num1 = int(input('informe um numero: '))
        resultado = raiz_quadrada(num1)
        print()
        print(resultado, 'é o resultado, da sua porcentagem! ')

    elif opcao == 8:
        print('RESTO DA DIVISÃO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = resto_da_divisao(num1, num2)
        print()
        print(resultado, 'é o resultado do resto da divisão! ')
     
    elif opcao == 9:
        print('DIVISÃO DE INTEIRO: ')
        print()
        num1 = int(input('informe um numero: '))
        num2 = int(input('informe outro numero: '))
        resultado = divisao_de_inteiro(num1,num2)
        print()
        print(resultado, 'é o resulatdo da sua divisão de inteiro! ')

    elif opcao == 0:
        print('SAIR DO PROGRAMA: ')

    else:
        print('Esta opção é invalida... ')