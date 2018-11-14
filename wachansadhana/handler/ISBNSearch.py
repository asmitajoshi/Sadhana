import http.client
import requests

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

  def open_connection(self):
    self.conn = http.client.HTTPSConnection(self.uri)

  def search(self, isbn):
    if self.data: return self.data# don't repeat requests
    self.open_connection()
    try:
      if not isbn: isbn = self.default_test_isbn
      #https://isbndb.com/search/books/9781501183669
      self.conn.request('GET', self.path + isbn)
      response = self.conn.getresponse()
      print(response.status, response.reason)
      self.data = response.read()
      print('response closed ' + str(response.closed))
      #while not response.closed:
        #self.data.append(response.read(200))
    except requests.ConnectionError:
      print('Failed to connect')
      print(response.status, response.reason)
    finally:
      self.conn.close()
    return self.data
