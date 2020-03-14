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
    a[name].reverse()
print(a["盛运环保"])
with open("result.csv",'w',encoding='utf-8') as out:
    f = ['公司','开始','结束']
    out.write("{},{},{}\n".format(f[0],f[1],f[2]))
    for name in a.keys():
        out.write("{},{},{}\n".format(name, a[name][0], a[name][-1]))
