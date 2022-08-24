from guardarArquivo import guardarArquivo
from random import randint


def textoAleatorio() :
    string = ""
    for i in range(int(input("Quantos caracteres queres que o texto tenha?: "))):
        string += chr(randint(0,0xD7FA))
    print("\n")
    print(string)
    guardar = input("Queres guardar o texto para um arquivo?: [S/N]").strip().upper()
    if guardar == "S":
        guardarArquivo(string)