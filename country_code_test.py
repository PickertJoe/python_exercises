# A test for the country_code function

import unittest
from country_code import code_search


class CodeTestCase(unittest.TestCase):
    """Tests the functioning of the code_search funciton"""

    def test_code_search(self):
        """Will code_search generate the proper codes for Libya, Russia, and Germany?"""
        libya_code = code_search('Libya')
        russia_code = code_search('Russian Federation')
        germany_code = code_search('Germany')
        self.assertEqual(libya_code, 'ly')
        self.assertEqual(russia_code, 'ru')
        self.assertEqual(germany_code, 'de')


unittest.main()
