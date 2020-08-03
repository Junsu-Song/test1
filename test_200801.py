"""
print("Hello Bioinformatics")

import math
pi = math.pi
r = int(input("반지름:"))
print(round(pi*r**2), 6)
########################################
num1 = 3
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1**2, num2**2)
########################################
num1 = int(input("숫자:"))
if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")
########################################
num1 = int(input("숫자:"))
if num1 % 3 == 0 and num1 % 7 == 0:
    print("3과 7의 배수이다.")
elif num1 % 3 == 0:
    print("3의 배수이다.")
elif num1 % 7 == 0:
    print("7의 배수이다.")
else:
    print("3과 7의 배수가 아니다")
########################################
total = 0
for i in range(1, 11, 1):
    total += i
print(total)

n = int(input("숫자:"))
sum = 0
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
########################################
for i in range(2, 10, 2):
    for j in range(1, 10, 1):
        print(i,"x",j,"=",i*j)
        print(f"{i}x{j} = {i*j}")
        print("{}x{} = {}".format(i, j, i*j))
########################################
n = 5
t = 1
while n > 0:
    t *= n
    n -= 1
print(t)

n = int(input("입력:"))
t = 1
while n > 0:
    t *= n
    n -= 1
print(t)

n = int(input("입력:"))
t = 1
for i in range(1, n+1, 1):
    t *= i
print(t)
########################################
def greet():
    print("Hello, Bioinformatics")
greet()
greet()
##########################################
def mySum(n1, n2):
    print(f"{n1}+{n2} = {n1+n2}")
mySum(2,3)
mySum(5,7)
mySum(10,15)
print()

def mySum(n1, n2):
    return(f"{n1}+{n2} = {n1+n2}")
print(mySum(2,3))
print(mySum(5,7))
print(mySum(10,15))
##########################################
def F():
    n = 5
    total = 1
    while n > 0:
        total *= n
        n = n - 1
    return total
total = F()
print(total)

def FF(num):
    T = 1
    while num > 0:
        T *= num
        num = num - 1
    return T
num = 3
T = FF(num)
print(T)
##########################################
name = input("what your name:")
print("Hello %s" %name)
##########################################
sd = input("입력:")
if sd.isalpha():
    print("문자입니다")
elif sd.isnumeric():
    print("숫자입니다")
else:
    print("둘 다 아닙니다")
##########################################
import sys
try:
    num = int(sys.argv[1])
    print(10/num)
except ValueError:
    print("값을 입력하세요")
    sys.exit()
except ZeroDivisionError:
    print("0으로 못나눠요")
    sys.exit()
##########################################
a = "Bio"
b = "Informatics"
print(a +" "+ b)

a = "Bio"
b = "Informatics"
print(a +" "+ b)
"""
##########################################





##########################################





##########################################





##########################################





##########################################






##########################################






##########################################






##########################################





##########################################











