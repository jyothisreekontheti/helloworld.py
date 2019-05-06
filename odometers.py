size,num,l1 = int(input()),int(input()),[]
l = '123456789'
start,limit = int(l[:size]),int(l[-size:])

def isAscending(num):
    if len(set(list(num))) == len(num):
        return 1
    return 0

def previous(num,l1):
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a - 1]

def next_num(num,l1):
    if num == l1[-1]:
        return l1[0]
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a + 1]

def next_nth_reading(num,n):
    if num == l1[-1]:



for x in range(start,limit + 1):
    if list(str(x)) == sorted(str(x)) and x % 11 != 0 and isAscending(str(x)):
        l1.append(x)

if num not in l1:
    print("Invalid")
else:
    print(previous(num,l1))
    print(next_num(num,l1))
