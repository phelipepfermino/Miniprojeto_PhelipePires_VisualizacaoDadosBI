# Mini-Projeto Avaliativo - Análise Exploratória da Base Varejo

## Aluno

Phelipe Pires

## Turma

Visualização de Dados e BI

## Objetivo

Este projeto realiza uma Análise Exploratória de Dados da base Varejo, com foco em importação, verificação de qualidade, limpeza, transformação, estatística descritiva e agrupamentos.

## Base utilizada

A base utilizada foi `Varejo.csv`.

A base original possui 830000 registros e 14 colunas. Durante a análise, 4 colunas totalmente vazias foram removidas, pois não contribuíam para o estudo.

## Estrutura do projeto

```text
Miniprojeto_PhelipePires_VisualizacaoDadosBI/
│
├── dados/
│   ├── Varejo.csv
│   └── varejo_limpo.csv
│
├── src/
│   └── miniprojeto_varejo.py
│
├── README.md
└── README_PhelipePires_VisualizacaoDadosBI.md
```

## Organização por Sprints

### Sprint 1 - Importação dos dados

A base `Varejo.csv` foi carregada com pandas. Foram exibidos número de registros, número de colunas, nomes das colunas, tipos de dados e primeiras linhas.

### Sprint 2 - Transformação de strings, inteiros, floats e datas

Foram realizadas as seguintes transformações:

- Remoção de colunas totalmente vazias.
- Padronização dos nomes das colunas.
- Renomeação das colunas para nomes mais claros.
- Limpeza de espaços extras em textos.
- Conversão da coluna `data` para o tipo `datetime`.
- Conversão de colunas numéricas.

Renomeações principais:

| Nome original | Nome usado no projeto |
|---|---|
| `CO_ID` | `compra_id` |
| `CL_ID` | `cliente_id` |
| `CL_GENERO` | `cliente_genero` |
| `CL_EC` | `cliente_estado_civil` |
| `CL_FHL` | `cliente_numero_filhos` |
| `CL_SEG` | `cliente_segmento` |
| `PR_ID` | `produto_id` |
| `PR_CAT` | `produto_categoria` |
| `PR_NOME` | `produto_nome` |

### Sprint 3 - Limpeza de nulos e duplicatas

Foram verificados valores nulos, categorias inválidas e registros duplicados.

As categorias vazias ou inválidas foram substituídas por `"Sem Categoria"`. Os registros duplicados foram removidos para evitar contagens repetidas nas análises.

### Sprint 4 - Estatística descritiva

A coluna `cliente_numero_filhos` foi analisada com:

- média;
- mediana;
- desvio padrão;
- moda;
- máximo;
- mínimo;
- contagem.

### Sprint 5 - Relatório e documentação

Foram criados agrupamentos usando `groupby()` para observar:

- quantidade de compras por categoria;
- quantidade de compras por gênero;
- quantidade de compras por mês.

Também foi gerado o arquivo `dados/varejo_limpo.csv`.

### Sprint 6 - Versionamento

O projeto deve ser enviado para um repositório público no GitHub.

## Como executar

No terminal do VS Code, execute:

```bash
pip install pandas
```

Depois execute:

```bash
python src/miniprojeto_varejo.py
```

Se o comando `python` não funcionar, use:

```bash
py src/miniprojeto_varejo.py
```

## Reflexão sobre ETL e qualidade dos dados

ETL significa extrair, transformar e carregar dados.

Neste projeto, a extração ocorreu na leitura do arquivo `Varejo.csv`. A transformação aconteceu na padronização das colunas, na remoção de colunas vazias, na conversão de datas e números, no tratamento de categorias inválidas e na remoção de duplicatas. A etapa de carregamento foi representada pela geração do arquivo `varejo_limpo.csv`.

A qualidade dos dados é importante porque valores nulos, duplicatas, categorias inválidas ou tipos incorretos podem gerar análises erradas. Antes de criar relatórios ou dashboards, é necessário verificar e tratar a base.

## Insights obtidos

1. A base original possui grande volume de registros, com 830000 linhas.
2. Foram encontradas 4 colunas totalmente vazias, que foram removidas.
3. Foram identificados registros duplicados, que foram removidos da base limpa.
4. A categoria `ALIMENTOS` apresentou a maior quantidade de compras.
5. O agrupamento por gênero permitiu comparar o volume de compras entre clientes femininos e masculinos.
6. A análise por mês mostrou a distribuição das compras ao longo do tempo.
