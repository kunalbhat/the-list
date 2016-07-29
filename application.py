import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template

app = Flask(__name__)

# Load credentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

sheet_key = "1pwfgHY06x8BYCrbZ79RNWxGFMl4mBFL_Yqr4ezZ1cRs"

def openSheet():
    worksheet = gc.open_by_key(sheet_key)

    return worksheet

def getList():
    wks = openSheet()
    worksheet = wks.get_worksheet(0)
    list_of_lists = worksheet.get_all_values()

    return list_of_lists

@app.route("/")

def index():
    the_list = getList()

    return render_template('index.html', films=the_list)

if __name__ == "__main__":
    app.run(debug=True)

