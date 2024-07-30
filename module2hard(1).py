Latch = int(input("Введите число от 3 до 20: "))
while Latch < 3 or Latch > 20:
  print("Шипы сверху стали ближе на 10см, будьте внимательнее") 
  Latch = int(input("Введите число от 3 до 20: ")) 
print("В первом поле камни с числом -" , Latch)
code = []
for i in range(1,Latch):
        for j in range (i+1, Latch):
            if Latch % (i+j) == 0:
                code.extend([i, j])
code=list(map(str,code))
print("Код","".join(code))
