import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds=ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)

client=gspread.authorize(creds)

sheet=client.open('flask').sheet1

#printing full data inside our table
data=sheet.get_all_records()
pprint(data)

#printing a row
row=sheet.row_values(2)
print(row)

#printing a cell
cell=sheet.cell(1,2).value
print(cell)

#inserting into a row
insertrow=['s',6]
sheet.insert_row(insertrow,7)

#deleting a row
sheet.delete_row(5)

#updating a value
sheet.update_cell(2,2,"qharsh")