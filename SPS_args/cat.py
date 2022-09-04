from guardarArquivo import guardarArquivo
def cat(string, salvar, nomeArquivo) :

    print(string)
    if salvar :
        guardarArquivo(string, nomeArquivo)