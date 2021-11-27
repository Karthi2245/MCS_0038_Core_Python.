# Json to Csv
import json
import csv
from urllib.request import urlopen

url = "http://www.gov.uk/bank-holidays.json"
data = urlopen(url)
url1_dict = json.loads(data.read())
f = open("dict_data.txt", 'w')
f.write(str(url1_dict))
print(url1_dict)
list1 = []
list2 = []
list3 = []

for i in url1_dict['england-and-wales']['events']:
    list1.append(i['title'])
    list1.append(i['date'])

print('list 1', list1)
for j in url1_dict['scotland']['events']:
    list2.append(j['title'])
    list2.append(j['date'])
print('list2', list2)
for z in url1_dict['northern-ireland']['events']:
    list3.append(z['title'])
    list3.append(z['date'])
print('list3', list3)

list1.extend(list2)
list1.extend(list3)
print('list1', list1)


list5 = [list1]
print('list 5', list5)

f = open("mydata.csv", 'w')
write = csv.writer(f)
write.writerows(list5)
