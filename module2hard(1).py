Latch = int(input("Введите число от 3 до 20: "))
while Latch < 3 or Latch > 20:
  print("Шипы сверху стали ближе на 10см, будьте внимательнее") 
  Latch = int(input("Введите число от 3 до 20: ")) 
print("В первом поле камни с числом -" , Latch)
key = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
code = []
for i in range(1,Latch):
        for j in range (i+1, Latch):
            if Latch % (i+j) == 0:
                code.extend([i, j])
code=list(map(str,code))
print("Код","".join(code))
