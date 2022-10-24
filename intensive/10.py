print('Enter seat number')
number = int(input())
coupe = number/4
if coupe % 1 == 0:
    print(coupe)
else :
    print(coupe//1 + 1)