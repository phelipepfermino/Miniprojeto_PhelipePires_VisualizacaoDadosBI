# Mini-Projeto Avaliativo - Módulo 1 - Semana 07
# Curso: Visualização de Dados e Business Intelligence
# Aluno: Phelipe Pires
# Turma: Visualização de Dados e BI
# Tema: Análise Exploratória de Dados da base Varejo

import pandas as pd


def limpar_texto(valor):
    if pd.isna(valor):
        return valor
    return str(valor).strip()


# Sprint 1 - Importação dos dados

print("=" * 70)
print("ANÁLISE EXPLORATÓRIA DE DADOS - BASE VAREJO")
print("=" * 70)

caminho_arquivo = "dados/Varejo.csv"

# Leitura do arquivo CSV
df = pd.read_csv(caminho_arquivo, sep=";")

print("\nSPRINT 1 - IMPORTAÇÃO DOS DADOS")
print("-" * 70)

print("Quantidade de registros:", df.shape[0])
print("Quantidade de colunas:", df.shape[1])

print("\nColunas da base original:")
print(df.columns)

print("\nTipos de dados da base original:")
print(df.dtypes)

print("\nPrimeiras linhas da base:")
print(df.head())


# Sprint 2 - Transformação de strings, inteiros, floats e datas

print("\nSPRINT 2 - TRANSFORMAÇÃO DOS DADOS")
print("-" * 70)

df_limpo = df.copy()

# Remoção de colunas vazias
colunas_vazias = df_limpo.columns[df_limpo.isnull().all()]
df_limpo = df_limpo.drop(columns=colunas_vazias)

print("\nColunas totalmente vazias removidas:")
print(list(colunas_vazias))

