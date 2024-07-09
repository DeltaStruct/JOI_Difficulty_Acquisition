import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import time

def connect_gspread(jsonf,key,name):
  scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
  credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
  gc = gspread.authorize(credentials)
  SPREADSHEET_KEY = key
  worksheet = gc.open_by_key(SPREADSHEET_KEY).worksheet(name)
  return worksheet

jsonf = "g.json"
spread_sheet_key = "1zXDtkFmskO5NSxkqck8uDbcJtAhTVZtzPh2hLw64Sw4"
ws = connect_gspread(jsonf,spread_sheet_key,"難易度表")
for i in range(ws.row_count):
  task = ws.cell(i+1,4).value
  if task==None:
    time.sleep(1)
    continue
  vote = ws.cell(i+1,6).value
  if "春合宿" not in task:
    if "春" in task:
      task = task.replace("春","春合宿")
    elif "合宿" in task:
      task = task.replace("合宿","春合宿")
  if "JOIG-" in task:
    task = task.replace("JOIG-","JOIG")
  print("fetch: " + task)
  print(vote)
  f = open(task,'w')
  f.write(vote)
  f.close()
  time.sleep(2)

ws = connect_gspread(jsonf,spread_sheet_key,"難易度表 New")
for i in range(ws.row_count):
  task = ws.cell(i+1,4).value
  if task==None:
    time.sleep(1)
    continue
  vote = ws.cell(i+1,6).value
  if "春合宿" not in task:
    if "春" in task:
      task = task.replace("春","春合宿")
    elif "合宿" in task:
      task = task.replace("合宿","春合宿")
  if "JOIG-" in task:
    task = task.replace("JOIG-","JOIG")
  print("fetch: " + task)
  print(vote)
  if vote == None:
    vote = ""
  f = open(task,'w')
  f.write(vote)
  f.close()
  time.sleep(2)
