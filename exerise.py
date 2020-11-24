import datetime

x = "Toi di hoc"
print (x.translate)

x = "hello"
y = 15

print(bool(x))
print(bool(y))

list = ["a", "b","c"]
list[1] = "e"
list.insert(0, 'f')
print(list)

list = ["a","b","c"]
list2 = ['n','m','k']
list.extend(list2)
print (list)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i=i+1

fruits = ['Banana', 'apple','oragne']
newlist = [ x for x in fruits if "a" in x]
print(newlist)

newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return abs(n-50)
mylist=[100,50,65,82,23]
mylist.sort(key=myfunc)
print(mylist)


list1 = ["a","b","c"]
list2= [1,2,3]
for x in list2:
    list1.append(x)
    print(list1)

fruits = ["apple" ,"banana","cherry"]
print (fruits[2])

dict = {"name": "Datphan" , "age":18,"DOB":1984}
for x in dict.items():
    #print(dict[x])
    print(x)
    #print(dict.keys)

#whilr loop
i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i+=1

#continue statement
i =0
while i < 6:
    i +=1
    if  i ==3:
        continue
    print(i)
# defaul arrgument
def my_function (country = 'VN'):
    print("My country :" + country)
my_function()
my_function("singapore")

#lambda
x = lambda a, b : a*b
print(x(5,6))

#inhertance
class Person:
    def __init__(self, name , yearold):
        self.name = name
        self.yearold = yearold
    
    def Printname(self):
        print(self.name, self.yearold)

x = Person("Join", 23)
x.Printname()

class Student(Person):
    def __init__(self , name, year, years):
        Person.__init__(self , name, year)
        self.graduationyear = years
x = Student("Dat",29,2019)
print(x.graduationyear)

x = datetime.datetime(2018,01,12)
print(x.strftime("%m"))

#RegEx
import re

txt = "The rain in spain"
x = re.search("^The.*spain$", txt)
print(x)
x = re.findall("r..n",txt)
print(x)

yearold = 20
txt = " I am {:.2f} year old"
print (txt.format(yearold))






