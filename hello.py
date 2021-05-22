import openpyxl
from openpyxl.styles import Font, Alignment

#Make adjustment to summary sheet and move that to start
book = openpyxl.load_workbook("URLForMonitors.xlsx")
#book.active = book.sheetnames.index('Summary')
sheet = book.active

import datetime
today = datetime.datetime.now()
print("Monitor Python file")
print(today.strftime("%d-%b %H Hr"))
book.save("URLForMonitors.xlsx")  
