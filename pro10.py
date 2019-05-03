sum = 0
for i in range(1,10000):
  count = 0
  for j in range(1,10000):
    if i % j == 0:
      count += 1
  if count == 2:
    sum += i
print(sum)
