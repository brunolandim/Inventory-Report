import csv
import json
import xml.etree.ElementTree as ET
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

        elif "xml" in path:
            with open(path, encoding='utf-8') as file:
                root = ET.parse(file).getroot()
                return [
                    {child.tag: child.text for child in item}
                    for item in root.findall('record')
                ]

    @staticmethod
    def import_data(path, report):
        if report == "simples":
            lista = Inventory.get_file_type(path)
            return SimpleReport.generate(lista)
        elif report == 'completo':
            lista = Inventory.get_file_type(path)
            return CompleteReport.generate(lista)
