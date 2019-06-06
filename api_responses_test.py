# A program to test if api_responses.py made its API calls successfully

import unittest
from api_responses import read_API


class APITestCase(unittest.TestCase):
    """Ensures that the status code is equal to 200"""

    def teststatuscode(self):
        """Calling the read_API function from api_responses.py"""
        r = read_API()
        self.assertEqual(r.status_code, 200)


unittest.main()
