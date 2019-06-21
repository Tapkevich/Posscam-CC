import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from googleapiclient import discovery
import json

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


spreadsheet_id = "1yH3KgAqfeR0ANbXYT4D2yOIPC-XKlNzOswyChqdViwY"

service = discovery.build('sheets', 'v4', credentials=creds)

ranges = 'MonsterBaseParam!A:C'

request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range = ranges, valueRenderOption = 'FORMATTED_VALUE')
result = request.execute()

new_json = json.dumps(result)


pprint(new_json)