lst = []
for i in range(1, 11):
  s = [
    str(i * j).center(2) + '|' 
    for j in range(1, 11)
      ]
  lst.append(s)
  
for elem in lst:
  print(*elem, end='\n')
  print('-' * 39)
