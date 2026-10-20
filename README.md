# Previsão de Receita de Filmes — TMDB 5000 Movies

> Meu primeiro projeto de análise de dados, desenvolvido enquanto estudo Ciência de Dados.
> Usei dados públicos de filmes para aprender na prática como funciona um projeto real de dados do início ao fim.

---

## Por que fiz esse projeto?

Estou no início da minha jornada em Ciência de Dados e queria ir além dos exercícios de curso. Decidi pegar um dataset real, escolher um problema que fizesse sentido de verdade e tentar resolver do zero — exploração, limpeza, análise e visualização.

O tema filmes foi uma escolha intencional: os dados são ricos, intuitivos e qualquer pessoa consegue entender o contexto sem precisar de conhecimento técnico prévio.

Aprendi muito errando no caminho. Algumas células de código quebraram várias vezes antes de funcionar. Algumas decisões de limpeza precisei pesquisar bastante para entender o motivo. Esse README é um registro honesto do que foi feito e do que aprendi.

---

## O Problema

Um estúdio de cinema quer entender o que influencia a receita de um filme antes do lançamento — orçamento investido, gênero, época de lançamento — para tomar decisões mais embasadas sobre marketing e distribuição.

Usei dados reais de mais de 4.800 filmes do TMDB (The Movie Database) para investigar esse problema.

---

## Perguntas que quis Responder

- Filmes com maior orçamento faturam mais?
- Qual gênero de filme gera mais receita em média?
- A produção de filmes cresceu ao longo dos anos?
- Quais são os filmes mais lucrativos do dataset?
- Existe relação entre a nota do público e a receita?

---

## O que aprendi em cada etapa

### Exploração dos dados
Aprendi que antes de qualquer análise é preciso entender o que os dados têm — e o que está faltando. Descobri que colunas como `homepage` e `tagline` tinham mais de 60% de dados vazios, e que os zeros em `budget` e `revenue` não eram zeros de verdade, mas sim dados que não foram informados. Isso muda tudo na análise.

### Limpeza dos dados
Aprendi a diferença entre dado ausente real (`NaN`) e dado ausente disfarçado de zero. Aprendi também por que fazemos uma cópia do DataFrame antes de modificar — para não perder o original se algo der errado. O dataset passou de 4.803 para 3.229 filmes após a limpeza, o que foi esperado.

### Análise e visualizações
Aprendi a criar gráficos que respondem perguntas concretas, não apenas gráficos bonitos. A descoberta que mais me surpreendeu foi a fraca correlação entre nota do público e receita — um filme pode ser muito bem avaliado e faturar pouco, e vice-versa.

### App com Streamlit
Essa parte foi feita com auxílio de Inteligência Artificial. Ainda não tenho conhecimento suficiente para construir um app do zero sozinho, mas quis incluir porque o projeto fica mais completo com uma interface interativa. Entendi a lógica geral do que o código faz, mas não escreverei que construí essa parte sozinho.

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
│   ├── 01_exploracao.ipynb     # Exploração inicial
│   ├── 02_limpeza.ipynb        # Limpeza e tratamento
│   └── 03_analise.ipynb        # Análise e visualizações
│
├── sql/
│   └── perguntas.sql           # Consultas SQL sobre os dados
│
├── images/                     # Gráficos gerados pelos notebooks
│
├── app/
│   └── app.py                  # App Streamlit (desenvolvido com auxílio de IA)
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Principais Descobertas

| Pergunta | O que encontrei |
|---|---|
| Orçamento x Receita | Correlação de 0.73 — quanto mais se investe, maior a tendência de faturar mais, mas não é regra |
| Melhor gênero | Animação e Aventura lideram em receita média |
| Crescimento do mercado | Produção cresceu muito a partir dos anos 2000 |
| Mais lucrativos | Franquias dominam — Avatar, Star Wars e Marvel no topo |
| Nota x Receita | Correlação fraca de 0.17 — qualidade e bilheteria são coisas diferentes |

---

## Ferramentas que usei

- **Python** — foi minha principal ferramenta. Aprendi Pandas, NumPy, Matplotlib e Seaborn na prática aqui
- **SQL** — escrevi consultas para responder as mesmas perguntas de negócio com outra abordagem
- **Streamlit** — usado no app, com auxílio de IA
- **GitHub** — primeira vez versionando um projeto do início ao fim

---

## Dataset

- **Fonte:** [TMDB 5000 Movie Dataset — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Volume original:** 4.803 filmes e 20 colunas
- **Volume após limpeza:** 3.229 filmes e 19 colunas

---

## Como Rodar

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

Acesse [kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata), baixe `tmdb_5000_movies.csv` e coloque em `data/raw/`.

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

## Sobre mim

**Ygor Benicio de Siqueira**
Estudante de Engenharia de Computação — UNISUAM (previsão: 2030)
Cursando Profissão Cientista de Dados — EBAC

Esse é meu primeiro projeto de dados. Estou aprendendo, errando e melhorando. Feedbacks são bem-vindos.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ygor%20Benicio-blue)](https://www.linkedin.com/in/ygorbenicio)
[![GitHub](https://img.shields.io/badge/GitHub-YgorBenicio-black)](https://github.com/YgorBenicio)

---

## Referências

- [TMDB Movie Metadata — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
