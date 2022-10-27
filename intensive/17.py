print('Introduction color')
color1 = input()
print('introduction color')
color2 = input()
if color1 == 'красный' and color2 == 'синий':
    answer = ('фиолетовый')
elif color1 == 'красный' and color2 == 'жёлтый':
    answer =('оранжевый')
elif color1 == 'синий' and color2 == 'жёлтый':
    answer =('зелёный')
elif color1 == color2 == 'красный' or color1 == color2 == 'синий' or color1 == color2 == 'жёлтый':
    answer =(color1)
else:
    answer =('Error')
print(answer)