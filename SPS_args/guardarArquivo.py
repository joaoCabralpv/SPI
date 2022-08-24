def guardarArquivo(texto,nomeArquivo) :
    arquivo = open(nomeArquivo, "w", encoding="utf-8")
    arquivo.write(str(texto))