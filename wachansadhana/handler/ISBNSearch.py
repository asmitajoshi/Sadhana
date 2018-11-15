import http.client
import requests
import re
from wachansadhana.parser.OpenLibrary import OpenLibrary
from wachansadhana.parser.ISBNDB import ISBNDB

class ISBNSearch:

  def __init__(self, isbn_search_uri, path):
    self.default_uri = 'www.isbndb.com'
    self.default_path = '/search/books/'
    self.default_test_isbn = '9781501183669'
    if not isbn_search_uri: self.uri = self.default_uri
    else: self.uri = isbn_search_uri
    if not path: self.path = self.default_path
    else: self.path = path
    self.data = []
    self.conn = None
    self.parser = None
    self.parser = self.find_parser_from_uri()
    print('parser ' + type(self.parser).__name__)
  # set uri for testing
  def _setUri(self, uri):
    self.uri = uri

  def find_parser_from_uri(self):
    if not self.parser: self.parser = None
    self.all_parsers = {'openlibrary': OpenLibrary(), 'isbndb': ISBNDB()}
    for k, v in self.all_parsers.items():
      p = re.compile('.*\.?' + k + '\..+')
      m = p.match(self.uri)
      if (m): self.parser = self.all_parsers[k]
    return self.parser

  def find_parser(self, key):
    p = re.compile('.*\.?' + key + '\..+')
    m = p.match(self.uri)
    return self.all_parsers[key] if m else None

  def open_connection(self):
    self.conn = http.client.HTTPSConnection(self.uri)

  def search(self, isbn):
    if self.data: return self.data# don't repeat requests
    try:
      if not isbn: isbn = self.default_test_isbn
      response = requests.get('https://' + self.uri + self.path + isbn)
      print(response.text)
      self.data = response.text
      print(self.data)
    except requests.ConnectionError:
      print('Failed to connect')
      print(response.status, response.reason)
    return self.data

  def parse(self, data):
    print('parser ' + str(self.parser))
    return self.parser.parse(self.data)
