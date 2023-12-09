import io
import sys
import time
import streamlit as st

class Dev:
    def __init__(self, spark, df):
        self.spark = spark
        self.df = df

    def display(self):
        st.title('Desenvolvedor')
        st.text('')

        command = st.text_area('Digite a operação que deseja realizar:', height=300)

        if command:
            try:
                progress = st.progress(0)
                for i in range(100):
                    progress.progress(i + 1)
                    time.sleep(0.01)

                old_stdout = sys.stdout
                sys.stdout = io.StringIO()

                exec(command)
                output = sys.stdout.getvalue()

                sys.stdout = old_stdout
                progress.empty()

                st.code(output, language='python')
            except Exception as e:
                sys.stdout = old_stdout
                progress.empty()

                st.write(f'Erro: {e}')
