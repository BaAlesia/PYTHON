Задача:
Напишите код, после выполнения которого мы получим такой результат:
    
1
22
333
4444
55555
   
Решение:
for i in range (1, 6) :
    print (str(i)*i)
    
Решение (с пробелами):   
for i in range(1, 6):
    print((str(i) + ' ') * i)
    
Решение:  
for i in range(1, 6):
 for k in range(i):
  print(i, end='')
 print()
    
Решение:
print(*[(str(i)+' ') *i for i in range(1, 6)], sep = '\n')

Решение:
print('''1
22
333
4444
55555''')
    
Решение:  
a = 1
b = 22
c = 333
d = 4444
e = 55555
def f(a,b,c,d,e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    
print(a)
print(b)
print(c)
print(d)
print(e)
