from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        relatorio_simples = super().generate(data)
        empresas = [empresa["nome_da_empresa"] for empresa in data]

        produto_em_estoque = "Produtos estocados por empresa:\n"
        estoque = Counter(empresas).most_common()
        for produto in estoque:
            produto_em_estoque += f"- {produto[0]}: {produto[1]}\n"

        return(
            f"{relatorio_simples}\n"
            f"{produto_em_estoque}"
        )
