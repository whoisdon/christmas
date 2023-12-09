import requests
import streamlit as st
import plotly.express as px

from pyspark.sql.functions import col, when
from bs4 import BeautifulSoup

class Graphics:
    def __init__(self, spark, df):
        self.spark = spark
        self.df = df

    def get_track_image(self, track_id):
        url = f"https://open.spotify.com/track/{track_id}"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        meta_tag = soup.find('meta', property='og:image')

        style = st.markdown(f"""
        <style>
        .card-container {{
            width: 300px;
            height: 300px;
            background-color: #13111b;
            border-radius: 9px;
            padding: 10px;
            box-shadow: 0px 15px 15px rgba(0, 0, 0, 0.2);
            margin-top: 129px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
        }}
        .card-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 10px;
        }}
        .card-wrapper p {{
            margin-left: 60px;
        }}
        .card-wrapper {{
            display: flex;
            align-items: center;
        }}
        </style>
        <div class="card-wrapper">
            <div class="card-container">
                <img src="{meta_tag['content']}" />
            </div>
        </div>
        """, unsafe_allow_html=True)

        return style

    def danceability(self, df):
        df = df.orderBy(df.danceability.desc())

        st.markdown("<h2 style='text-align: center;'>Músicas Mais Dançantes</h2>", unsafe_allow_html=True)
        st.bar_chart(df.select('danceability').toPandas(), height=300)

        df_pandas = df.select('track_name', 'danceability').toPandas()
        fig = px.bar(df_pandas, x='danceability', y='track_name', orientation='h', height=500, width=1200)

        st.plotly_chart(fig)

    def display(self):
        num_musicas = st.number_input('Digite o número de músicas que deseja verificar', min_value=1, max_value=self.df.count(), value=100)

        df = self.df.limit(num_musicas)
        df = df.withColumn("explicit", when(col("explicit") == False, False).otherwise(True))

        explicit_data = df.groupBy("explicit").count().collect()

        labels = ['Explícita' if row['explicit'] else 'Não explícita' for row in explicit_data]
        values = [row['count'] for row in explicit_data]

        fig = px.pie(values=values, names=labels, title='Porcentagem de Músicas Explícitas e Não Explícitas', color=labels, color_discrete_map={'Explícita':'blue', 'Não explícita':'lightblue'})

        album_names = df.select("album_name").distinct().rdd.flatMap(lambda x: x).collect()
        selected_album = st.selectbox('Selecione um álbum', album_names)
        df_album = df.filter(col("album_name") == selected_album)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Gráficos")
            st.plotly_chart(fig)

        with col2:
            track_id = df_album.select("track_id").collect()[0]["track_id"]
            self.get_track_image(track_id)

        self.danceability(df)
