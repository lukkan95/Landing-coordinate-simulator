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
                raw = re.sub('\n', '', row)
                temp_list = []
                for elem in raw.split(','):
                    temp_list.append(round(float(elem), 3))
                dlmread.append(temp_list)
            return dlmread


coordinates = Coordinates()

range_limits = coordinates.csv_files_open(ustka_granice_poligonu)
smaller_range_limits = coordinates.csv_files_open(ustka_granice_poligonu2)
range_shore = coordinates.csv_files_open(ustka_lad)
range_sea_limits = coordinates.csv_files_open(ustka_strefa_morska)



