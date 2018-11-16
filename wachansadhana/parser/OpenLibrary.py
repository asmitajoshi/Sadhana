import requests
import lxml.html
from lxml.html import fromstring, tostring

class OpenLibrary:
  def __init__(self):
    pass

  def get_info_url(self, data):
    pass

  def http_get_info_url(self, info_url):
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
    print('json ', data)
    info_url = self.get_info_url(data)
    return self.http_get_info_url(info_url)


