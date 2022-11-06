import csv
import numpy as np
from datetime import *

month = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}#2
hotel = { "Resort Hotel" : [1,0] , "City Hotel" : [0,1]}#0
meal = { "Undefined" : [1,0,0,0,0,0] , "SC" : [0,1,0,0,0,0], "FB" : [0,0,1,0,0,0],"BB":[0,0,0,1,0,0] , "HB":[0,0,0,0,1,0] , "Undefined" : [0,0,0,0,0,1]}#9
market_segment = {"Groups":[1,0,0,0,0,0,0,0],"Direct" : [0,1,0,0,0,0,0,0] , "Offline TA/TO" : [0,0,1,0,0,0,0,0] , "Online TA":[0,0,0,1,0,0,0,0] , "Corporate" : [0,0,0,0,1,0,0,0], "Complementary" : [0,0,0,0,0,1,0,0] , "Undefined" : [0,0,0,0,0,0,1,0] , "Aviation" : [0,0,0,0,0,0,0,1]}#10
distribution_channal = {"Direct" : [1,0,0,0,0] , "TA/TO" : [0,1,0,0,0] , "Corporate" : [0,0,1,0,0] , "Undefined" : [0,0,0,1,0] , "GDS" : [0,0,0,0,1]}#11
assigned_room_type = {"A": [1,0,0,0,0,0,0,0,0,0,0] , "B" : [0,1,0,0,0,0,0,0,0,0,0] , "C" : [0,0,1,0,0,0,0,0,0,0,0] , "D" : [0,0,0,1,0,0,0,0,0,0,0] , "E" : [0,0,0,0,1,0,0,0,0,0,0] , "F" : [0,0,0,0,0,1,0,0,0,0,0] , "G" : [0,0,0,0,0,0,1,0,0,0,0] , "H" : [0,0,0,0,0,0,0,1,0,0,0], 'I':[0,0,0,0,0,0,0,0,1,0,0] , 'P' : [0,0,0,0,0,0,0,0,0,1,0] , "K" : [0,0,0,0,0,0,0,0,0,0,1]}#12
customer_type = {"Contract" : [1,0,0,0] , "Group" : [0,1,0,0] , "Transient" : [0,0,1,0] , "Transient-Party" : [0,0,0,1]}#13


def handle_data(data):
    data = np.delete(data,0,0)
    data = np.delete(data, [0,3,6,14,17,18,19,20,22,23,24,25,26,31,32] ,1)
    data = [ x for x in data if x[1] == '0']
    data = np.delete(data,1,1)
    dealed_data = []
    ans_days = []
    ans = []
    for i in data:
        day = [int(i[1]) , int(month[i[2]]) , int(i[3]) , int(i[4]) + int(i[5])]
        ans_days.append(day)
        temp = hotel[i[0]] + [i[4] , i[5]] + [i[6] , i[7] , i[8]] + meal[i[9]] + market_segment[i[10]] + distribution_channal[i[11]] + assigned_room_type[i[12]] + customer_type[i[13]] +[i[15] , i[16]]
        a = [float(x) for x in temp]
        dealed_data.append(a)
        ans.append(float(i[14]))
    
    return dealed_data,ans,ans_days

def handle_test_data(data):
    data = np.delete(data,0,0)
    data = np.delete(data, [0,2,5,13,16,17,18,19,21,22,23,24,25] ,1)
    print(data[0])
    dealed_data = []
    ans_days = []
    for i in data:
        day = [int(i[1]) , int(month[i[2]]) , int(i[3]) , int(i[4]) + int(i[5])]
        ans_days.append(day)
        temp = hotel[i[0]] + [i[4] , i[5]] + [i[6] , i[7] , i[8]] + meal[i[9]] + market_segment[i[10]] + distribution_channal[i[11]] + assigned_room_type[i[12]] + customer_type[i[13]] +[i[14] , i[15]]
        a = [float(x) for x in temp]
        dealed_data.append(a)
    return dealed_data,ans_days


with open('train.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

with open('train_label.csv', newline='') as f:
    reader = csv.reader(f)
    data_label = list(reader)

with open("test.csv", newline='') as f:
    reader = csv.reader(f)
    test_data = list(reader)

data,ans,ans_days = handle_data(data)


