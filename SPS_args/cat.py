from guardarArquivo import guardarArquivo
def cat(string, salvar, nomeArquivo) :
    print(salvar)
    #guardar = input("Queres guardar o texto para um arquivo?: [S/N]").strip().upper()
    #cat = input("cat: ")
    print(string)
    if salvar :
        guardarArquivo(string, nomeArquivo)