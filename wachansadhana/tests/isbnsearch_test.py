import unittest
from wachansadhana.handler import ISBNSearch

class TestISBNSearch(unittest.TestCase):
  def test_get_valid(self):
    uri = 'en.wikipedia.org'
    path = '/wiki/Special:BookSources?isbn=9781501183669'
    isbnsearch = ISBNSearch.ISBNSearch(uri, path)    
    self.assertEqual( isbnsearch.search(None), 'skdj' )

  def test_openlib(self):
    #https://openlibrary.org/api/books?bibkeys=ISBN:0451526538
    uri = 'openlibrary.org'
    path = '/api/books?bibkeys=ISBN:'
    isbnsearch = ISBNSearch.ISBNSearch(uri, path)    
    self.assertEqual( isbnsearch.search('9781501183669'), 'skdj' )

  def test_find_parser(self):
    isbnsearch = ISBNSearch.ISBNSearch(None, None)
    self.assertEqual( isbnsearch.find_parser('isbndb'), 'parseISBNDB' )
    isbnsearch._setUri('openlibrary.org')
    self.assertEqual( isbnsearch.find_parser('openlibrary'), 'parseOpenLibrary' )
    isbnsearch._setUri('en.wikipedia.org')
    self.assertEqual( isbnsearch.find_parser('owieur'), None )
if __name__ == '__main__':
  unittest.main()
