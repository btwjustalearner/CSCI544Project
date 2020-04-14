import json
import os
import time
from pathlib import Path
import csv
path = Path.cwd() / "us-financial-news-articles"
data = {"google":{},"amazon":{},"apple":{},"microsoft":{},"facebook":{},"tesla":{},"intel":{}}
for_write = []
start = time.time()
for root, dirs, files in os.walk(path):
    print(root)
    print(len(files))
    for name in  files:
        if name.endswith("json"):
            # print(name)
            with open(os.path.join(root, name), 'r', encoding='utf-8') as f:
                news_data = json.load(f)
                for company in data.keys():
                    if company in news_data['title'].lower():
                        date = news_data['published'][:10]
                        if date in data[company]:
                            data[company][date].append(news_data['text'])
                        else:
                            data[company][date] = [news_data['text']]
                        s = [company ,date ,news_data['title'].replace("\n"," ") ,news_data['text'].replace("\n"," ")]
                        for_write.append(s)
    print('end\n')
end = time.time()
print("total:{}".format(end - start))

print("-------- start stat -------\n")
temp = []
t = 0
for company in data.keys():
    total = 0
    for date in data[company]:
        # print("{}, count_of_news:{}\n".format(date, len(data[company][date])))
        temp.append(tuple([date, len(data[company][date])]))
    temp = sorted(temp, key=lambda x:x[0])
    with open(company+".cvs","w") as o:
        o.write("date, count\n")
        for item in temp:
            o.write("{},{}\n".format(item[0], item[1]))
            total += item[1]
    print("Company: {}, {}".format(company, total))
    temp = []
    t += total
print(t)
print("---------start writing------\n")
with open("news.json",'w') as t:
    json.dump(data, t)
with open("news(en).csv",'w', encoding="utf-8") as f:
    f.write("company, date, title, text\n")
    for line in for_write:
        f.write("{},{},{},{}\n".format(line[0],line[1],line[2],line[3]))


