
import pandas as pd

# Carregando o arquivo CSV dos jogadores
df = pd.read_csv("Jogadores.csv", sep=";")

# Ajustando nomes das colunas para facilitar o uso
df = df.rename(columns={
    "nome_do_jogador": "Nome",
    "salario_do_jogador": "Salario",
    "nome_time_jogador": "Time",
    "nome_estado_jogador": "Estado"
})

# Convertendo salário para número e trocando valores inválidos por 0
df["Salario"] = pd.to_numeric(df["Salario"], errors="coerce").fillna(0)

# 1 - Nome e time dos jogadores com salário acima de 20 mil
consulta1 = df[df["Salario"] > 20000][["Nome", "Time"]]

# 2 - Nome e salário dos jogadores dos times de MG
consulta2 = df[df["Estado"] == "MG"][["Nome", "Salario"]]

# 3 - Jogadores cujo nome contenha a letra "u"
consulta3 = df[df["Nome"].str.contains("u", case=False)][["Nome", "Time"]]

# 4 - Jogadores ordenados por salário (decrescente)
consulta4 = df.sort_values(by="Salario", ascending=False)[["Nome", "Salario", "Time"]]

# 5 - Jogadores ordenados por time (crescente) e salário (decrescente)
consulta5 = df.sort_values(by=["Time", "Salario"], ascending=[True, False])[["Nome", "Salario", "Time"]]

# 6 - Quantidade de jogadores por time
consulta6 = df.groupby("Time")["Nome"].count()

# 7 - Média salarial por time
consulta7 = df.groupby("Time")["Salario"].mean()

# Exibindo os resultados
print("1) Jogadores com salário acima de 20 mil:")
print(consulta1, "\n")

print("2) Jogadores dos times de MG:")
print(consulta2, "\n")

print("3) Jogadores com a letra 'u' no nome:")
print(consulta3, "\n")

print("4) Jogadores ordenados por salário (decrescente):")
print(consulta4, "\n")

print("5) Jogadores ordenados por time e salário:")
print(consulta5, "\n")

print("6) Quantidade de jogadores por time:")
print(consulta6, "\n")

print("7) Média salarial por time:")
print(consulta7)
