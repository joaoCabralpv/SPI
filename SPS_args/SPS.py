import sys
from calculadora import calculadora
from cat import cat
from textoAleatorio import textoAleatorio
salvar = False
nomeArquivo = 0
#try : 
if True:
    salvar = sys.argv[len(sys.argv)-2] == "s" or sys.argv[len(sys.argv)-2] == "salvar"
    print(salvar)


    if salvar:
        nomeArquivo = sys.argv[len(sys.argv)-1]

    if sys.argv[1] == "c" or sys.argv[1] == "calculadora":
        calculadora(sys.argv[2],sys.argv[3],sys.argv[4],salvar,nomeArquivo)
    elif sys.argv[1] == "a" or sys.argv[1] == "cat":
        cat(sys.argv[2],salvar,nomeArquivo)
    elif sys.argv[1] == "t" or sys.argv[1] == "textoAleatorio":
        textoAleatorio(int(sys.argv[2]),salvar,nomeArquivo)
    else:
        print("Arurmento inválido") 
#except:
 #   print("Nenhum argumento foi dado")