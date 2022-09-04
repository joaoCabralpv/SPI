import sys
from calculadora import calculadora
from cat import cat
from textoAleatorio import textoAleatorio
salvar = False
nomeArquivo = 0
try :
    n2 = 0.0
    # Salva o arquivo se o argumento -s for encontrado
    salvar = sys.argv[len(sys.argv)-2] == "s" or sys.argv[len(sys.argv)-2] == "salvar"

    # verifica o nome do arquivo para guardar o resultado
    if salvar:
        nomeArquivo = sys.argv[len(sys.argv)-1]

    # escolhe o programa para ser executado

    if sys.argv[1] == "c" or sys.argv[1] == "calculadora":
        try:
            n2 = sys.argv[4] 
        except:
            1
        calculadora(sys.argv[2],sys.argv[3],n2,salvar,nomeArquivo)
    elif sys.argv[1] == "a" or sys.argv[1] == "cat":
        cat(sys.argv[2],salvar,nomeArquivo)
    elif sys.argv[1] == "t" or sys.argv[1] == "textoAleatorio":
        textoAleatorio(int(sys.argv[2]),salvar,nomeArquivo)
    else:
        print("Arurmento inválido") 
except IndexError:
   print("Nenhum argumento foi dado")