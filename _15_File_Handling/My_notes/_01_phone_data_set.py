'''
Steps to read a CSV file:
--> Import the csv library. import csv.
--> Open the CSV file. The . ...
--> Use the csv.reader object to read the CSV file.csvreader = csv.reader(file)
--> Extract the field names. Create an empty list called header. ...
--> Extract the rows/records. ...
--> Close the file
'''
import csv

'''f = open("E:\MCS-Core Python\phone_dataset.csv", 'r')
list_data = [[] for i in range(4)]
for i, j in zip(range(len(list_data)), f):
    list_data[i] = j
print(list_data)

q = open("E:\MCS-Core Python\query - Copy.txt")
for i in q:
    print(i)'''

f = open("E:\MCS-Core Python\_15_File_Handling\phone_dataset.csv")
read = csv.reader(f)
list1 = []
for i in read:
    list1.extend(i)
print(list1)

f1 = open("E:\MCS-Core Python\_15_File_Handling\query - Copy.txt")
query_list = []
read1 = csv.reader(f1)
for j in read1:
    query_list.extend(j)
print(query_list)

for i in query_list:   # This is for comparing the list
    for j in range(len(list1)):
        if i in list1[j]:
            print("Matches for Given list", i, ':', list1[j])


input1 = eval(input("Enter The number"))

print(input1)

'''using while loop display m, n'''


'''
import csv

csv_data = []
with open('result.txt','w') as f:
    with open("phone_dataset.csv", 'r') as phone_data:
        my_csv = csv.reader(phone_data,delimiter =',')
        for i in my_csv:
            csv_data.append(i)

    with open("query - Copy.txt", "r") as query_data:
        input_data = query_data.read()
        input_data = input_data.splitlines()

        for inpt in input_data:
            count = 1
            matches = False
            f.write(f"matches for {inpt}\n")
            for csv_d in csv_data:
                temp_csv = csv_d
                csv_d = csv_d[0].split(',')
                if csv_d[0].strip().lower() == inpt.lower() or csv_d[1].strip().lower() == inpt.lower():
                    f.write(f"Result {count} : {temp_csv}\n")
                    count = count + 1
                    matches = True
            if matches == False:
                 f.write("No Result Found \n")
    f.close()'''
