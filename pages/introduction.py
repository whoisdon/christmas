import time
import streamlit as st
import matplotlib.pyplot as plt

from pyspark.sql.functions import col, round

class Introduction:
    def __init__(self, spark, df):
        self.spark = spark
        self.df = df

    def display(self):
        st.title('Introdução ao PySpark'); st.text('')

        st.text('Para iniciar uma sessão no PySpark, empregamos o seguinte comando:')
        st.code("""
        spark = SparkSession.builder.appName('Rinha').getOrCreate()
        """, language='python')

        if st.button('Criar uma sessão spark'):
            st.success('Sessão spark criada com sucesso.')

        st.text('Para carregar um DataFrame, empregamos o seguinte comando:')
        st.code("""
        df = spark.read.csv('spotify.csv', header=True, inferSchema=True)
        df.show()
        """, language='python')

        if st.button('Carregar DataFrame'):
            with st.spinner('Carregando dados...'):
                st.dataframe(self.df.toPandas())
                msg = st.success('Dados carregados com sucesso.')
                time.sleep(10)
                msg.empty()

        st.text('Para obter as 10 músicas com a maior duração, empregamos o seguinte comando:')
        st.code("""
        top_10 = df.orderBy(df.duration_ms.desc()).limit(10)
        top_10.show()
        """, language='python')

        col1, col2 = st.columns(2)
        top_10 = self.df.orderBy(self.df.duration_ms.desc()).limit(10)

        with col1:
            if st.button('Mostrar as 10 músicas com maior duração (em ms)'):
                with st.spinner('Carregando dados...'):
                    st.dataframe(top_10.toPandas())
                suc = st.success('Dados carregados com sucesso.')
                time.sleep(10)
                suc.empty()

        with col2:
            if st.button('Mostrar gráfico de música com maior duração (em ms)'):
                with st.spinner('Gerando gráfico...'):
                    plt.figure(figsize=(12, 10))
                    plt.barh(top_10.toPandas()['track_name'], top_10.toPandas()['duration_ms'])
                    plt.xlabel('Duração em ms')
                    plt.ylabel('Nome da música')
                    plt.title('10 músicas mais tocadas')
                    st.pyplot(plt)
                st.success('Gráfico gerado com sucesso.')

        st.text('Para obter as 10 músicas mais populares, empregamos o seguinte comando:')
        st.code("""
        # Filtra apenas para string usando regex
        df = df.filter(col("track_genre").rlike('^[a-zA-Z\s]*$'))

        # Obtém todos os gêneros, converte em RDD e coleta
        genres = df.select("track_genre").distinct().rdd.flatMap(lambda x: x).collect()

        # Cria um selectbox
        selected_genre = st.selectbox('Selecione um gênero', genres)

        # Filtra apenas para o gênero selecionado
        top_songs_genre = df.filter(df.track_genre == selected_genre).orderBy(df.popularity.desc()).limit(10)

        # Exibe o DataFrame
        st.dataframe(top_songs_genre.toPandas())
        """, language='python')

        df = self.df.filter(col("track_genre").rlike('^[a-zA-Z\s]*$'))
        genres = df.select("track_genre").distinct().rdd.flatMap(lambda x: x).collect()
        selected_genre = st.selectbox('Selecione um gênero', genres)
        top_songs_genre = df.filter(df.track_genre == selected_genre).orderBy(df.popularity.desc()).limit(10)

        if st.button('Mostrar as 10 músicas mais populares do gênero ' + selected_genre):
            with st.spinner('Carregando dados...'):
                st.dataframe(top_songs_genre.toPandas())
            st.success('Dados carregados com sucesso.')
