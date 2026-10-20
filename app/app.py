import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(
    page_title="Previsão de Receita de Filmes",
    page_icon="🎬",
    layout="wide"
)

st.title("Previsão de Receita de Filmes")
st.markdown("Projeto de portfólio — TMDB 5000 Movies | Análise de Dados")

@st.cache_data
def carregar_dados():
    df = pd.read_csv('../data/processed/tmdb_limpo.csv')
    return df

df = carregar_dados()

# Sidebar com filtros
st.sidebar.header("Filtros")
ano_min, ano_max = st.sidebar.slider(
    "Período de lançamento",
    int(df['release_year'].min()),
    int(df['release_year'].max()),
    (1990, 2016)
)

df_filtrado = df[
    (df['release_year'] >= ano_min) &
    (df['release_year'] <= ano_max)
]

# Métricas gerais
col1, col2, col3 = st.columns(3)
col1.metric("Total de Filmes", f"{len(df_filtrado):,}")
col2.metric("Receita Média", f"US$ {df_filtrado['revenue'].mean():,.0f}")
col3.metric("Orçamento Médio", f"US$ {df_filtrado['budget'].mean():,.0f}")

st.markdown("---")

# Gráfico 1 — Orçamento x Receita
st.subheader("Orçamento x Receita")
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.scatter(df_filtrado['budget'], df_filtrado['revenue'], alpha=0.4, s=15, color='#5b8bd0')
ax1.set_xlabel("Orçamento (USD)")
ax1.set_ylabel("Receita (USD)")
ax1.set_title("Relação entre Orçamento e Receita")
st.pyplot(fig1)
plt.close()

corr = df_filtrado['budget'].corr(df_filtrado['revenue'])
st.caption(f"Correlação de Pearson: {corr:.2f}")

st.markdown("---")

# Previsão de receita
st.subheader("Simule a Receita de um Filme")
st.markdown("Preencha as informações abaixo e veja a receita estimada pelo modelo.")

col_a, col_b, col_c = st.columns(3)
orcamento = col_a.number_input("Orçamento (USD)", min_value=1_000_000, max_value=400_000_000, value=50_000_000, step=1_000_000)
popularidade = col_b.number_input("Popularidade estimada", min_value=1.0, max_value=200.0, value=20.0, step=1.0)
nota = col_c.number_input("Nota esperada (0 a 10)", min_value=0.0, max_value=10.0, value=6.5, step=0.1)

# Treina modelo simples
X = df_filtrado[['budget', 'popularity', 'vote_average']].dropna()
y = df_filtrado.loc[X.index, 'revenue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
r2 = r2_score(y_test, modelo.predict(X_test))

entrada = np.array([[orcamento, popularidade, nota]])
previsao = modelo.predict(entrada)[0]

st.markdown("---")
col_res1, col_res2 = st.columns(2)
col_res1.metric("Receita Estimada", f"US$ {max(previsao, 0):,.0f}")
col_res2.metric("Lucro Estimado", f"US$ {max(previsao - orcamento, 0):,.0f}")
st.caption(f"Modelo: Regressão Linear | R² no conjunto de teste: {r2:.2f}")

st.markdown("---")
st.markdown("Projeto desenvolvido por: **Ygor Benicio**")