# Padronização e renomeação das colunas
df_limpo.columns = (
    df_limpo.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

df_limpo = df_limpo.rename(columns={
    "data": "data",
    "co_id": "compra_id",
    "cl_id": "cliente_id",
    "cl_genero": "cliente_genero",
    "cl_ec": "cliente_estado_civil",
    "cl_fhl": "cliente_numero_filhos",
    "cl_seg": "cliente_segmento",
    "pr_id": "produto_id",
    "pr_cat": "produto_categoria",
    "pr_nome": "produto_nome"
})

print("\nColunas após padronização e renomeação:")
print(df_limpo.columns)

# Limpeza de textos
colunas_texto = df_limpo.select_dtypes(include=["object", "string"]).columns

for coluna in colunas_texto:
    df_limpo[coluna] = df_limpo[coluna].apply(limpar_texto)

print("\nLimpeza de textos realizada.")

# Conversão de data
df_limpo["data"] = pd.to_datetime(df_limpo["data"], errors="coerce", dayfirst=True)
datas_invalidas = df_limpo["data"].isnull().sum()

print("\nColuna de data convertida para datetime.")
print("Datas inválidas encontradas:", datas_invalidas)

# Conversão de colunas numéricas
colunas_numericas_esperadas = [
    "compra_id",
    "cliente_id",
    "cliente_estado_civil",
    "cliente_numero_filhos",
    "produto_id"
]

for coluna in colunas_numericas_esperadas:
    df_limpo[coluna] = pd.to_numeric(df_limpo[coluna], errors="coerce")

print("\nColunas numéricas convertidas:")
print(colunas_numericas_esperadas)


# Sprint 3 - Limpeza de nulos e duplicatas

print("\nSPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS")
print("-" * 70)

print("\nValores nulos antes da limpeza:")
print(df_limpo.isnull().sum())

duplicatas_antes = df_limpo.duplicated().sum()
print("\nRegistros duplicados antes da limpeza:", duplicatas_antes)

# Tratamento de categorias vazias ou inválidas
categorias_invalidas = (
    df_limpo["produto_categoria"].isnull().sum()
    + (df_limpo["produto_categoria"].astype(str).str.strip() == "").sum()
    + (df_limpo["produto_categoria"].astype(str).str.strip() == "#N/D").sum()
)

df_limpo["produto_categoria"] = df_limpo["produto_categoria"].replace("", "Sem Categoria")
df_limpo["produto_categoria"] = df_limpo["produto_categoria"].replace("#N/D", "Sem Categoria")
df_limpo["produto_categoria"] = df_limpo["produto_categoria"].fillna("Sem Categoria")

print("\nCategorias vazias ou inválidas tratadas:", categorias_invalidas)

# Tratamento de nulos numéricos com mediana
colunas_numericas = df_limpo.select_dtypes(include="number").columns

print("\nTratamento de nulos em colunas numéricas:")

for coluna in colunas_numericas:
    total_nulos = df_limpo[coluna].isnull().sum()

    if total_nulos > 0:
        mediana = df_limpo[coluna].median()
        df_limpo[coluna] = df_limpo[coluna].fillna(mediana)
        print(f"- {coluna}: {total_nulos} nulos preenchidos com mediana {mediana}")

# Remoção de duplicatas
df_limpo = df_limpo.drop_duplicates()

duplicatas_depois = df_limpo.duplicated().sum()

print("\nRegistros duplicados após a limpeza:", duplicatas_depois)

print("\nValores nulos após a limpeza:")
print(df_limpo.isnull().sum())


# Sprint 4 - Estatística descritiva

print("\nSPRINT 4 - ESTATÍSTICA DESCRITIVA")
print("-" * 70)

coluna_filhos = "cliente_numero_filhos"

print("\nEstatísticas da coluna cliente_numero_filhos:")
print("Média:", df_limpo[coluna_filhos].mean())
print("Mediana:", df_limpo[coluna_filhos].median())
print("Desvio padrão:", df_limpo[coluna_filhos].std())
print("Moda:", df_limpo[coluna_filhos].mode()[0])
print("Máximo:", df_limpo[coluna_filhos].max())
print("Mínimo:", df_limpo[coluna_filhos].min())
print("Contagem:", df_limpo[coluna_filhos].count())


# Sprint 5 - Agrupamentos, relatório e documentação

print("\nSPRINT 5 - AGRUPAMENTOS E RELATÓRIO FINAL")
print("-" * 70)

print("\nAGRUPAMENTO 1 - QUANTIDADE DE COMPRAS POR CATEGORIA")
print("-" * 70)

compras_por_categoria = (
    df_limpo
    .groupby("produto_categoria")["compra_id"]
    .count()
    .sort_values(ascending=False)
)

print(compras_por_categoria)

print("\nAGRUPAMENTO 2 - QUANTIDADE DE COMPRAS POR GÊNERO")
print("-" * 70)

compras_por_genero = (
    df_limpo
    .groupby("cliente_genero")["compra_id"]
    .count()
    .sort_values(ascending=False)
)

print(compras_por_genero)

print("\nAGRUPAMENTO EXTRA - QUANTIDADE DE COMPRAS POR MÊS")
print("-" * 70)

df_limpo["mes"] = df_limpo["data"].dt.to_period("M")

compras_por_mes = (
    df_limpo
    .groupby("mes")["compra_id"]
    .count()
    .sort_index()
)

print(compras_por_mes)

# Geração da base limpa
df_limpo.to_csv("dados/varejo_limpo.csv", index=False)

print("\nArquivo limpo gerado:")
print("dados/varejo_limpo.csv")

print("\n" + "=" * 70)
print("RELATÓRIO FINAL DA ANÁLISE")
print("=" * 70)

print("Total de registros na base original:", df.shape[0])
print("Total de registros após limpeza:", df_limpo.shape[0])
print("Total de colunas após limpeza:", df_limpo.shape[1])
print("Colunas vazias removidas:", len(colunas_vazias))
print("Duplicatas encontradas antes da limpeza:", duplicatas_antes)
print("Duplicatas após a limpeza:", duplicatas_depois)
print("Categorias vazias ou inválidas tratadas:", categorias_invalidas)
print("Datas inválidas encontradas:", datas_invalidas)

print("\nCONCLUSÕES")
print("-" * 70)
print("1. A base foi carregada com 830000 registros e 14 colunas na estrutura original.")
print("2. Foram removidas 4 colunas totalmente vazias, pois não contribuíam para a análise.")
print("3. Foram identificados e removidos registros duplicados, reduzindo distorções nos resultados.")
print("4. Categorias inválidas foram tratadas como 'Sem Categoria', preservando os registros.")
print("5. A coluna de número de filhos foi analisada com média, mediana, desvio padrão, moda, máximo, mínimo e contagem.")
print("6. Os agrupamentos mostraram padrões de compras por categoria, gênero e mês.")
