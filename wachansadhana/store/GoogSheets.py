from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogSheets():
  def __init__(self):
    # If modifying these scopes, delete the file token.json.
    self.scopes = 'https://www.googleapis.com/auth/spreadsheets'
    self.sheet_id = '1XXqGbGSnda5qxAqhlUJ7RIN50MS17yJQiutZBHwQEEM'
    self.range_name = 'A1:D5'

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', self.scopes)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()

  def create(self, record):
    myvalues = [
        ["Item", "Cost", "Stocked", "Ship Date"],
        ["Wheel", "$20.50", "4", "3/1/2016"],
        ["Door", "$15", "2", "3/15/2016"],
        ["Engine", "$100", "1", "30/20/2016"],
        ["Totals", "=SUM(B2:B4)", "=SUM(C2:C4)", "=MAX(D2:D4)"]
    ]
    mbody = {
      'values' : myvalues
    }
    value_input_option = 'RAW'
    result = sheet.values().update(spreadsheetId=self.sheet_id,
              range=self.range_name, valueInputOption=value_input_option, body=mbody).execute()

    print('{0} cells updated.'.format(result.get('updatedCells')));
    return result.get('updatedCells')
