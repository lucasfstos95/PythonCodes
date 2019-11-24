import pandas as pd

uri = "https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula4.1/movies.csv"
pd.read_csv(uri, error_bad_lines=False)