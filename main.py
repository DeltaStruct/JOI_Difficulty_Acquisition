import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# (1) Google Spread Sheetsにアクセス
def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet("難易度表")
    return worksheet

# ここでjsonfile名と2-2で用意したkeyを入力
jsonf = "../g.json"
spread_sheet_key = "1zXDtkFmskO5NSxkqck8uDbcJtAhTVZtzPh2hLw64Sw4"
ws = connect_gspread(jsonf,spread_sheet_key)
