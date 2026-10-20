# Previsão de Receita de Filmes — TMDB 5000 Movies

> Análise exploratória e previsão de receita de filmes usando dados públicos do TMDB.
> Projeto de portfólio individual desenvolvido para vaga de estágio em Ciência de Dados.

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
│   ├── 01_orcamento_x_receita.png
│   ├── 02_receita_por_genero.png
│   ├── 03_filmes_por_ano.png
│   ├── 04_top10_lucro.png
│   └── 05_nota_x_receita.png
│
├── app/
│   └── app.py                  # App interativo com Streamlit
│
├── requirements.txt
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
| Nota x Receita | Correlação fraca (~0.17) — qualidade não garante bilheteria |

---

## Ferramentas Utilizadas

- **Python** — Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **SQL** — consultas analíticas sobre os dados limpos
- **Streamlit** — deploy do modelo como app web interativo
- **GitHub** — versionamento do projeto

---

## Dataset

- **Fonte:** [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Volume original:** 4.803 filmes e 20 colunas
- **Volume após limpeza:** 3.229 filmes e 19 colunas
- **Remoções:** filmes sem orçamento ou receita registrados e colunas sem relevância analítica

---

## Como Rodar o Projeto

**1. Clone o repositório**
```bash
git clone https://github.com/YgorBenicio/filme-sucesso-regressao.git
cd filme-sucesso-regressao
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Baixe o dataset**

Acesse [kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), baixe o arquivo `tmdb_5000_movies.csv` e coloque em `data/raw/`.

**4. Execute os notebooks na ordem**
```
01_exploracao.ipynb → 02_limpeza.ipynb → 03_analise.ipynb
```

**5. Rode o app**
```bash
cd app
python -m streamlit run app.py
```

---

## Sobre o Projeto

Desenvolvido por **Ygor Benicio de Siqueira**
Estudante de Engenharia de Computação — UNISUAM
Cursando Profissão Cientista de Dados — EBAC

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ygor%20Benicio-blue)](https://www.linkedin.com/in/ygorbenicio)
[![GitHub](https://img.shields.io/badge/GitHub-YgorBenicio-black)](https://github.com/YgorBenicio)

---

## Referências

- [TMDB Movie Metadata — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
