# Definindo os dados
dados = [
    ("Maria", "Matrix", 8),
    ("Pedro", "Matrix", 8),
    ("Joao", "Star Wars", 9),
    ("Gabriel", "Star Wars", 6),
    ("Ana", "Divertidamente", 10),
    ("Daniel", "Divertidamente", 9),
    ("Joaquim", "Star Wars", 7),
    ("Sara", "Matrix", 5),
    ("Manuel", "Divertidamente", 9),
    ("Beatriz", "Star Wars", 4),
    ("Gabriela", "Divertidamente", 10),
    ("Diego", "Matrix", 9),
    ("Joaquim", "Star Wars", 7),
    ("Gabriel", "Star Wars", 6)
]

unicos = {}
for usuario, filme, nota in dados:
    if (usuario, filme) not in unicos:
        unicos[(usuario, filme)] = nota


soma_notas = {}
contagem_filmes = {}

for (usuario, filme), nota in unicos.items():
    if filme not in soma_notas:
        soma_notas[filme] = 0
        contagem_filmes[filme] = 0
    soma_notas[filme] += nota
    contagem_filmes[filme] += 1


media_por_filme = {filme: soma_notas[filme] / contagem_filmes[filme] for filme in soma_notas}


filme_maior_media = max(media_por_filme, key=media_por_filme.get)


print("Média de notas e número de pessoas que assistiram cada filme:")
for filme in media_por_filme:
    print(f"{filme}: Média = {media_por_filme[filme]:.2f}, Pessoas = {contagem_filmes[filme]}")

print(f"\nFilme com a maior média: {filme_maior_media} com média de {media_por_filme[filme_maior_media]:.2f}")
