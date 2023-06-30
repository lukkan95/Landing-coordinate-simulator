import unittest
from Application import geo2ecef, ecef2geo, enu2geo, geo2enu


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.percentage_difference = 2.0

    def test_ecef2geo_geo2ecef(self):
        data = [1.0, 1.0, 1.0]
        ecef2geo_conversion = ecef2geo.ecef2geo(data)
        geo2ecef_conversion = geo2ecef.geo2ecef(ecef2geo_conversion)
        for i in range(len(geo2ecef_conversion)):
            assert 100 - (geo2ecef_conversion[i]/data[i]) * 100 <= self.percentage_difference

    def test_geo2ecef_ecef2geo(self):
        data = [1.0, 1.0, 1.0]
        geo2ecef_conversion = geo2ecef.geo2ecef(data)
        ecef2geo_conversion = ecef2geo.ecef2geo(geo2ecef_conversion)

        for i in range(len(ecef2geo_conversion)):
            assert 100 - (ecef2geo_conversion[i]/data[i]) * 100 <= self.percentage_difference

    def test_enu2geo_geo2enu(self):
        data_1 = [1.0, 1.0, 1.0]
        data_2 = [1.0, 1.0, 1.0]
        enu2geo_conversion = enu2geo.enu2geo(data_1, data_2)
        geo2enu_conversion = geo2enu.geo2enu(enu2geo_conversion, data_2)
        temp_list_y = []
        for i in geo2enu_conversion.flatten():
            temp_list_y.append(i)
        for i in range(len(data_1)):
            assert 100 - (temp_list_y[i] / data_1[i]) * 100 <= self.percentage_difference

    def test_geo2enu_enu2geo(self):
        data_1 = [1.0, 1.0, 1.0]
        data_2 = [1.0, 1.0, 1.0]
        geo2enu_conversion = geo2enu.geo2enu(data_1, data_2)
        enu2geo_conversion = enu2geo.enu2geo(geo2enu_conversion, data_2)
        print(enu2geo_conversion)
        temp_list_y = []
        print(enu2geo_conversion)
        for i in enu2geo_conversion.flatten():
            temp_list_y.append(i)
        for i in range(len(data_1)):
            assert 100 - (temp_list_y[i] / data_1[i]) * 100 <= self.percentage_difference


test = Test()

