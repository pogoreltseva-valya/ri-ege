print('Enter cell coordinates (4 numbers from 1 to 8)')
st1 = int(input())
str1 = int(input())
st2 = int(input())
str2 = int(input())
if (str1 == str2 - 1 or str1 == str2 + 1 or str1 == str2) and (st1 == st2 or st1 == st2 - 1 or st1 == st2 + 1):
    print('Yes')
else:
    print('No')