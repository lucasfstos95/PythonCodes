#Programa 9.8 - Geração de uma pag html a partir de um dicionario
filmes = {
    'drama': ['Cidadão Kane', 'O poderoso Chefão'],
    'comédia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}

with open("arquivos/filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
<!DOCTYPE html>
<html lang="pt-br>
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>
    """)
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<p>{e}</p>\n")
    pagina.write("</body></html>")