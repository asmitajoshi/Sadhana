import unittest
from wachansadhana.handler import ISBNSearch

class TestISBNSearch(unittest.TestCase):
  def test_get_valid(self):
    uri = 'en.wikipedia.org'
    path = '/wiki/Special:BookSources?isbn=9781501183669'
    isbnsearch = ISBNSearch.ISBNSearch(uri, path)    
    self.assertEqual( isbnsearch.search(None), 'skdj' )

if __name__ == '__main__':
  unittest.main()
