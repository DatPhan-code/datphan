import re
"""
values = []
Str = [x for x in input(" enter your pasword: ").split(',')]
for p in Str:
   # if len(p) < 6 and len(p) > 12:
    #    break
    #else : 

        if not re.search("[a-z]",p):
            continue

        
        elif not re.search("[0-9]",p):    
            continue
        else:
            pass
        values.append(p)
print ("My result: ",",".join(values))        

"""
values = []
Str = [x for x in input(" enter your pasword: ").split(',')]
for p in Str:
    if len(p) < 6 or len(p) > 12:
       continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    else:
        pass
    values.append(p)
print ("my result: ",",".join(values))

print ('Toi di hoc','toi di choi', sep='---')


student_list =['Long','Ho','Gau','Beo']
gen = enumerate(student_list)
print (list(gen))

list = [1,2,3]
for i in  list:
    i +=1
print (list)

list =[1,2,3]
for i in range(len(list)):
    list[i]+=1
print (list)

set_ = {3,4,5,6}
tong = 0
for value in set_:
    tong+=value
print (tong)


list = [[1,2,3],[4,5,6]]
for i in list:
    list[0] = None
print (list)

list = [1,2,3,4,'toi']
print (*list)

list = [*(x for x in range(7))]
print(list)

dic = {"Name": 'Datphan',"member": 90}
def dict(Name, member):
    print(Name)
    print(member)

dict(**dic)

"""
a = input("nhap so 1: ")
b = input("nhap so 2: ")
def tinhtong(a1,b2):
    tong = a1+b2
    return tong

sum = tinhtong(a,b)
print(sum)
"""

#yield 

def square(lst):
    for x in lst:
        yield x**2

kteam = square([1,2,3])
for value in kteam:
    print(value)

klist = [lambda x: x**2 , lambda x : x**3]
print (klist[0](1))

"""
funt = lambda x,y : x+y
k1 = [1,2,3]
k2=[1,2,3]
kteam = map(funt,k1,k2)
print (list(kteam))
"""











       