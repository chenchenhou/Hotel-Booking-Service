import csv
import numpy as np
import pandas as pd
from datetime import datetime

with open("train.csv", newline = '') as csvfile:
    datas = list(csv.reader(csvfile))

with open("train_label.csv", newline = '') as csvfile_2:
    labels = list(csv.reader(csvfile_2))

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


title = datas[0]
    
examples = []
process_data = []

for data in datas[1:]:
    if data[2] == '0':
        values = [data[4], data[5], data[6], data[7], data[8], data[9], data[28]]
        examples.append(values)
        revenue = float(int(data[8]) + int(data[9]) + 1) *  float(data[28])
        process = [convertDate(data[4], data[5], data[7]), revenue]
        process_data.append(process)

dates = []
for data in process_data:
    if [data[0], 0] not in dates:
        dates.append([data[0], 0])

for data in process_data:
    for date in dates:
        if data[0] == date[0]:
            date[1] += data[1]

revenue_labels = [[], [], [], [], [], [], [], [], [], []]

for label in labels[1:]:
    for date in dates:
        if convertDate_2(label[0]) == date[0]:
            revenue_labels[int(label[1][:1])].append(date[1])


#print(f'{title[4]:^25}  {title[5]:^25}  {title[6]:^25}  {title[7]:^25}  {title[8]:^25}  {title[9]:^25}  {title[28]:^5}')
#print(f'{examples[0][0]:^25}  {examples[0][1]:^25}  {examples[0][2]:^25}  {examples[0][3]:^25}  {examples[0][4]:^25}  {examples[0][5]:^25}  {examples[0][6]:^5}')
#print(f'        date              revenue  ')
#for t in range(15):
#    print(f'{dates[t][0]:^20}{dates[t][1]:<20}')

for n in range(0, 10):
    print(f'Label {n}.0 equals to revenue in the range of {min(revenue_labels[n])}~{max(revenue_labels[n])}')
