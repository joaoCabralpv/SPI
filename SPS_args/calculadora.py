from mailbox import NotEmptyError
from guardarArquivo import guardarArquivo
from math import factorial

def calculadora(n1,op,n2,salvar,nomeArquivo) :
    n1 = float(n1)
    n2 = float(n2)
    print()

    # executa a operação e escreve o resultado para o console

    texto = 0
    resultado = 0

    if op == "mais":
        resultado = n1+n2
        texto ="A soma entre {} e {} é {} ".format(n1,n2,resultado)
    elif op == "menos":
        resultado = n1-n2
        texto = "A difrença entre {} e {} é {}".format(n1,n2,resultado)
    elif op == "vezes":
        resultado = n1*n2
        texto = "O produto entre {} e {} é {}".format(n1,n2, resultado)
    elif op == "dividir":
        resultado = n1/n2
        texto = "O quociente entre {} e {} é {}".format(n1,n2,resultado)
    elif op == "porcento":
        resultado = n1*(100/n2)
        texto = "{} porcento de {} é {}".format(n1,n2,resultado)
    elif op == "modulo":
         resultado = n1%n2
         texto ="{} módulo de {} é {}".format(n1,n2,resultado)
    elif op == "elevado":
        resultado = n1**n2
        texto = "{} elevado a {} é {}".format(n1,n2,resultado)
    elif op == "raiz quadrada":
        resultado = n1**0.5
        texto = "A raiz quadrada de {} é {}".format(n1,resultado)
    elif op == "raiz cubica":
        resultado = n1**(1/3)
        texto = "A raiz cúbica de {} é {}".format(n1,resultado)
    elif op == "media":
        resultado = (n1+n2)/2
        texto = "A média entre {} e {} é {}".format(n1,n2,resultado)
    elif op == "maior":
        resultado = (max(n1,n2))
        texto = "Entre {} e {}, o maior é {}".format(n1,n2,resultado)
    elif op == "menor":
        resultado = min(n1,n2)
        texto = "Entre {} e {}, o menor é ".format(n1,n2,resultado)
    elif op == "factorial":
        resultado = factorial(int(n1))
        texto = "{} factorial é {}".format(int(n1),resultado)
    else:
        print("Isso não devia acontecer")

    # escreve o resultado para o terminal e guarda o resultado para um arquivo se o usário pediu  

    print(texto)
    print("\n")
    if salvar:
        guardarArquivo(resultado,nomeArquivo)
   
    # volta para o início do programa
