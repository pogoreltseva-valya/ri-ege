print('Enter the sides of the triangle')
a, b, c = [int(i) for i in input().split()]
if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print('Yes')
else:
    print('No')




