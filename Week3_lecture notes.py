#不是质数
#n = 191392131214
#把原来的数字变为从0 到根号n， 如果这个数字特别大例如：10** 10，我们可以去遍历10的5次方（10**5）

#b < n ** 0.5 找到一个数小于根号n
# n % b == 0 找到一个数使得n能被这个数整除

#n = 100
#n = 10 *10
#2 * 50
#5 * 20

#格式化补位,
x = 100
w = 5
print(f'|{x:{w}}|')
#结果：|  100|总共5位，在100前面补两位，
print(f'|{x:0{w}}|')
#结果：|00100|， 如果不足的就在前面补零

list(range(4, 10))
#[4, 5, 6, 7, 8, 9]
list(range(4, 10, 2))# 最后一位指的是step因为它是跳跃着走
#[4, 6, 8]两个两个range
list(range(4, 10, -2))
#[],结果就是没有，因为它向后走

from itertools import accumulate
from operator import add,mul
a = [1, 3, 5, 7]
b = list(accumulate(a, add))#连加
print(b)#结果：[1, 4, 9, 16]
b = list(accumulate(a, mul))#连乘
print(b)#结果：[1, 3, 15, 105]

a = [8, 10, 6, 1]
b = list(accumulate(a[::-1], mul))
print(b)#结果：[1, 6, 60, 480]

# from lecture notes:
def compute_fraction(sigma, tau):
    numerator = int(sigma)*(10 ** len(tau) - 1) + int(tau)
    denominator = (10 ** len(tau) - 1) * 10 ** len(sigma)
    return numerator, denominator

print(compute_fraction('123', '456'))
# result is (123333, 999000)

# to calculate length is use:
len('234')#3
len(234)# error
#或者
x =234
len(str(x))

# we would like to use gcd here:

from math import gcd
print(gcd(123333, 999000))
# result is 3,

print(123333 / 3, 999000 / 3)
#result: 41111.0 333000.0 得到两个数的最简数
#试一下，将两个最简的数相除，应该会得到答案类似于： 0.123456456456
print(41111 / 333000)
#结果是：0.12345645645645646 for the calculate as a/b, the reult will always showing a floating number like 2/4, result it 2.0

# if I want and get the result look like a integer format not floating number, I can do things like this:
print(4//2)
#result is , double slash always gives a integer interval, except for 4.0//2, 4//2.0, 4.0//2.0 the result is 2.0 also the floating number.

print(990/1233)                             #0.8029197080291971
print(gcd(990, 1233))                       #9
print(990//9)                               #110
print(1233//9)                              #137
print(110/137)                              #0.8029197080291971
print(990 % 1233)                           #990
print(gcd(1233, 990 % 1233))                #9
print(1233, 990 % 1233)                     #1233 990
print(990, 1233 % 990)                      #990 243
print(243, 990 % 243)                       #243 18
print(18, 243 % 18)                         #18 9
print(9, 18 % 9)                            #9 0

# while is for true or false
def our_gcd(a, b):
    while b != 0: #也可以直接俄while b: 它满足布尔代数
        a, b = b, a % b
    return a
print(our_gcd(1233,990))

a = 1233
b = 990
a, b = b, a % b #右边的 a, a+b 会返回一个tuple 然后这个左边的a, b 会分别赋值为这个tuple里的第一个和第二个。
print(a)#990
print(b)#243

print(our_gcd(*compute_fraction('123', '456'))) #3

def f(x):
    return x, 2 * x
print(f(1)) #(1, 2)

def f(x, y):
    return 2 *x, 2 * y
print(f(1, 2)) #(2, 4)
print(f(* f(1, 2))) #(4, 8)将f(1,2)的结果又带进方程里面乘了一遍
print(f(*(f(* f(1, 2)))))#(8, 16)

def f(x):
    return 2 * x
print(f(1,2,3))#TypeError: f() takes 1 positional argument but 3 were given

def f(* x):
    return 2 * x
print(f((1,2,3)))#(1, 2, 3, 1, 2, 3)

def f(* x):
    return 2 * x
print(f(1,2,3))#(1, 2, 3, 1, 2, 3)
print(f(f((0, 0)))) #(((0, 0), (0, 0)), ((0, 0), (0, 0)))一组结果再次带回方程里，结果为一组tuple
# * can remove one ()
print(f(*f(0, 0))) #(0, 0, 0, 0, 0, 0, 0, 0)
print(f(*f((0, 0)))) #((0, 0), (0, 0), (0, 0), (0, 0))

def output(numerator, denominator):
    print(f'{numerator}/{denominator}')

print(32 // 13, 32 % 13) #2 6
print(divmod(32, 13))   #(2, 6)

