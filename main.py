import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# (1) Google Spread Sheetsにアクセス
def connect_gspread(jsonf,key,name):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet(name)
    return worksheet

# ここでjsonfile名と2-2で用意したkeyを入力
jsonf = "g.json"
spread_sheet_key = "1zXDtkFmskO5NSxkqck8uDbcJtAhTVZtzPh2hLw64Sw4"
ws = connect_gspread(jsonf,spread_sheet_key,"難易度表")
print(ws.cell(1,4).value)
