import unittest
import requests
import bs4


class TestMain(unittest.TestCase):

    def setUp(self):  #
        url = 'http://127.0.0.1:8000/'
        r = requests.get(url)
        self.html = bs4.BeautifulSoup(r.text)


    def test_can_open_homepage(self):
        # Nick has heard about a cool new online to-do app.
        # He goes to check out its homepage
        # He notices the page title and header mention Aquba
        self.assertEqual("Aquba", self.html.title.text)
        self.fail('Finish the test!') #
        # She is invited to enter a to-do item straight away



if __name__ == "__main__":
    unittest.main()