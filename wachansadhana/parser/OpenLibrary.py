import requests

class OpenLibrary:
  def __init__(self):
    pass

  def get_info_url(self, data):
    pass

  def http_get_info_url(self, info_url):
    response = requests.get(info_url)
    dict = response.json()
    print(dict)

  def parse(self, data):
    print('json ', data)
    info_url = self.get_info_url(data)
    return self.http_get_info_url(info_url)


