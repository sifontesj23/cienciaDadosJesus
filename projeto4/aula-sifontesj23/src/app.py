import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Títulos
st.title("Ciência de Dados")
st.header("Trabalho 4º Bimestre -Variáveis dummy - Clusterização com K-Means")

# Carregando o arquivo CSV
url = 'https://dadosabertos.mec.gov.br/arquivos/prouni/bolsista/pda-prouni-2016.csv'
#url = pd.read_csv('/drive/MyDrive/cienciadados/TB_RH.csv')
try:
    PROUNI = pd.read_csv(url, sep=';', encoding='latin-1')
    st.write("Visualizando os primeiros 10 registros do dataset PROUNI:")
    st.dataframe(PROUNI.head())
except Exception as e:
    st.error("Erro ao carregar os dados. Verifique o URL ou o formato do arquivo.")
    st.stop()

# Selecionando colunas categóricas
quali = [ 'REGIAO_BENEFICIARIO_BOLSA','RACA_BENEFICIARIO_BOLSA']



# Transformando colunas categóricas em dummies
PROUNI_dummies = pd.get_dummies(PROUNI[quali])


st.write("Colunas transformadas em variáveis dummy:", quali)
st.dataframe(PROUNI_dummies.head())

#Aplicando o algoritmo K-Means
st.write("Aplicando o algoritmo K-Means")
x = PROUNI_dummies.values
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(x)
#x2 = PROUNI_dummies2.values
#kmeans = KMeans(n_clusters=5, random_state=42)
#kmeans.fit(x2)
 

# Plotando os clusters com os dois primeiros atributos
fig, ax = plt.subplots()


plt.scatter(# plota os pontos
    x[:, 0], x[:, 1], #x e y
    c = kmeans.labels_, #cores de acordo com o grupo
   marker='o', # pontos com 'o'
    edgecolor='black', #cor da borda
    cmap='rainbow', #esquema de cores
    s=100 #tamanho
    )
# Adicionando os centróides

plt.scatter(# plota os centróides
     kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1],#x e y
   c='white',  #cor fixa
    marker='*', #pontos marcados com estrela
    edgecolor='black', #cor da borda
    s=100 #tamanho
)

#ax.set_title("Clusterização com K-Means (usando os dois primeiros atributos)")
#ax.legend()
st.pyplot(fig)


###################SEGUNDO TESTE##############################################################

st.header("Segundo teste, usando mais atributos")

#quali2 = ['NOME_IES_BOLSA', 'TIPO_BOLSA','MODALIDADE_ENSINO_BOLSA','NOME_CURSO_BOLSA','NOME_TURNO_CURSO_BOLSA',
 #       'SEXO_BENEFICIARIO_BOLSA','RACA_BENEFICIARIO_BOLSA','BENEFICIARIO_DEFICIENTE_FISICO','REGIAO_BENEFICIARIO_BOLSA',
  #      'SIGLA_UF_BENEFICIARIO_BOLSA','MUNICIPIO_BENEFICIARIO_BOLSA']
quali2 = ['TIPO_BOLSA','NOME_CURSO_BOLSA','NOME_TURNO_CURSO_BOLSA',
        'SEXO_BENEFICIARIO_BOLSA','RACA_BENEFICIARIO_BOLSA','BENEFICIARIO_DEFICIENTE_FISICO',
        'SIGLA_UF_BENEFICIARIO_BOLSA']

PROUNI_dummies2 = pd.get_dummies(PROUNI[quali2])
st.write("Colunas transformadas em variáveis dummy:")
st.dataframe(PROUNI_dummies2.head())



# Aplicando o algoritmo K-Means
st.write("Aplicando o algoritmo K-Means para o segundo teste")
x2 = PROUNI_dummies2.values  # Dados para o segundo teste
kmeans2 = KMeans(n_clusters=6, random_state=42)  # Escolhendo 3 clusters
kmeans2.fit(x2)

# Redução da dimensionalidade para 2D com PCA
pca = PCA(n_components=2)
x2_pca = pca.fit_transform(x2)

# Plotando os clusters com as duas primeiras componentes principais
fig2, ax2 = plt.subplots()

# Plota os pontos com as cores indicadas pelos clusters
plt.scatter(x2_pca[:, 0], x2_pca[:, 1], 
            c=kmeans2.labels_, 
            marker='o', 
            edgecolor='black', 
            cmap='rainbow', 
            s=100)

# Adicionando os centróides do K-Means
centroids_pca = pca.transform(kmeans2.cluster_centers_)
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], 
            c='white', 
            marker='*', 
            edgecolor='black', 
            s=200)

# Título para o gráfico
plt.title("Clusterização com K-Means (usando todas as colunas transformadas)")

# Exibindo o gráfico gerado
st.pyplot(fig2)


