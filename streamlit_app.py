import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
@st.cache
def load_data():
    data = pd.read_csv('IMDB-Movie-Data.csv')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = load_data()

if 'Title' in data.columns:
    selected_movie = st.selectbox('Selecciona una película', data['Title'].unique())
else:
    st.error('La columna "Title" no existe en el DataFrame.')
# Título de la aplicación
st.title('Visualizador de Películas')

# Selección de película
selected_movie = st.selectbox('Selecciona una película', data['Title'].unique())

# Mostrar información de la película seleccionada
movie_data = data[data['Title'] == selected_movie]
st.write('Descripción:', movie_data['Description'].iloc[0])
st.write('Director:', movie_data['Director'].iloc[0])
st.write('Actores:', movie_data['Actors'].iloc[0])
st.write('Año:', movie_data['Year'].iloc[0])
st.write('Duración:', movie_data['Runtime (Minutes)'].iloc[0], 'minutos')
st.write('Calificación:', movie_data['Rating'].iloc[0])
st.write('Votos:', movie_data['Votes'].iloc[0])
st.write('Ingresos (Millones): $', movie_data['Revenue (Millions)'].iloc[0])
st.write('Metascore:', movie_data['Metascore'].iloc[0])

# Gráfico de películas por año
st.subheader('Número de Películas por Año')
fig, ax = plt.subplots()
data['Year'].value_counts().sort_index().plot(kind='bar', ax=ax)
ax.set_xlabel('Año')
ax.set_ylabel('Número de Películas')
ax.set_title('Películas por Año de Estreno')
st.pyplot(fig)
