from cgi import print_arguments


listaprogramas = ["calculadora", "cat", "texto aleatório", "sair"]
primeira_vez = True

def calculadora() :
    print("calculadora")
def cat() :
    print("cat")
def texto_aleatorio() :
    print("texto aleatorio")

def inicio():
    primeira_vez = False
    igual = "=" * 19
    print(igual)
    print("escolha a aplicação")
    print(igual,"\n")

    for i in range(len(listaprogramas)):
        iponto = str(i+1) + ". "
        print(iponto,  listaprogramas[i])

    escolha = input("Qual é a aplicação que queres usar: ")
    if escolha.isnumeric() and int(escolha) <= len(listaprogramas)+1:
        if escolha == "1" :
            calculadora()
        elif escolha == "2" :
            cat()
        elif escolha == "3" :
            texto_aleatorio()
        
if primeira_vez :
    inicio()