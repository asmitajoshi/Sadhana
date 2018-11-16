import requests
import lxml.html
from lxml.html import fromstring, tostring
import re

class OpenLibrary:
  def __init__(self):
    pass

  def get_info_url(self, data):
    ola = data.split(' = {')[1].rstrip('}};').split(' {')[1]
    print(ola.split(', '))
    stripped_double_quotes_ola = re.sub('"', '', ola)
    book_record = dict(i.split(': ') for i in stripped_double_quotes_ola.split(', '))
    print(book_record.get('info_url'))
    return book_record.get('info_url')

  def http_get_info_url(self, info_url):
    if not info_url: return None
    response = requests.get(info_url)
    r = response.text
    page = lxml.html.fromstring(r)
    textarea = page.xpath('//textarea[@id="wikiselect"]')[0]
    print(textarea.value)
    print(textarea.name)
    tv = textarea.value
    citation = tv[tv.find("{{") + 1 : tv.find("}}")]
    print(citation)
    isbnfields = dict(i.split(' = ') for i in map(lambda x: x.rstrip(), citation.split('|')[1:]))
    print(isbnfields.values())
    return isbnfields

  def parse(self, data):
    print('lotsa text ', data)
    info_url = self.get_info_url(data)
    return self.http_get_info_url(info_url)


