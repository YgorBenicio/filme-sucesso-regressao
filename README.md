# Previsão de Receita de Filmes — TMDB 5000 Movies

> Meu primeiro projeto de análise de dados.  
> Estou estudando Ciência de Dados e resolvi pegar um dataset real pra tentar fazer um projeto do começo ao fim.

---

## Por que eu fiz isso?

Tô no começo da jornada ainda e não queria ficar só fazendo os exercícios dos cursos. Queria pegar um dataset de verdade, escolher um problema que fizesse algum sentido e tentar resolver sozinho (na medida do possível).

Escolhi filmes porque os dados são fáceis de entender e qualquer pessoa consegue se interessar pelo tema. Não precisa ser expert em cinema pra entender o que tá sendo analisado.

Errei bastante no caminho. Várias células quebraram, tive que pesquisar bastante coisa e algumas decisões de limpeza eu só entendi depois de um tempo. Esse README é mais um registro do que eu consegui fazer e do que eu aprendi (e do que ainda não sei muito bem).

---

## O problema

Imaginei a situação: um estúdio de cinema quer entender o que mais influencia a receita de um filme antes de lançar. Orçamento, gênero, época… coisas assim. Pra tentar tomar decisões melhores de marketing e distribuição.

Usei os dados do TMDB (mais de 4.800 filmes) pra tentar investigar isso.

---

## Perguntas que eu quis responder

- Filmes com orçamento maior realmente faturam mais?
- Qual gênero costuma gerar mais receita em média?
- A quantidade de filmes produzidos aumentou ao longo dos anos?
- Quais foram os filmes mais lucrativos nesse dataset?
- Tem alguma relação forte entre a nota do público e a receita?

---

## O que eu aprendi em cada parte

### Exploração
Antes de analisar qualquer coisa, precisa olhar bem os dados. Descobri que várias colunas (tipo `homepage` e `tagline`) tinham um monte de valor faltando. E os zeros em `budget` e `revenue` na verdade eram dados que não foram informados. Isso muda bastante a análise.

### Limpeza
Aprendi a diferença entre `NaN` de verdade e zero que tá “escondendo” dado faltante. Também aprendi a importância de fazer cópia do DataFrame antes de mexer, pra não estragar o original. Depois da limpeza o dataset ficou com 3.229 filmes (antes tinha 4.803).

### Análise e gráficos
Tentei fazer gráficos que respondessem as perguntas, não só gráficos bonitos. A coisa que mais me surpreendeu foi a correlação fraca entre nota do público e receita (só 0.17). Ou seja, filme bem avaliado não necessariamente fatura muito, e o contrário também acontece.

### App com Streamlit
Essa parte eu fiz com bastante ajuda de IA. Ainda não consigo construir um app sozinho do zero. Quis colocar mesmo assim porque o projeto fica mais completo com uma interface. Entendi a lógica geral do código, mas não vou fingir que fiz tudo sozinho.

---

## Estrutura do projeto

```
filme-sucesso-regressao/
│
├── data/
│   ├── raw/          # dataset original (não versionado)
│   └── processed/    # dataset limpo
│
├── notebooks/
│   ├── 01_exploracao.ipynb
│   ├── 02_limpeza.ipynb
│   └── 03_analise.ipynb
│
├── sql/
│   └── perguntas.sql
│
├── images/           # gráficos que eu gerei
│
├── app/
│   └── app.py        # feito com ajuda de IA
│
├── requirements.txt
├── .gitignore
└── README.md
```

---


---

## Principais descobertas

| Pergunta            | O que eu encontrei                                              |
|---------------------|-----------------------------------------------------------------|
| Orçamento x Receita | Correlação de 0.73 — quanto mais investe, maior a tendência de faturar, mas não é regra |
| Melhor gênero       | Animação e Aventura ficaram na frente em receita média          |
| Crescimento         | A produção de filmes cresceu bastante a partir dos anos 2000    |
| Mais lucrativos     | Franquias dominam (Avatar, Star Wars, Marvel…)                  |
| Nota x Receita      | Correlação bem fraca (0.17) — qualidade e bilheteria são coisas diferentes |

---

## Ferramentas que usei

- **Python** (Pandas, NumPy, Matplotlib e Seaborn) — aprendi bastante na prática
- **SQL** — escrevi umas consultas pras mesmas perguntas
- **Streamlit** — no app (com ajuda de IA)
- **GitHub** — primeira vez versionando um projeto completo

---

## Dataset

- Fonte: [TMDB 5000 Movie Dataset no Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Original: 4.803 filmes e 20 colunas
- Depois da limpeza: 3.229 filmes e 19 colunas

---

```

---

## Sobre mim

Sobre mim
Ygor Benicio de Siqueira

Estudante de Engenharia de Computação — UNISUAM (previsão de formatura: 2030)

Cursando Profissão Cientista de Dados — EBAC
Esse é meu primeiro projeto de dados de verdade. Ainda tô aprendendo, errando e tentando melhorar. Qualquer feedback é bem-vindo.

---

## Referências

- [TMDB Movie Metadata — Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
