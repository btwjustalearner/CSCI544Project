# -*- coding: utf-8 -*-
import csv
import collections



a = collections.defaultdict(list)
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
                temp = ''
            elif char == '日':
                d = temp
                temp = ''
            else:
                temp += char
        a[row["公司"]].append(y+'-'+m+'-'+d)
print(a["盛运环保"])
for name in a.keys():
    a[name] = dict(collections.Counter(a[name]))
print(a["盛运环保"])
with open("ChineseCompany_1.csv",'w',encoding='utf-8') as out:
    f = ['company','time and fequency']
    out.write("{},{}\n".format(f[0],f[1]))
    for name in a.keys():
        temp = []
        for k,v in a[name].items():
            if v >= 2:
                temp.append(tuple([k,v]))
        sorted(temp,key=lambda x: x[0])
        out.write("{},{}\n".format(name, temp))
