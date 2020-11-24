"""
n = int(input('Nhap so:' ))
d = dict()
for i in range(1,n+1):
    d[i] =i*i

print (d)

print '----------------bai 2--------'


print '-------------'

n =int(input('nhap so:'))
def square(num):
    return num **2
print ('Binh phuong laf: ', square(n))


"""

"""
class PrintUpper:
    def __init__(self):
        self.name = ""

    def setupper(self):
        self.name = raw_input('Input your string: ')

    def printupper(self):
        print "Name before upper is : " , self.name
        print "Name after upper is : " , self.name.upper()
str = PrintUpper()
str.setupper()
str.printupper()
"""
"""
class PrintUpper:
    def __init__(self, name):
        self.name = name

   # def setupper(self):
   #     self.name = input('Input your string: ')

    def printupper(self):
        print "Name before upper is : " , str.name.upper()
       # print "Name after upper is : " , str.name.upper()
str = PrintUpper("ngyuyen")
#str.setupper()
str.printupper()
"""



"""
class Infoclass:
    def __init__(self):
        self.lop = ""
    def inputlop(self):
        self.lop = input('Moi Nhap lop: ')
    def printlop(self):
        print "lop nhap vao la:", self.lop
str = Infoclass()
str.inputlop()
str.printlop()
"""


"""
print (r'"is\'t" true')
print ('c:\\path')
"""



#list comprehension
cub3 = []
for x in range(9):
    if x > 4 :
        cub3.append(3**x)
    print(cub3)
j=[]
for x in range(2000,2300):
    if(x%7==0) and (x %5 !=0):
        j.append(str(x))
print ("ket qua la:")
print (",".join(j))
"""
items = [x for x in raw_input("nhap mo chuoi:").split(",")]
items.sort()
print (','.join(items))
"""
items = input("nhap chuoi:").split(",")
for x in items:
    items.sort()
print (','.join(items))




