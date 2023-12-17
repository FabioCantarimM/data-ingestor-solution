from typing import Type
from pydantic import BaseModel
from utils.validador import validar_dados
from utils.get_excel import read_range_to_dataframe
import streamlit as st
import io
from utils.client import S3Client

def etl_excel_to_parquet(file: str, cell_range: str, schema: Type[BaseModel]):
    st.title(f"Inserir dados de catálogo {file}")

    dados_catalogo = st.file_uploader("Selecione o arquivo excel", type="xlsx", key=file)
    parquet_buffer = None  # Inicializa parquet_buffer com None

    if dados_catalogo:
        try:
            df = read_range_to_dataframe(dados_catalogo, cell_range)

            # Valida os dados
            bool_de_sucesso, mensagem_de_sucesso = validar_dados(df, schema)

            if bool_de_sucesso:
                st.success(mensagem_de_sucesso)
                parquet_buffer = io.BytesIO()
                df.to_parquet(parquet_buffer, index=False)
                parquet_buffer.seek(0)  # Volta ao início do buffer
                if parquet_buffer is not None:
                    if st.button(label="enviar"):
                        try: 
                            S3Client().upload_file(parquet_buffer, f"{file}.parquet")
                            st.success("Arquivo enviado com sucesso")
                        except Exception as e:
                            st.error(f"Ocorreu um erro: {e}")

            else:
                st.error(mensagem_de_sucesso)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")