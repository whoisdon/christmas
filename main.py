import streamlit as st

from pages.developer import Dev
from pages.graphics import Graphics
from pyspark.sql import SparkSession
from pages.introduction import Introduction
from utils.christmas import christmas

st.set_page_config(
    page_title="Rinha de backend",
    page_icon="🎅",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = ['Introdução', 'Gráficos', 'Opções do Desenvolvedor']
page = st.sidebar.selectbox('Guia', pages)

spark = SparkSession.builder.appName('Rinha').getOrCreate()
df = spark.read.csv('./utils/spotify.csv', header=True, inferSchema=True)

if page == 'Introdução':
    introduction = Introduction(spark, df)
    introduction.display()
elif page == 'Gráficos':
    graphics = Graphics(spark, df)
    graphics.display()
elif page == 'Opções do Desenvolvedor':
    dev = Dev(spark, df)
    dev.display()

christmas()
