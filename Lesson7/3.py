print('Enter two numbers')
one, two = [int(i) for i in input().split()]
print('Enter action')
action = input()
if action == '*':
    answer = (one * two)
elif action == '/' and two != 0:
    answer = (one / two)
elif action == '+':
    answer = (one + two)
elif action == '-':
    answer = (one - two)
elif action == ('/') and two == 0:
    answer = ('На ноль делить нельзя!')
else:
    answer = ('Неверная операция')
print(answer)

















