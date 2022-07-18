import csv
import json
import pandas as pd
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def get_file_type(path):
        if 'csv' in path:
            with open(path, encoding="utf-8") as file:
                lista = csv.DictReader(file)
                lista_de_items = [item for item in lista]
                return lista_de_items

        elif 'json' in path:
            with open(path, encoding="utf-8") as file:
                lista = json.load(file)
                lista_de_items = [item for item in lista]
                return lista_de_items

        elif 'xml' in path:
            file = pd.read_xml(path)
            lista_de_items = file.to_dict('records')
            return lista_de_items

    @staticmethod
    def import_data(path, report):
        if report == "simples":
            lista = Inventory.get_file_type(path)
            return SimpleReport.generate(lista)
        elif report == 'completo':
            lista = Inventory.get_file_type(path)
            return CompleteReport.generate(lista)

lista = Inventory.import_data('inventory_report/data/inventory.csv','simples')
print(lista)