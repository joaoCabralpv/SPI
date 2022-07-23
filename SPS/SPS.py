listaProgramas = ["calculadora", "cat", "texto aleatório", "sair"]
primeira_vez = True

def calculadora() :
    listaOperacoes = ["soma","subtetração", "mutiplicação", "divisão", "porcentagem", "módulo", "expoente", "raiz quadrada"]
    igual = "="*19
    print(igual)
    print("escolha a operação")
    print(igual)


    for i in range(len(listaOperacoes)):
        iponto = str(i+1) + ". "
        print(iponto, listaOperacoes[i])
    op = 0;    
    while True:
        op = input("Qual é a operação? ")
        if op.isnumeric() :
            if int(op) >= len(listaOperacoes)+1 and int(op) >= 1:
                break
        print("\033[;31;m erro: operação inválida\033[;;;m")
    
    n1 = int(input("Qual é o 1º número? "))
    if listaOperacoes[op] is not "raiz quadrada":
        n2 = int(input("Qual é o 2º número? "))

    


def cat() :
    print("cat")
def texto_aleatorio() :
    print("texto aleatorio")

def inicio():
    # iniacialização
    primeira_vez = False
    igual = "=" * 19
    print(igual)
    print("escolha a aplicação")
    print(igual,"\n")

    # escreve os programas para o console
    for i in range(len(listaProgramas)):
        iponto = str(i+1) + ". "
        print(iponto,  listaProgramas[i])

    # escolhe o programa na suite

    escolha = input("Qual é a aplicação que queres usar: ")
    if escolha.isnumeric() and int(escolha) <= len(listaProgramas)+1:
        if escolha == "1" :
            calculadora()
        elif escolha == "2" :
            cat()
        elif escolha == "3" :
            texto_aleatorio()
        
if primeira_vez :
    inicio()