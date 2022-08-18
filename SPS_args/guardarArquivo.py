def guardarArquivo(texto) :
    arquivo = open(input("Qual é o nome do arquivo? Se tiver um arquivo com o mesmo nome, o arquivo será apagado: "), "w", encoding="utf-8")
    arquivo.write(str(texto))