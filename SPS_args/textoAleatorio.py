from guardarArquivo import guardarArquivo
from random import randint


def textoAleatorio(numChar,salvar,nomeArquivo) :
    string = ""
    for i in range(int(numChar)):
        string += chr(randint(0,0xD7FA))
    print("\n")
    print(string)
    if salvar:
        guardarArquivo(string, nomeArquivo)