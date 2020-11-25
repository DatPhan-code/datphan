#Viết chương trình sử dụng generator 
# để in số chia hết cho 5 và 7 giữa 0 và n,
#cách nhau bằng dấu phẩy, n được người dùng nhập vào.


n = int(input("Please Enter number : "))
def printchiahet(n):
    for i in range(n+1):

        if (i%5==0) and (i % 7 ==0):
            yield i
        

values = []
for i in printchiahet(n):
    values.append(str(i))
print ("Chia het cho 5 va 7: ",",".join(values))


#assert 
li =[2,4,6,8]
for i in li:
    assert i%2==0

#import
import random
print (random.random()*100)

import random
print (random.choice([i for i in range(0,200) if i%5==0 and i%7==0]))



