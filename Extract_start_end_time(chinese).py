# -*- coding: utf-8 -*-
import csv
import collections



a = collections.defaultdict(list)
code = collections.defaultdict(str)

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
        code[row["公司"]] = row["代码"]
# print(a["盛运环保"])
for name in a.keys():
    a[name] = dict(collections.Counter(a[name]))
print(a["盛运环保"])
with open("ChineseCompany_2.csv",'w',encoding='utf-8') as out:
    f = ['code','company','start','end','count of date points']
    out.write("{},{},{},{},{}\n".format(f[0],f[1],f[2],f[3],f[4]))
    for name in a.keys():
        temp = []
        for k,v in a[name].items():
            if v > 1:
            #the threshold is now 2, which means news count large than or equal to 2 will be counted as a date point
                temp.append(tuple([k,v]))
        sorted(temp,key=lambda x: x[0])
        if temp:
            if len(temp) >= 2:
                out.write("{},{},{},{},{}\n".format(code[name],name,temp[0][0],temp[-1][0],len(temp)))
