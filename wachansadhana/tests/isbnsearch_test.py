import unittest
from wachansadhana.handler import ISBNSearch

class TestISBNSearch(unittest.TestCase):
  def test_get_valid(self):
    uri = 'en.wikipedia.org'
    path = '/wiki/Special:BookSources?isbn=9781501183669'
    isbnsearch = ISBNSearch.ISBNSearch(uri, path)    
    self.assertIsNotNone( isbnsearch.search(None) )

  def test_openlib(self):
    #https://openlibrary.org/api/books?bibkeys=ISBN:0451526538
    uri = 'openlibrary.org'
    path = '/api/books?bibkeys=ISBN:'
    isbnsearch = ISBNSearch.ISBNSearch(uri, path)
    found = isbnsearch.search('9781501183669')
    #self.assertEqual( found, 'skdj' )
    print(found)
    parsed = isbnsearch.parse(found)
    print(parsed)
    self.assertEqual( parsed.get('title'), 'Ship of Fools' )

  def test_find_parser(self):
    isbnsearch = ISBNSearch.ISBNSearch(None, None)
    self.assertEqual( type(isbnsearch.find_parser('isbndb')).__name__, 'ISBNDB' )
    isbnsearch._setUri('openlibrary.org')
    self.assertEqual( type(isbnsearch.find_parser('openlibrary')).__name__, 'OpenLibrary' )
    isbnsearch._setUri('en.wikipedia.org')
    self.assertEqual( type(isbnsearch.find_parser('owieur')).__name__, 'NoneType' )

    isbnsearch = ISBNSearch.ISBNSearch(None, None)
    self.assertEqual( type(isbnsearch.find_parser_from_uri()).__name__, 'ISBNDB' )
    isbnsearch._setUri('openlibrary.org')
    self.assertEqual( type(isbnsearch.find_parser()).__name__, 'OpenLibrary' )
    isbnsearch._setUri('en.wikipedia.org')
    self.assertEqual( type(isbnsearch.find_parser()).__name__, 'NoneType' )
if __name__ == '__main__':
  unittest.main()
