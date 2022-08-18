from guardarArquivo import guardarArquivo
def cat() :
    guardar = input("Queres guardar o texto para um arquivo?: [S/N]").strip().upper()
    cat = input("cat: ")
    print(cat)
    if guardar == "S" :
        guardarArquivo(cat)