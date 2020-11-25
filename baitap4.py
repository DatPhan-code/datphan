import time;
import calendar

var = '123'
print(var)

list =['xyz','abc', 'cds']
list[2]='123'
print 'xinchao' , list
del list[1]
print list

#list index
list = ['abc','xyz','khj']
print list.index('xyz')

#compare
tupl1 =(123, 'bcd')
tuple2 =(456, 'cdf')
print cmp(tupl1, tuple2)

#dictionary
dict = {'name': 'DatPhan', 'age': 7, 'school': 'Hau Giang'}
dict['name'] = 'Phan Dat' 
print dict

#time

localtime = time.asctime(time.localtime(time.time()))
print 'Local time : ' , localtime

calendar = calendar.month(2008,1)
print calendar

#function
def printme (str):
    print str
    return 
#call printme
printme('this is my friend')

def changme (list):
    list=[1,2,3,4]
    print 'List in local : ' ,list
    return

mylist=(10,20,30)
changme(mylist)
print 'List sau khi change : ' , mylist

def printinfo (name , age):
    print 'name: ' , name
    print 'tuoi: ' , age
    return

printme('Thong tin ca nhan : ') 
printinfo(name= 'jack', age =30)

def info(name , age =30):
    print 'name',name
    print 'age', age
    return

info(name = 'tuan')

def function(args, *vartuple):
    print "output is:"
    print args
    for var in vartuple:
        print var
    return

function(10)
function(70,60,50)

#return stament
def sum(arg1, arg2):
    total = arg1 + arg2
    print "Ket qua la : " , total
    return total
total = sum(10,20)
print 'ket qua 2 la :' , total

str = raw_input('Please enter: ')
print 'Your  input ' , str

def temp_convert (var):
    try:
        return int(var)
    except ValueError, Argument:
        print "The arrgument does not content number" , Argument

temp_convert("123")
    















