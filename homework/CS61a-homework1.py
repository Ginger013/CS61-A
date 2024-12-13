Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from operator import add, sub
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub(a, b)
    else:
        f = add(a, b)
    return f(a,b)

a_plus_abs_b(3, 4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a_plus_abs_b(3, 4)
  File "<pyshell#9>", line 6, in a_plus_abs_b
    return f(a,b)
TypeError: 'int' object is not callable
def a_plus_abs_b(a, b):
    if b < 0:
        f = sub
    else:
        f = add
    return f(a,b)

a_plus_abs_b(3, 4)
7
a_plus_abs_b(3, -4)
7
‘’‘
SyntaxError: invalid character '‘' (U+2018)
'''
赋值 f 时不要把 f 设置为运算结果，而是让它保持为一个函数，然后在函数中根据条件来选择哪个运算函数
'''
'\n赋值 f 时不要把 f 设置为运算结果，而是让它保持为一个函数，然后在函数中根据条件来选择哪个运算函数\n'
'''
下面的函数为：取三个数中最小的两个数 a，b，然后计算 a*a + b*b。
'''
'\n下面的函数为：取三个数中最小的两个数 a，b，然后计算 a*a + b*b。\n'

def two_of_three(x, y, z):
    return add(min(x, y) * min(x, y), min(max(x, y), z) * min(max(x, y), z))

two_of_three(5, 3, 1)
10
'''
另一种解法：x*x + y*y + z*z - max(x, y, z) * max(x, y, z)
'''
'\n另一种解法：x*x + y*y + z*z - max(x, y, z) * max(x, y, z)\n'

'''
第三题：一个函数，取大于 1 的整数 n，return 比 n 小，并且能整除 n 的最大整数。
a 整除 b 指：b % a == 0 (a < b)
'''
'\n第三题：一个函数，取大于 1 的整数 n，return 比 n 小，并且能整除 n 的最大整数。\na 整除 b 指：b % a == 0 (a < b)\n'

def largest_factor(n):
     for i in range(n-1, 0, -1):
         if n % i == 0:
             return i

            
largest_factor(101)
1
largest_factor(102)
51
'''
for i in range(n-1, 0, -1): 的作用是：
从 n-1 开始递减，直到 1（不包括 0）。每次循环 i 的值会逐步减小.
可以用于从大到小进行迭代。

range(n-1, 0, -1) 是一个生成整数序列的函数，具体参数含义如下：
    n-1：序列的起始值。即从 n-1 开始。
    0：序列的结束值，但不包括 0。所以序列会停止在 1，不包括 0。
    -1：步长.表示每次循环时，序列中的值会减小 1。所以它会从 n-1 开始，每次递减，直到 1 为止。
'''
'\nfor i in range(n-1, 0, -1): 的作用是：\n从 n-1 开始递减，直到 1（不包括 0）。每次循环 i 的值会逐步减小.\n可以用于从大到小进行迭代。\n\nrange(n-1, 0, -1) 是一个生成整数序列的函数，具体参数含义如下：\n    n-1：序列的起始值。即从 n-1 开始。\n    0：序列的结束值，但不包括 0。所以序列会停止在 1，不包括 0。\n    -1：步长.表示每次循环时，序列中的值会减小 1。所以它会从 n-1 开始，每次递减，直到 1 为止。\n'

'''
第四题：if function VS statement
'''
'\n第四题：if function VS statement\n'

'''
先定义一个函数，does the same thing as an if statement
'''
'\n先定义一个函数，does the same thing as an if statement\n'
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

    
'''
下面的可能会不一样
'''
'\n下面的可能会不一样\n'
def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

    
def with_if_function():
    return if_function(cond(), true_func(), false_func())

def cond():
    return True

def true_func():
    print(42)
    return 47

def false_func():
    print(47)
    return 42

print(with_if_statement())
42
47
print(with_if_function())
42
47
47
def cond():
    return 47
def true_func():
    
SyntaxError: invalid syntax
def cond():
    return 47

def true_func():
    print(47)

    
def false_func():
    print(42)

    
print(with_if_statement())
47
None
print(with_if_function())
47
42
None
def cond():
    return True

def true_func():
    print(47)

    
def false_func():
    print(42)

    
print(with_if_statement())
47
None
print(with_if_function())
47
42
None
'''
总结：在 with_if_function() 函数调用时，true_func() 和 false_func() 会先被运行打印出47，42，但 return 值是 None，所以 if_function 中 true_result 返回 None。
'''
'\n总结：在 with_if_function() 函数调用时，true_func() 和 false_func() 会先被运行打印出47，42，但 return 值是 None，所以 if_function 中 true_result 返回 None。\n'
'''
最终版代码展示：
'''
'\n最终版代码展示：\n'
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

    
def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

    
def with_if_function():
    return if_function(cond(), true_func(), false_func())

def cond():
    return True

def true_func():
    return 47

def false_func():
    print(42)

    
print(with_if_statement())
47
print(with_if_function())
42
47
'''
小结：原因在于 if_function(cond(), true_func(), false_func()) return 的时候会先把括号内三个函数过一遍，有 print 的就会打印出来，return 值有没有是在后续函数运行调用中用到的。
'''
'\n小结：原因在于 if_function(cond(), true_func(), false_func()) return 的时候会先把括号内三个函数过一遍，有 print 的就会打印出来，return 值有没有是在后续函数运行调用中用到的。\n'

'''
第五题：Hailstone
1. 取正整数 n
2. n 为偶数，被 2 整除
3. n 为奇数，*3 + 1
4. 重复上述过程直到 n 为 1
a = Hailstone(x)，a 为整个 step 数。
例如 a = Hailstone(10), return 7
'''
'\n第五题：Hailstone\n1. 取正整数 n\n2. n 为偶数，被 2 整除\n3. n 为奇数，*3 + 1\n4. 重复上述过程直到 n 为 1\na = Hailstone(x)，a 为整个 step 数。\n例如 a = Hailstone(10), return 7\n'
def Hailstone():
    '''
    start at n
    while we're not at 1
    set n to the next hailstone value
    return count(?)
    '''
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else
        
SyntaxError: expected ':'
def Hailstone():
    '''
    start at n
    while we're not at 1
    set n to the next hailstone value
    return count(?)
    '''
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1 ''' count = count +1 '''
        
SyntaxError: invalid syntax
def Hailstone():
    '''
    start at n
    while we're not at 1
    set n to the next hailstone value
    return count(?)
    '''
    count = 0
...     while n != 1:
...         if n % 2 == 0:
...             n = n / 2
...         else:
...             n = 3 * n + 1
...         count += 1
...         '''
...         count = count + 1
...         '''
...     return count
... 
>>> def Hailstone(n):
...     '''
...     start at n
...     while we're not at 1
...     set n to the next hailstone value
...     return count(?)
...     '''
...     count = 0
...     while n != 1:
...         if n % 2 == 0:
...             n = n / 2
...         else:
...             n = 3 * n + 1
...         count += 1
...         '''
...         count = count + 1
...         '''
...     return count
... 
>>> Hailstone(7)
16
>>> 
>>> '''
... 另一种解法：递归法。（上面一种是迭代法，即循环。）
... '''
'\n另一种解法：递归法。（上面一种是迭代法，即循环。）\n'
>>> def Hailstone(n, count = 0):
...     if n == 1,
...     
SyntaxError: invalid syntax
>>> def Hailstone(n, count = 0):
...     if n == 1:
...         return count
...     if n % 2 == 0:
...         return Hailstone(n/2, count + 1)
...     else
    
SyntaxError: expected ':'
def Hailstone(n, count = 0):
    if n == 1:
        return count
    if n % 2 == 0:
        return Hailstone(n/2, count + 1)
    else:
        return Hailstone(3 * n + 1, count + 1)

    
Hailstone(7)
16
Hailstone(1)
0
'''
还可以把中间过程都罗列出来，这个之后再学。
'''
'\n还可以把中间过程都罗列出来,这个之后再学。\n'
