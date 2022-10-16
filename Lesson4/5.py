print('Enter 3 numbers')
a = int(input())
b = int(input())
v = int(input())
if a>0 and b>0 and v>0:
    print('3')
if (b<0 or a<0 or v<0) and (a>0 and b>0 or a>0 and v>0 or b>0 and v>0):
    print('2')
if a<0 and b<0 or a<0 and v<0 or b<0 and v<0:
    print('1')








