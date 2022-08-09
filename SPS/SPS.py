from random import randint


listaProgramas = ["calculadora", "cat", "texto aleatório", "sair"]
primeira_vez = True

def calculadora() :
    listaOperacoes = ["soma","subtetração", "mutiplicação", "divisão", "porcentagem", "módulo", "expoente", "raiz quadrada"]
    igual = "="*18
    print(igual)
    print("escolha a operação")
    print(igual)
  
    # escreve as operações para o console

    for i in range(len(listaOperacoes)):
        iponto = str(i+1) + ". "
        print(iponto, listaOperacoes[i])
    op = 0;  

    # escolhe a operação na calculadora

    while True:
        op = input("Qual é a operação? ")
        
        if op.isnumeric() :
            iop = int(op)-1
            if op.isnumeric() and int(op) <= len(listaOperacoes)+1:
                break
        print("\u001b[31m erro: operação inválida\u001b[0m")

    # input dos números 

    n1 = int(input("Qual é o primeiro número: "))
    if listaOperacoes[iop] != "raiz quadrada":
        n2 = int(input("Qual é o segundo número: "))

    # executa a operação e escreve o resultado para o console

    if iop == 0:
        print("A soma entre {} e {} é {} ".format(n1,n2,n1+n2))
    elif iop == 1:
        print("A difrença entre {} e {} é {}".format(n1,n2,n1-n2))
    elif iop == 2:
        print("O produto entre {} e {} é {}".format(n1,n2,n1*n2))
    elif iop == 3:
        print("O quociente entre {} e {} é {}".format(n1,n2,n1/n2))
    elif iop == 4:
        print("{} módulo de {} é {}".format(n1,n2,n1%n2))
    elif iop == 5:
        print("{} porcento de {} é {}".format(n1,n2,n1*(100/n2)))
    elif iop == 6:
        print("{} elevado a {} é {}".format(n1,n2,n1**n2))
    elif iop == 7:
        print("A raiz quadrada de {} é {}".format(n1,n1**0.5))
    else:
        print("Isso não devia acontecer")

    # volta para o início do programa

    inicio()


    


def cat() :
    print(input("cat: "))
    inicio()


def texto_aleatorio() :
    print("texto aleatório")

def inicio():
        # iniacialização
        primeira_vez = False
        print("\n")
        igual = "=" * 19
        print(igual)
        print("escolha a aplicação")
        print(igual,"")

        # escreve os programas para o console
        for i in range(len(listaProgramas)):
            iponto = str(i+1) + ". "
            print(iponto,  listaProgramas[i])

        # escolhe o programa na suite

        while True:
            escolha = input("Qual é a aplicação que queres usar: ")
            if escolha.isnumeric() and int(escolha) <= len(listaProgramas)+1:
                if escolha == "1" :
                    calculadora()
                elif escolha == "2" :
                    cat()
                elif escolha == "3" :
                    texto_aleatorio()
                elif escolha == "4":
                    sair = True
                    return
            else :
                print("\033[;31;m erro: operação inválida\033[;;;m")

if primeira_vez:
    inicio()