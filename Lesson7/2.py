print('Enter the sides of the triangle')
a, b, c = [int(i) for i in input().split()]
if (a == b and c < b, a > b) or (a == c and b < c, b > c) or (b == c and a > c, a < c):
    answer = ('Равнобедренный')
elif a == b ==c:
    answer = ('Равносторонний')
elif (a < b < c) or (a < c < b) or (c < a < b) or (c < b < a) or (b < a < c) or (b < c < a):
    answer = ('Разносторонний')
print(answer)

