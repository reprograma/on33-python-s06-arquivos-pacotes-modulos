import csv #'importamos o modulo do python para trabalhar com csv


'''usamos o with para usar um arquivo e fechar esse arquivo quando terminar o que 
tiver dentro, mesmo se ocorrer um erro durante a execução do bloco de código. '''

'''na função open passamos
    1. o caminho do arquivo, 
    2. se o arquivo é de leitura ou escrita'''

'''Esta parte da linha cria um apelido (ou referência) chamado csvfile que 
será usado para se referir ao arquivo aberto dentro do bloco with'''

with open('Temperatura.csv', 'r') as csvfile: 
    leitor = csv.reader(csvfile) #Usamos a função csv reader para criar nosso leitor
    for linha in leitor: #aqui fazemos um for para ler cada linha do arquivo
        print(linha)






    
