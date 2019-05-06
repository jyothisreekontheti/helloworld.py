p = 1
while(1):
  r = int(input())
  if r == 0:
    exit()
  else:
    c = int(input())
    l1,num,count = [],[],0
    for i in range(r):
      l1.append(input())
    for i in range(r):
      for j in range(c):
        if l1[i-1][j] == '*' or l1[i][j-1] == '*' or l1[0][j] == '*' or l1[i][0] == '*':
          count += 1
	  num.append(count)
  print(num)
  print("Puzzle #",p)
  print("Across")
  for i in l1:
    i = i.split('*')
    while '' in i:
      i.remove('')
    for j in i:
      print(j)
  print("Down")
  
  for i in range(c):
    for j in range(r):
      if l1[j][i] == '*':
        print('')
      else:
       print(l1[j][i],end = '')
    print('')
  p += 1

