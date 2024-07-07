import csv #importamos o modulo do python para trabalhar com csv


#a lista novas_temperaturas contém os dados que queremos inserir no nosso csv
novas_temperaturas = [    
    ['10', '10', '25', 'Sim'],
    ['11', '10', '22', 'Não'],
    ['12', '10', '17', 'Sim'],   
    ['13', '10', '28', 'Sim'],
    ['14', '10', '27', 'Não'],
    ['15', '10', '17', 'Sim'],
    ['16', '10', '30', 'Sim'],
    ['17', '10', '22', 'Não'],
    ['18', '10', '27', 'Sim']
]

'''usamos o with para usar um arquivo e fechar esse arquivo quando terminar o que 
tiver dentro, mesmo se ocorrer um erro durante a execução do bloco de código. '''

'''na função open passamos
    1. o caminho do arquivo, 
    2. se o arquivo é de leitura ou escrita
    3. o enconding utf-8 para trabalharmos com acentos'''

with open('Temperatura.csv', 'w', encoding="UTF-8", newline='') as csvfile: #csvfile é o apelido que criamos para usar o nosso arquivo
    
    escritor = csv.writer(csvfile)  
#Usamos a função csv writer para criar nosso escritor

    escritor.writerow(['dia', 'mês', 'temperatura', 'chuva'])
#usamos a funcao writerow para escrever uma linha no arquivo, nesse caso nosso cabeçalho

    escritor.writerows(novas_temperaturas)
#usamos a função write rows para escrever várias linhas no arquivo

