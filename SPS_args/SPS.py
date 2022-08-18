from guardarArquivo import guardarArquivo
from calculadora import calculadora
from cat import cat
from textoAleatorio import textoAleatorio


listaProgramas = ["calculadora", "cat", "texto aleatório", "sair"]
primeira_vez = True


def inicio(): 
            # iniacialização
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

            escolha = input("Qual é a aplicação que queres usar: ")
            if escolha.isnumeric() and int(escolha) <= len(listaProgramas)+1:
                if escolha == "1" :
                    calculadora()
                elif escolha == "2" :
                    cat()
                elif escolha == "3" :
                    textoAleatorio()
                elif escolha != "4" :
                    input("\033[;31;merro: operação inválida\033[;;;m")
                    print("\n")
                    inicio()
            else :
                input("\033[;31;merro: operação inválida\033[;;;m")
                print("\n")
                inicio()

if primeira_vez:
    primeira_vez = False
    a = inicio()

