import unittest
from python_repos import *

class TestAPICall(unittest.TestCase):
    def test_API_call(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers = headers)
        self.assertEqual(200, r.status_code)


if __name__ == '__main__':
    unittest.main()
