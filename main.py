import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1pwfgHY06x8BYCrbZ79RNWxGFMl4mBFL_Yqr4ezZ1cRs/edit?usp=sharing")

worksheet = wks.get_worksheet(0)

values_list = worksheet.col_values(2)

print values_list

