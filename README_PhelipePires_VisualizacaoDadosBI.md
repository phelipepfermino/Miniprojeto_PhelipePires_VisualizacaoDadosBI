# Instruções de execução

## Aluno

Phelipe Pires

## Turma

Visualização de Dados e BI

## Projeto

Mini-Projeto Avaliativo - Análise Exploratória da Base Varejo

## Como abrir

Abra a pasta `Miniprojeto_PhelipePires_VisualizacaoDadosBI` no VS Code.

## Instalação da biblioteca necessária

No terminal do VS Code, execute:

```bash
pip install pandas
```

## Como executar o script

No terminal do VS Code, execute:

```bash
python src/miniprojeto_varejo.py
```

Caso o comando acima não funcione, execute:

```bash
py src/miniprojeto_varejo.py
```

## Resultado esperado

O script irá:

1. carregar a base `Varejo.csv`;
2. mostrar quantidade de registros e colunas;
3. mostrar os tipos de dados;
4. remover colunas vazias;
5. padronizar e renomear colunas;
6. verificar valores nulos;
7. verificar registros duplicados;
8. tratar categorias inválidas com `"Sem Categoria"`;
9. converter a coluna de data para `datetime`;
10. calcular estatísticas da coluna `cliente_numero_filhos`;
11. criar agrupamentos por categoria, gênero e mês;
12. gerar o arquivo `dados/varejo_limpo.csv`;
13. exibir conclusões no terminal.

## Arquivo principal

```text
src/miniprojeto_varejo.py
```

## Arquivo limpo gerado

```text
dados/varejo_limpo.csv
```

## Entrega

O projeto deve ser entregue por meio do link do repositório público no GitHub.
