# Running tests on the city_functions module

import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do cities like 'Bogota, Colombia' work?"""
        formatted_city = city_country('bogota', 'colombia')
        self.assertEqual(formatted_city, 'Bogota, Colombia')

    def test_city_country_pop(self):
        """Do cities like 'Motevideo, Uruguay Population: 1,381,000' work?"""
        formatted_city = city_country('montevideo', 'uruguay', '1,381,000')
        self.assertEqual(formatted_city, "Montevideo, Uruguay-- Population: 1,381,000")


unittest.main()
