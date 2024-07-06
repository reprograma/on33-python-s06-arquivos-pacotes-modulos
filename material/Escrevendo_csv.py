import csv

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

with open('Temperatura.csv', 'w') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['dia', 'mês', 'temperatura', 'chuva'])
    escritor.writerows(novas_temperaturas)


'''importamos o modulo do python para trabalhar com csv'''

'''usamos o with para usar um arquivo e fechar esse arquivo quando terminar o que 
tiver dentro, mesmo se ocorrer um erro durante a execução do bloco de código. '''

'''na função open passamos
    1. o caminho do arquivo, 
    2. se o arquivo é de leitura ou escrita'''

'''Esta parte da linha cria um apelido (ou referência) chamado csvfile que 
será usado para se referir ao arquivo aberto dentro do bloco with'''

'''Usamos a função csv writer para escrever em cada linha do arquivo'''