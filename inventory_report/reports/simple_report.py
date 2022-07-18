from datetime import datetime
from typing import Counter


class SimpleReport():
    def generate(data):
        data_fabricacao = []
        data_vencido = []
        data_de_hoje = datetime.now().strftime("%Y-%m-%d")
        empresas = []

        for item in data:
            if item["data_de_fabricacao"]:
                data_fabricacao.append(item["data_de_fabricacao"])
            if item["data_de_validade"] > data_de_hoje:
                data_vencido.append(item["data_de_validade"])
            if item["nome_da_empresa"]:
                empresas.append(item["nome_da_empresa"])

        contador = print(Counter(empresas).most_common()[0][0])

        return [
            f"Data de fabricação mais antiga: {min(data_fabricacao)}\n"
            f"Data de fabricação mais antiga: {min(data_vencido)}\n"
            f"Data de fabricação mais antiga: {contador}\n"
        ]
