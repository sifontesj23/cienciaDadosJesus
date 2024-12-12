import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Ciência de Dados")
st.title("PROUNI 2020")


df_ex=pd.DataFrame(np.random.randn(15,4),columns=["a","b","c","d"])
st.line_chart(df_ex)
st.bar_chart(df_ex)


fig, ax = plt.subplots()
ax.scatter(df_ex['a'],df_ex['b'])
ax.plot([0,2,5],[0,1,2],c='r')
st.pyplot(fig)



PROUNI = pd.read_csv('https://dadosabertos.mec.gov.br/arquivos/prouni/bolsista/pda-prouni-2016.csv',sep=';', encoding= 'latin-1')
st.dataframe(PROUNI.head())
#fig2, ax2 = plt.subplots()
#ax.scatter(PROUNI['ANO_CONSESAO_BOLSA'],PROUNI['CODIGO_EMEC_IES_BOLSA'])
#ax.plot([0,2,5],[0,1,2],c='r')
#st.pyplot(fig2)

#st.line_chart(PROUNI) 
#st.bar_chart(PROUNI)
#st.data_editor(PROUNI)

#PROUNI = pd.read_csv('Prouni2020.csv',  sep=';', encoding= 'latin-1' )
#PROUNI = pd.read_csv('/drive/MyDrive/cienciadados/TB_RH.csv')
#database_path, sep=';', encoding='latin-1



