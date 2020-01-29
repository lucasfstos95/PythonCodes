import pandas as pd

uri = "https://raw.githubusercontent.com/lucasfstos95/PythonCodes/master/csv_github_example/csv_github.csv"
filmes = pd.read_csv(uri)
print(filmes)