#bai 1
print( "=============Bai 1============")
j=[]
for i in range(2000,3200):
    if(i%7==0) and (i%5!=0):
        j.append(str(i))

print (",".join(j))

#bai 2
print ("=============Bai 2============")

x = 8
#x =int(input("Enter number: "))
def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
print (fact(x))

print ("=============Bai 3============")

n = 4
d = dict()
for i in range(1,n+1):

    d[i] =[i*i]
    print (d)

print ("=============Bai 4============")
"""
x = raw_input("Enter number: ")
l = x.split(",")
t = tuple(l)
print(t)
print(l)
"""
print ("=============Bai 5============")
"""
class OutPutstring:
    def __int__(self):
        self.str = "a"

   # def Getstring(self):
    #    self.str = raw_input("Enter string : ")
    
    def Printstring(self):
        print (self.str.upper())


output = OutPutstring()
#output.Getstring()
output.Printstring()
"""
print ("=============Bai 6============")

#num = int(input("nhap so: "))
def Binhphuong(num):
        return num ** 2
print(Binhphuong(3))
print (Binhphuong.__doc__)


print ("=============Bai 7============")
print (abs.__doc__)
print(int.__doc__)
print(input.__doc__)

print ("=============Bai 8============")
import math

c = 50
h = 30
value =[]
items = [x for x in input("Nhap gia tri cua d : ").split(",")]
for d in items:
    value.append(str(int(round((math.sqrt(2*c*float(d))/h)))))
   # print (','.join(value))
print (','.join(value))

print ("=============Bai 9============")

inputstr = input("Nhap chuoi: ").split(",")
for x in inputstr:
    inputstr.sort()
print(",".join(inputstr))

print ("=============Bai 10============")

line = []
while True:
    s = input("Moi nhap chuoi: ")
    if s:
        line.append(s.upper())
    else:
        break;
for sentence in line:
    print(sentence)

