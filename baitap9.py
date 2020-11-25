#Viết chương trình sử dụng generator để in số chẵn trong khoảng từ 0 đến n, cách nhau bởi dấu phẩy, n là số được nhập vào.

#Ví dụ nếu n=10 được nhập vào thì đầu ra của chương trình là: 0,2,4,6,8,10


n =int(input("nhao so n = ")) 
values = []
def printsochan(n):
    i = 0 
    while i <= n :
        if i%2 ==0:
            yield i
        i+=1

for i in printsochan(n):
    values.append(str(i))
print ("so chia het cho 2 tu 0 den n: ",",".join(values))





