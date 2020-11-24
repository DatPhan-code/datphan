print ("=============Bai 11============")
str = input("nhap vao 1 chuoi: ").split(",")
for x in str:
    str.sort()
print (",".join(str))

print ("=============Bai 12============")

s = input("Nhap chuoi cua ban: ")
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))

print ("=============Bai 13============")
"""
values =[]
items = input("moi nhap chuoi nhi phan".split(","))
for x in items:
    items.append(x)
    for p in items:
        intp = int(p,2)
        if not intp%5:
            values.append(p)
print(",".join(values))  
"""
"""
value =[]
items =[x for x in print ("Moi nhap chuoi nhi phan: ").split(',')] 
for p in items :
    intp = int(p,2)
    if not intp%5:
        value.append(p)       
print (','.join(value))
"""
"""
values =[]
for i in range(1000,3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
"""

s = input("Nhap cau cua ban: ")
d ={"digit":0 , "letter":0}
for c in s:
    if c.isdigit():
        d["digit"] +=1
    elif c.isalpha():
        d["letter"]+=1
    else:
        pass
print ("So chu cai: ",d["letter"])
print("so chu so: ",d["digit"])

print ("=============Bai 14============")

s =input("Enter your sention: ")
d = {"upper":0 , "lower":0}
for c in s:
    if c.isupper():
        d["upper"]+=1
    elif c.islower():
        d["lower"]+=1
    else:
        pass
print ("chu hoa: ",d["upper"])
print ("chu thuong: ",d["lower"])

print ("=============Bai 15============")

a = input ("moi nhap a :")
n1 = int("%s" %a)
n2 = int("%s%s" %(a,a))
print ("Thong la: ",n1+n2)

print ("=============Bai 16============")
#cách 1 
values = input("nhap day so cua ban: ")
numbers = [x for x in values.split(",") if int(x)%2 !=0 ]
print(",".join(numbers))

#cách 2
values = input("nhap day so cua ban: ")
number =[]
for x in values.split(","):
    if int(x)%2!=0:
        number.append(x)

print(",".join(number))


print ("=============Bai 17============")

import sys
netmount = 0
while True:
    s = input("moi nhap giao dich: ")
    if not s :
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation =="D":
        netmount+=amount
    elif operation == "W" : 
        netmount-=amount
    else:
        pass
print(netmount)
    



