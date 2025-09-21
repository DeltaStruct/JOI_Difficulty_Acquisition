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
f = json.load(open("main.json","wr"))
for i in range(ws.row_count):
  task = ws.cell(i+1,4).value
  if task==None:
    time.sleep(1)
    continue
  vote = ws.cell(i+1,6).value
  if "春合宿" not in task:
    task = task.replace("春","春合宿")
  if "春合宿" not in task:
    task = task.replace("合宿","春合宿")

  task = task.replace("JOIG-","JOIG")

  task = task.replace('１','1');
  task = task.replace('２','2');
  task = task.replace('３','3');
  task = task.replace('４','4');
  task = task.replace('５','5');
  task = task.replace('６','6');
  task = task.replace('７','7');
  task = task.replace('８','8');
  task = task.replace('９','9');
  task = task.replace('０','0');
  task = task.replace(' ','');
  
  print("fetch: " + task)
  print(vote)
  if vote == None:
    vote = ""
  f[task] = vote
  time.sleep(2)

ws = connect_gspread(jsonf,spread_sheet_key,"難易度表 New")

for i in range(ws.row_count):
  task = ws.cell(i+1,4).value
  if task==None:
    time.sleep(1)
    continue
  vote = ws.cell(i+1,6).value
  if "春合宿" not in task:
    task = task.replace("春","春合宿")
  if "春合宿" not in task:
    task = task.replace("合宿","春合宿")

  task = task.replace("JOIG-","JOIG")
  task = task.replace("本選-","本選")
  task = task.replace("予選-","予選")

  task = task.replace('１','1');
  task = task.replace('２','2');
  task = task.replace('３','3');
  task = task.replace('４','4');
  task = task.replace('５','5');
  task = task.replace('６','6');
  task = task.replace('７','7');
  task = task.replace('８','8');
  task = task.replace('９','9');
  task = task.replace('０','0');
  task = task.replace(' ','');
  print("fetch: " + task)
  print(vote)
  if vote == None:
    vote = ""
  f[task] = vote
  time.sleep(2)
json.dump(f,open("main.json",'w'))
