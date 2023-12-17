import pandas as pd
from typing import Tuple, Type
from pydantic import BaseModel

def validar_dados(dataframe: pd.DataFrame, schema: Type[BaseModel]) -> Tuple[bool, str]:

    erros = []

    for index, row in dataframe.iterrows():
        try:
            schema(**row.to_dict())
        except Exception as e:
            erros.append(f"Erro na linha {index+1}: {e}")

    if erros:
        return False, str(erros)

    return True, "Todos os arquivos validados"