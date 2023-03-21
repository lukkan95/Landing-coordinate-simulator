import re

ustka_granice_poligonu = 'ustka_granice_poligonu.csv'
ustka_granice_poligonu2 = 'ustka_granice_poligonu2.csv'
ustka_lad = "ustka_lad.csv"
ustka_strefa_morska = "ustka_strefa_morska.csv"

class Coordinates(object):

    @staticmethod
    def csv_files_open(file):
        with open(file, 'r') as temporary_csv:
            dlmread = []
            for row in temporary_csv:
                dlmread.append(re.sub('\n', '', row))
            return dlmread


coordinates = Coordinates()

range_limits = coordinates.csv_files_open(ustka_granice_poligonu)
smaller_range_limits = coordinates.csv_files_open(ustka_granice_poligonu2)
range_shore = coordinates.csv_files_open(ustka_lad)
range_sea_limits = coordinates.csv_files_open(ustka_strefa_morska)



