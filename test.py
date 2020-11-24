from functools import reduce

func = lambda x : x > 0 
func1= lambda x : str(x)
kteam =[-1,2,-3,5,6]

filterlist = filter(func,kteam)
list = map(func1,filterlist)
print(" ".join(list))

print("==================")

func = lambda x,y : x+y
func1 = lambda x: str(x)
k1 = {1,2,3}
k2 = {1,2,3}

kteam = map(func,k1,k2)
list =map(func1,kteam)

print(",".join(list))

print("==================")


def checkvalue (n):
    if n %2==0:
        print ("Day la so chan:")
    else:
        print ("Day la so le: ")
checkvalue(8)

print("==================")

def printdict():
    d =dict()
    for i in range(1,21):
        d[i] = i**2
# pirnt gia' tri cua dict
    for (k,v) in d.items():
        print (v)
printdict()

print("==================")

list ={1,2,3,4,5,6,7,8,9,10}
func = lambda x : x %2 ==0
func1 = lambda x : str(x)
emnuber = filter(func,list)
emuber1 = map(func1,emnuber)
print (" ,".join(emuber1))

print("==================")

class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg

error = MyError("cos gi do sai sai")
print(error)

print("==================")

#lay ten email 
import re
emailinput = input()
pat1 = "(\w+)@(\w+)\.(com)"
r =re.match(pat1,emailinput)
print(r.group(1))




      









