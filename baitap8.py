import re
#Yêu cầu:
#Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.
#Ví du: Nếu những từ sau đây là đầu vào của chương trình: 3 quantrimang.com và 2 python. Đầu ra sẽ là ['3', '2']

str = "3 qtm, 3 nguyenvancu"
result = re.findall("\d+",str)
print(result)


#In chuỗi Unicode "Hello world"
unicodestring = u"Nguyễn văn A"
print(unicodestring)

#Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).

n = 5
sum = 0.0
if n > 0:
    for x in range(1,n+1):
        sum += round(float(int(x)/(int(x)+1)))  
else:
    print(u"Số không hợp lệ")

print (u"Kết quả là: ",sum)



    