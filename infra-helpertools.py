import json
import re
import time
import sys
from slacker import Slacker
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('helpertools-5eaa9290c475.json', scope)
client = gspread.authorize(creds)


api_token = "xoxp-12637824912-680903713712-720519570615-b5f3d5937482d96beebdc9a1621b839c"

slack = Slacker(api_token)
sheet = client.open("Lunch-Status").sheet1

wr= sheet.acell('B19').value
wor= sheet.acell('C19').value
slack.chat.post_message('#test-jags', "Total count\n With rice = "+ wr + "\nWithout rice = " + wor ,username='lunch status')

#sheet = client.open("Lunch-Status").sheet1
all_cells = sheet.range('A1:C9')
#print all_cells

