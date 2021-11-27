'''import csv
f = open("E:\MCS-Core Python\\New folder\\mydata.csv")
read = csv.reader(f)
list1 = []
for i in read:
    list1.extend(i)
print(list1)
count = 0
for i in range(len(list1)):
    if i % 2 == 1:
        print(list1[i] ,':', list1[i-1])
        count += 1
print("The Holidays of three countries", count)'''


dave = 180
laura = dave/3
amr = 150
vicky = dave/3 + amr/2 + laura+120
owen = dave/3 + amr/2
amr = 0 + laura+120
dave = 0 + owen -85
print('dave', dave)
print('amr', amr)
print('laura', laura)
print('owen', owen)
print('vicky', vicky)


# # dict1 = {'dave':180, 'owen':50, 'amr': 150, 'laura' : 360 , 'vicky' : 0 }
# dave = 0
# amr = 0
# laura = 0
# vicky = 0
# owen = 0
# d = 180
# a = 150
# l = 360
# o = 50
# v = 0
# if dave == 0:
