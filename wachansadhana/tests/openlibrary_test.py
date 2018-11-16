import unittest
from wachansadhana.parser.OpenLibrary import OpenLibrary

class TestOpenLibraryParser(unittest.TestCase):
  def test_get_valid(self):
    long_string = [b'var _OLBookInfo = {"ISBN:9781501183669": {"bib_key": "ISBN:9781501183669", "preview": "noview", "thumbnail_url": "https://covers.openlibrary.org/b/id/8269183-S.jpg", "preview_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools", "info_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools"}};'
b'var _OLBookInfo = {"ISBN:9781501183669": {"bib_key": "ISBN:9781501183669", "preview": "noview", "thumbnail_url": "https://covers.openlibrary.org/b/id/8269183-S.jpg", "preview_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools", "info_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools"}};']
    info_url = 'https://openlibrary.org/books/OL26529008M/Ship_of_Fools'
    parsed = OpenLibrary().http_get_info_url(info_url)
    self.assertEqual( parsed.get('publisher'), 'Free Press' )

  def test_get_info_url(self):
    long_str = 'var _OLBookInfo = {"ISBN:9781501183669": {"bib_key": "ISBN:9781501183669", "preview": "noview", "thumbnail_url": "https://covers.openlibrary.org/b/id/8269183-S.jpg", "preview_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools", "info_url": "https://openlibrary.org/books/OL26529008M/Ship_of_Fools"}};'
    info_url = OpenLibrary().get_info_url(long_str)
    expected_info_url = 'https://openlibrary.org/books/OL26529008M/Ship_of_Fools'
    self.assertEqual( info_url, expected_info_url )

if __name__ == '__main__':
  unittest.main()



#https://openlibrary.org/books/OL26529008M/Ship_of_Fools"
