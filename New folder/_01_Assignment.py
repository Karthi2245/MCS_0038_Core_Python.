'''tamil = int(input("Enter a Marks"))
english = int(input("Enter a marks"))
maths = int(input("enter a marks"))
science = int(input("Enter a marks"))
social = int(input("Enter a marks"))


list1 = [tamil, english, maths, science, social]
sum1 = 0
for i in range(len(list1)):
    sum1 += list1[i]
    avg = sum1 / 5
print(avg)

for i in list1:
    if i >= 95:
        count = count+1
    elif i >=90:
        count2 += 1
    elif i>=75:
        count3 += 1
    else:
        count4 += 4
count = 0
if avg >= 95:

    for i in list1:

        if i >= 95:
            count = count + 1
            if count >= 3:
                print("Gold Medal")
                break
elif avg >= 90:
    print('Distinction')
elif avg > 75:
    print('Average')
elif avg < 75:
    print('Fail')
else:
    print('Ultra Fail')'''


# Cards:
s = h = c = d = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

a = s[4::8]+ h[1::5] + s[0::3] + c[-8::-3] + d[4::8]+h[6::10]+d[10::13]+c[0:6] \
    + c[4:8]
b = s[0::3]+ h[1::5] + s[4::8] + c[-9::-5] + d[1::7]+h[3::8]+d[-10::-3]+c[5:10] \
    + c[0:4]

sum_a = 0
for i in range(len(a)):
        sum_a += a[i]
# print(sum_a)
sum_b = 0
for i in range(len(b)):
        sum_b += b[i]
# print(sum_b)


if sum_a > sum_b:
    print(f'{sum_a} A is a winner')
else:
    print(f'{sum_b} B is a Winner')
# print(b)
# print(len(a))
# print(b)
# print(len(b))

'''from  random import  shuffle

a = [1, 2, 3 , 4, 5, 6]
shuffle(a)
print(a)'''
import time
s=c=d=h=[1,2,3,4,5,6,7,8,9,10,11,12,13]

def ran_val(y):
    a = time.time()**2
    a //= y
    a %= y
    return a
print(ran_val(14))

























































