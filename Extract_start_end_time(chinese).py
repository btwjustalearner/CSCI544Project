# -*- coding: utf-8 -*-
import csv
import collections
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


a = collections.defaultdict(list)
code = collections.defaultdict(str)
valid = collections.defaultdict(set)
for_count = []

def outlier():
    for_count = []
    with open("test_data.csv",'r', encoding="utf-8") as input:
        reader = csv.DictReader(input)
        for row in reader:
            raw_date = row["日期"]
            y, m, d = '','',''
            temp = ''
            for char in raw_date:
                if char == '年':
                    y = temp
                    temp = ''
                elif char == '月':
                    for k, ch in enumerate(temp):
                        if ch != '0':
                            break
                    m = temp[k:]
                    if len(m) == 1:
                        m = '0' + m
                    temp = ''
                elif char == '日':
                    d = temp
                    temp = ''
                else:
                    temp += char
            for_count.append(y+'-'+m)
    for_count = sorted(list(collections.Counter(for_count).items()), key=lambda x: x[0])
    print(for_count)
    x, y = zip(*for_count)
    plt.bar(x, y)
    plt.show()

def Extract_start_end():
    with open("test_data.csv",'r', encoding="utf-8") as input:
        reader = csv.DictReader(input)
        for row in reader:
            raw_date = row["日期"]
            y, m, d = '','',''
            temp = ''
            for char in raw_date:
                if char == '年':
                    y = temp
                    temp = ''
                elif char == '月':
                    for k, ch in enumerate(temp):
                        if ch != '0':
                            break
                    m = temp[k:]
                    if len(m) == 1:
                        m = '0' + m
                    temp = ''
                elif char == '日':
                    d = temp
                    temp = ''
                else:
                    temp += char
            for_count.append(y+'-'+m)
            a[row["公司"]].append(y+'-'+m+'-'+d)
            code[row["公司"]] = row["代码"]
    
    # print(a["盛运环保"])
    for name in a.keys():
        a[name] = dict(collections.Counter(a[name]))
    # print(a["盛运环保"])
    with open("ChineseCompany_3_test.csv",'w',encoding='utf-8') as out:
        f = ['code','company','start','end','count of date points']
        out.write("{},{},{},{},{}\n".format(f[0],f[1],f[2],f[3],f[4]))
        for name in a.keys():
            temp = []
            for k,v in a[name].items():
                if v > 0:
                #the threshold is now 2, which means news count large than or equal to 2 will be counted as a date point
                    temp.append(tuple([k,v]))
            sorted(temp,key=lambda x: x[0])
            if temp:
                out.write("{},{},{},{},{}\n".format(code[name],name,temp[0][0],temp[-1][0],len(temp)))
                valid[name] |= set([x[0] for x in temp])
    # print(valid)
    print("done with extracting start-end date info")



def Filter_traindata():
    traindata = []

    with open("train_data.csv",'r', encoding="utf-8") as input:
        reader = csv.DictReader(input)
        for row in reader:
            raw_date = row["日期"]
            y, m, d = '','',''
            temp = ''
            for char in raw_date:
                if char == '年':
                    y = temp
                    temp = ''
                elif char == '月':
                    for k, ch in enumerate(temp):
                        if ch != '0':
                            break
                    m = temp[k:]
                    if len(m) == 1:
                        m = '0' + m
                    temp = ''
                elif char == '日':
                    d = temp
                    temp = ''
                else:
                    temp += char
            date = y+'-'+m+'-'+d
            company = row["公司"]
            if company in valid:
                if date in valid[company]:
                    row = dict(row)
                    row["日期"] = date
                    traindata.append(row)
    # print(traindata[0])
    
    outputpath = Path.cwd() / "data" / "traindata(ch).csv"
    with open(outputpath,"w",encoding='utf-8',newline='') as train:
        title = ["","日期","公司","代码","正负面","标题","正文"]
        writer = csv.DictWriter(train, fieldnames=title)
        train.write("index,date,company,code,P/N,title,news\n")
        for row in traindata:
            writer.writerow(row)
    print("done with filtering train data")
    print("train data count: {}\nunique company count: {}".format(len(traindata), len(valid.keys())))

if __name__ == "__main__":
    Extract_start_end()
    # Filter_traindata()
    # outlier()