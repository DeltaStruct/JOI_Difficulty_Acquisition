import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import time

def connect_gspread(jsonf,key,name):
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
  gc = gspread.authorize(credentials)
  SPREADSHEET_KEY = key
  worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet(name)
  return worksheet

jsonf = "g.json"
spread_sheet_key = "1zXDtkFmskO5NSxkqck8uDbcJtAhTVZtzPh2hLw64Sw4"
ws = connect_gspread(jsonf,spread_sheet_key,"難易度表")
for i in range(ws.row_count):
  print(ws.cell(i+1,4).value)
  time.sleep(0.2)
