# Previsão de Receita de Filmes — TMDB 5000 Movies

> Análise exploratória e previsão de receita de filmes usando dados públicos do TMDB.
> Projeto de portfólio desenvolvido em equipe para vaga de estágio em Ciência de Dados.

---

## Contexto de Negócio

Um estúdio de cinema precisa decidir quanto investir em marketing e distribuição antes de lançar um filme. Para isso, quer entender quais fatores influenciam a receita — orçamento, gênero, época de lançamento — e ser capaz de estimar o retorno financeiro de uma produção antes que ela chegue às telas.

Este projeto simula exatamente esse cenário usando dados reais de mais de 4.800 filmes catalogados pelo TMDB (The Movie Database).

---

## Perguntas de Negócio

- Filmes com maior orçamento faturam mais?
- Qual gênero de filme gera mais receita em média?
- A produção de filmes cresceu ao longo dos anos?
- Quais são os filmes mais lucrativos do dataset?
- Existe relação entre a nota do público e a receita?

---

## Estrutura do Projeto

```
filme-sucesso-regressao/
│
├── data/
│   ├── raw/                    # Dataset original do Kaggle (não versionado)
│   └── processed/              # Dataset limpo gerado pelo notebook 02
│
├── notebooks/
│   ├── 01_exploracao.ipynb     # Exploração inicial — estrutura e problemas dos dados
│   ├── 02_limpeza.ipynb        # Limpeza e tratamento dos dados
│   └── 03_analise.ipynb        # Análise exploratória e resposta às perguntas
│
├── sql/
│   └── perguntas.sql           # Consultas SQL sobre os dados do projeto
│
├── images/                     # Gráficos gerados pelos notebooks
│
├── app/                        # Deploy do modelo (em desenvolvimento)
│
├── .gitignore
└── README.md
```

---

## Principais Descobertas

| Pergunta | Resultado |
|---|---|
| Orçamento x Receita | Correlação positiva moderada (~0.73) — maior investimento tende a gerar mais retorno, mas não é garantia |
| Melhor gênero | Animação e Aventura lideram em receita média |
| Crescimento do mercado | Produção cresceu significativamente a partir dos anos 2000 |
| Mais lucrativos | Avatar, Star Wars e franquias da Marvel dominam o top 10 |
| Nota x Receita | Correlação fraca — qualidade não garante bilheteria |

---

## Ferramentas Utilizadas

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **SQL** — consultas analíticas sobre os dados limpos
- **Power BI** — dashboard interativo (em desenvolvimento)
- **GitHub** — versionamento e colaboração em equipe

---

## Dataset

- **Fonte:** [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Volume original:** 4.803 filmes e 20 colunas
- **Volume após limpeza:** 3.229 filmes e 19 colunas
- **Remoções:** filmes sem orçamento ou receita registrados, colunas sem relevância analítica

---

## Como Rodar o Projeto

**1. Clone o repositório**
```bash
git clone https://github.com/YgorBenicio/filme-sucesso-regressao.git
cd filme-sucesso-regressao
```

**2. Instale as dependências**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

**3. Baixe o dataset**

Acesse [kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), baixe o arquivo `tmdb_5000_movies.csv` e coloque em `data/raw/`.

**4. Execute os notebooks na ordem**
```
01_exploracao.ipynb → 02_limpeza.ipynb → 03_analise.ipynb
```

---

## Equipe e Contribuições

| Integrante | Contribuição |
|---|---|
| **Ygor Benicio** | Liderança técnica, estrutura do repositório, notebooks de exploração, limpeza e análise |
| **Luís** | Consultas SQL e análise por perguntas de negócio |
| **Gabriel** | Visualizações no Power BI e dashboard |
| **Arthur** | Documentação, README e revisão geral |

---

## Referências

- [TMDB Movie Metadata — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
