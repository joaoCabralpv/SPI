from mailbox import NotEmptyError
from guardarArquivo import guardarArquivo
from math import factorial

def calculadora(n1,op,n2,salvar,nomeArquivo) :
    n1 = float(n1)
    n2 = float(n2)
    #listaOperacoes = ["soma","subtetração", "mutiplicação", "divisão", "porcentagem", "módulo", "expoente", "raiz quadrada", "raiz cúbica", "média", "maior", "menor", "factorial"]
    #igual = "="*18
    #print(igual)
    #print("escolha a operação")
    #print(igual)
  
    # escreve as operações para o console

    #for i in range(len(listaOperacoes)):
     #   if i < 9:
      #      iponto = str(i+1) + ". "
       # else:
        #    iponto = str(i+1) + "."
        #print(iponto, listaOperacoes[i])
    #op = 0;  

    # escolhe a operação na calculadora

    #while True:
     #   op = input("Qual é a operação? ")
        
      #  if op.isnumeric() :
       #     iop = int(op)-1
        #    if op.isnumeric() and int(op) <= len(listaOperacoes)+1:
         #       break
        #print("\u001b[31m erro: operação inválida\u001b[0m")

    # input dos números 

    #n1 = int(input("Qual é o primeiro número: "))
    #if listaOperacoes[iop] != "raiz quadrada" and listaOperacoes[iop] != "raiz cúbica" and listaOperacoes[iop] != "factorial":
     #   n2 = int(input("Qual é o segundo número: "))

    #guardar = input("Queres grardar o resultado para um arquivo? [S/N] : ").strip().upper()
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
    elif op == "a dividir por":
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
        resultado = factorial(n1)
        texto = "{} factorial é {}".format(n1,resultado)
    else:
        print("Isso não devia acontecer")

    # escreve o resultado para o terminal e guarda o resultado para um arquivo se o usário pediu  

    print(texto)
    print("\n")
    if salvar:
        guardarArquivo(resultado,nomeArquivo)
   
    # volta para o início do programa
