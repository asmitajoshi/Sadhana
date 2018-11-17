from wachansadhana.store.GoogSheets import GoogSheets

class CreateBookRecord:

  def __init__(self, store):
    self.supported_storage = {'goog_sheets': GoogSheets()}
    if not store: self.store = 'goog_sheets'
    self.storage = self.supported_storage.get(self.store)

  def create(self, record):
    self.storage.create(record)
