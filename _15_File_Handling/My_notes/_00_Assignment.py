'''
write a program and fetch data using http get and point out number of holidays
in england and wales then group them based on year.

http://www.gov.uk//bank-holidays.json
'''
import json
from urllib.request import urlopen

url = "http://www.gov.uk/bank-holidays.json"
data = urlopen(url)
url1_dict = json.loads(data.read())
print(url1_dict)

print(url1_dict['england-and-wales']['events'])
list1 = []
list2 = []
year = '2016'
for i in url1_dict['england-and-wales']['events']:
    list1.append(i['title'])
    list2.append(i['date'])
print(list1)

count = 0
for i in list1:
    if i != 0:
        count += 1
print("Total Holidays are:", count)


print(list2)
list3 = [str[:4] for str in list2]
list3 =set(list3)
list4 = list(list3)
list4 = list4.sort()
print(list4)
print("list3 is",list3)
string1 = str(list2)
print(string1, type(string1))
for year in list3:
   print(f'Holiday in {year, type(year)} is {string1.count(year)}')

