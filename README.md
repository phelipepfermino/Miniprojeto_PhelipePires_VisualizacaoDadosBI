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

Miniprojeto_PhelipePires_VisualizacaoDadosBI/

├── dados/

│   ├── Varejo.csv

│   └── varejo_limpo.csv

├── src/

│   └── miniprojeto_varejo.py

├── README.md

└── README_PhelipePires_VisualizacaoDadosBI.md

## Organização por Sprints

### Sprint 1 - Importação dos dados

A base `Varejo.csv` foi carregada com pandas. Foram exibidos número de registros, número de colunas, nomes das colunas, tipos de dados e primeiras linhas.

### Sprint 2 - Transformação de strings, inteiros, floats e datas

Foram realizadas as seguintes transformações:

* Remoção de colunas totalmente vazias.
* Padronização dos nomes das colunas.
* Renomeação das colunas para nomes mais claros.
* Limpeza de espaços extras em textos.
* Conversão da coluna `data` para o tipo `datetime`.
* Conversão de colunas numéricas.

Renomeações principais:

| Nome original | Nome usado no projeto   |
| ------------- | ----------------------- |
| `CO_ID`       | `compra_id`             |
| `CL_ID`       | `cliente_id`            |
| `CL_GENERO`   | `cliente_genero`        |
| `CL_EC`       | `cliente_estado_civil`  |
| `CL_FHL`      | `cliente_numero_filhos` |
| `CL_SEG`      | `cliente_segmento`      |
| `PR_ID`       | `produto_id`            |
| `PR_CAT`      | `produto_categoria`     |
| `PR_NOME`     | `produto_nome`          |

### Sprint 3 - Limpeza de nulos e duplicatas

Foram verificados valores nulos, categorias inválidas e registros duplicados.

As categorias vazias ou inválidas foram substituídas por `"Sem Categoria"`. Os registros duplicados foram removidos para evitar contagens repetidas nas análises.

### Sprint 4 - Estatística descritiva

A coluna `cliente_numero_filhos` foi analisada para entender o perfil familiar dos clientes presentes na base.

| Estatística | Resultado |
|---|---:|
| Média | 1,15 |
| Mediana | 0 |
| Desvio padrão | 1,42 |
| Moda | 0 |
| Máximo | 4 |
| Mínimo | 0 |
| Contagem | 733447 |

A média de filhos foi de aproximadamente 1,15 por cliente/registro analisado. Porém, a mediana foi 0 e a moda também foi 0, indicando que o valor mais comum na base é cliente sem filhos.

O desvio padrão de aproximadamente 1,42 mostra que existe variação na quantidade de filhos, mas a maioria dos registros está concentrada em valores baixos. O maior valor encontrado foi 4 filhos.

Com isso, é possível observar que, nesta base, o perfil mais frequente é de clientes sem filhos, embora também existam registros de clientes com 1 a 4 filhos.

### Sprint 5 - Relatório e documentação

Foram criados agrupamentos usando `groupby()` para observar:

* quantidade de compras por categoria;
* quantidade de compras por gênero;
* quantidade de compras por mês.

Também foi gerado o arquivo `dados/varejo_limpo.csv`.

### Sprint 6 - Versionamento

O projeto foi enviado para um repositório público no GitHub.

## Resumo dos resultados

| Item analisado                          | Resultado |
| --------------------------------------- | --------: |
| Registros na base original              |    830000 |
| Colunas na base original                |        14 |
| Registros após limpeza                  |    733447 |
| Colunas após limpeza                    |        11 |
| Colunas vazias removidas                |         4 |
| Registros duplicados removidos          |     96553 |
| Categorias vazias ou inválidas tratadas |      3650 |
| Datas inválidas encontradas             |         0 |

## Interpretação dos tratamentos realizados

Durante a análise, foram identificadas quatro colunas totalmente vazias: `Unnamed: 10`, `Unnamed: 11`, `Unnamed: 12` e `Unnamed: 13`. Essas colunas foram removidas porque não possuíam informação útil para a análise.

Também foram encontrados registros duplicados. A remoção dessas duplicatas foi importante para evitar contagens repetidas nos agrupamentos por categoria, gênero e mês.

Na coluna `produto_categoria`, valores vazios ou inválidos foram tratados como `Sem Categoria`. Essa escolha permitiu preservar os registros na base, sem eliminar linhas que ainda possuíam outras informações relevantes.

A coluna `DATA` foi convertida para o tipo `datetime`, permitindo a criação da coluna `mes` e a análise das compras ao longo do tempo.

## Como executar

No terminal do VS Code, execute:

`pip install pandas`

Depois execute:

`python src/miniprojeto_varejo.py`

Se o comando `python` não funcionar, use:

`py src/miniprojeto_varejo.py`

## Reflexão sobre ETL e qualidade dos dados

ETL significa extrair, transformar e carregar dados.

Neste projeto, a extração ocorreu na leitura do arquivo `Varejo.csv`. A transformação aconteceu na padronização das colunas, na remoção de colunas vazias, na conversão de datas e números, no tratamento de categorias inválidas e na remoção de duplicatas. A etapa de carregamento foi representada pela geração do arquivo `varejo_limpo.csv`.

A qualidade dos dados é importante porque valores nulos, duplicatas, categorias inválidas ou tipos incorretos podem gerar análises erradas. Antes de criar relatórios ou dashboards, é necessário verificar e tratar a base.

## Insights obtidos

1. A base original possui 830000 registros. Após a remoção de duplicatas, a base limpa ficou com 733447 registros. Foram removidos 96553 registros duplicados, o que representa aproximadamente 11,63% da base original. Esse percentual mostra que havia uma quantidade relevante de registros repetidos, que poderiam distorcer a análise caso fossem mantidos.

2. A base limpa representa aproximadamente 88,37% da base original. Isso indica que a maior parte dos dados foi preservada após a limpeza, mas a etapa de remoção de duplicatas foi importante para tornar os agrupamentos mais confiáveis.

3. A categoria `ALIMENTOS` apresentou a maior quantidade de compras, com 384197 registros, representando aproximadamente 52,38% da base limpa. Porém, o ponto mais importante não é apenas dizer que alimentos teve mais compras, mas perceber que a base está muito concentrada em produtos de consumo recorrente.

4. Somando `ALIMENTOS`, `HIGIENE` e `LIMPEZA`, temos 650531 registros, o que representa aproximadamente 88,70% da base limpa. Isso mostra que quase 9 em cada 10 registros estão ligados a produtos essenciais ou de reposição frequente. Para um dashboard de BI, essas três categorias deveriam receber destaque especial, pois explicam quase todo o volume da base.

5. No agrupamento por gênero, os clientes do gênero feminino apresentaram 382427 compras, aproximadamente 52,14% da base limpa, enquanto os clientes do gênero masculino apresentaram 351020 compras, cerca de 47,86%. A diferença existe, mas não é extrema. Isso sugere que o comportamento de compra está mais relacionado ao tipo de produto e à recorrência das categorias do que a uma diferença muito forte entre gêneros.

6. A análise mensal mostrou que outubro de 2021 teve o maior volume de compras, com 28575 registros, aproximadamente 3,90% da base limpa. Já setembro de 2022 teve apenas 1297 registros, cerca de 0,18%. Essa queda merece investigação futura, pois pode indicar redução real de compras, falha de registro, mudança no período de coleta ou base incompleta nesse mês.