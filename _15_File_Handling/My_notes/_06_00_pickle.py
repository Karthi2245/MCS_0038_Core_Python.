from _15_File_Handling._06_pickle import *
import pickle
e = Employee("Karthi", "MCS-0038", 9786910190, "Bangalore")
f = ''
pickle.dump(e , f)


f = open("E:\\MCS-Core Python\\_15_File_Handling\\_06_pickle.py", 'rb')
print("Employee details: ")
while True:
    obj = pickle.load(f)





