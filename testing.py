import pandas as pd
from datetime import datetime
import csv

startdate = "07/10/2011"
enddate = pd.to_datetime(startdate) + pd.DateOffset(days=40)
date = enddate.strftime("%m/%d/%Y")
print(date)

def convertDate(year, month, day):
    month_ = 0
    day_ = 0
    months = [('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')]
    day_verify = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    days = [('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'), ('07', '7'), ('08', '8'), ('09', '9')]
    for i in months:
        if month == i[1]:
            month_ = i[0]
    if day in day_verify:
        for j in days:
            if day == j[1]:
                day_ = j[0]
    else:
        day_ = day

    return f'{month_}/{day_}/{year}'

def convertDate_2(date):
    return f'{date[5:7]}/{date[8:]}/{date[:4]}'

a = convertDate('2015','July','8')
b = convertDate_2('2015-07-08')
print(a)
print(b)

with open("train_label.csv", newline = '') as csvfile_2:
    labels = list(csv.reader(csvfile_2))

print(labels[:5])
    