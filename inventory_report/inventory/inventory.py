import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport

class Inventory():
    @staticmethod
    def import_data(csv_data,report):
        if report == "simples":
            with open(csv_data, encoding="utf-8") as file:
                lista = csv.DictReader(file)
                lista_de_items = [item for item in lista]
                return SimpleReport.generate(lista_de_items)

        elif report == 'completo':
            with open(csv_data, encoding="utf-8") as file:
                lista = csv.DictReader(file)
                lista_de_items_completa = [item for item in lista]
                return CompleteReport.generate(lista_de_items_completa)
