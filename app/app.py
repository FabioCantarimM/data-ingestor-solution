import streamlit as st
from contract.product_schema import ProdutoSchema
from contract.store_schema import StoreSchema
from dotenv import load_dotenv
from etl.etl import etl_excel_to_parquet


load_dotenv()

st.title("Meu portal de dados")

etl_excel_to_parquet("catalogo", "C11:I211", ProdutoSchema)

etl_excel_to_parquet("loja", "A1:E11", StoreSchema)