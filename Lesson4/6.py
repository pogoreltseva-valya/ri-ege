print('Enter 3 numbers')
a = int(input())
b = int(input())
n = int(input())
if a<b<n:
    print(a,b,n)
if b<a<n:
    print(b,a,n)
if a<n<b:
    print(a,n,b)
if b<n<a:
    print(b,n,a)
if n<b<a:
    print(n<b<a)
if n<a<b:
    print(n,a,b)
if a == b and a<n:
    print(a,b,n)
if a == n and a<b:
    print(a,n,b)
if b == n and b<a:
    print(b,n,a)
if a == b and a>n:
    print(n,b,a)
if a == n and a>b:
    print(b,a,n)
if b == n and b>a:
    print(a,b,n)
if a == b == n:
    print(a,b,n)











