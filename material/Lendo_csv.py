import csv

with open('Temperatura.csv', 'r') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)


'''importamos o modulo do python para trabalhar com csv'''

'''usamos o with para usar um arquivo e fechar esse arquivo quando terminar o que 
tiver dentro, mesmo se ocorrer um erro durante a execução do bloco de código. '''

'''na função open passamos
    1. o caminho do arquivo, 
    2. se o arquivo é de leitura ou escrita'''

'''Esta parte da linha cria um apelido (ou referência) chamado csvfile que 
será usado para se referir ao arquivo aberto dentro do bloco with'''

'''Usamos a função csv reader para ler cada linha do arquivo'''


    
