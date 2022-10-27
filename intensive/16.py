print('Введите координаты первого отрезка')
a1, b1 = [int(i) for i in input().split()]
print('Введите координаты второго отрезка')
a2, b2 = [int(i) for i in input().split()]
if b1 < a2 or a1 > b2:
    answer = ('Пустое множество')
elif (a1 == a2 and b1 == b2) or (a2 < a1 and b1 < b2) or (a1 == a2 and b1 < b2):
    answer = (a1, b1)
elif (a1 < a2 and b1 < b2) or(a1 < a2 and b1 == b2):
    answer = (a2, b1)
elif (a1 < a2 and b2 < b1) or (a1 == a2 and b2 < b1):
    answer = (a2, b2)
elif (a1 > a2 and b1 ==b2) or (a1 > a2 and b1 > b2):
    answer = (a1, b2)
elif a1 < a2 and a2 == b1:
    answer = (a2)
elif a2 < a1 and a1 == b2:
    answer = (a1)
print(answer)










