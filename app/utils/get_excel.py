import openpyxl
import io
import pandas as pd

def read_range_to_dataframe(dados_uplodad: io.BytesIO, cell_range: str) -> pd.DataFrame:
    workbook = openpyxl.load_workbook(dados_uplodad, data_only=True)
    sheet = workbook.active
    range_cells = sheet[cell_range]

    # Extrai os cabeçalhos das colunas da primeira linha
    headers = [cell.value for cell in range_cells[0]]

    # Extrai os dados das células restantes
    data = []
    for row in range_cells[1:]:  # Começa do segundo elemento (linha) pois o primeiro são os cabeçalhos
        data.append([cell.value for cell in row])

    # Cria um DataFrame com os dados
    df = pd.DataFrame(data, columns=headers)
    return df