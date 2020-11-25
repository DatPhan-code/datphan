import enum
import zlib

s ="hello helloo helloo"
t = zlib.compress(s.encode("utf-8"))

print(t)
print(zlib.decompress(t))


# shuffle() : tron list
from random import shuffle
li = [1,23.4]
shuffle(li)
print(li)

#list comprehension

li =[12,24,35,70,88,120,155]
li2 =[]
for x in li:
    if x % 5!=0 and x %7!=0:
        li2.append(str(x))
print(",".join(li2))

li3 =[x for x in li if x %5!=0 and x%7!=0]
print(li3)

li4 = [2,3,5,6,8,14]
li5 =[x for x in li4 if x%2!=0]
print (li5)


li = [12,24,35,70,88,120,155]
 # Code by Quantrimang.com
a= [x for i,x in enumerate(li)if i%2!=0]
print (a)




     
    
        

        
    
    

