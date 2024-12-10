def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    while k > 0:
        result *= n
        n -= 1
        k -= 1
    return result

    """Original version:
    result = 1
    while k > 0:
        result = result * (n - k + 1)
        k -= 1
    return result
    """
    """for version:
    result = 1
    for i in range(k):
        result *= n
        n -= 1
    return result
    """


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(1, n+1):
        if i % k == 0:
            print(i)
            count += 1
    return count
    """Original version:
    count = 0
    while n > 0:
        if n % k == 0:
            count += 1
        n -= 1
    return count
    """


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    while y > 0:
        result += y % 10
        y = y // 10
    return result


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 100 == 88:
            return True
        n = n // 10
    return False

# Alternate solution
def double_eights(n):
    while n:
        if n % 10 == 8 and n // 10 % 10 == 8:
            return True
        n = n // 10
    return False

# Alternate solution
def double_eights(n):
    pre_eight = False
    "bool 函数"
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and pre_eight:
            "这一行检查当前位是否为 8, 并且 pre_eight 是否为 True。"
            return True
        elif last_digit == 8:
            """如果当前位是 8, 但 pre_eight 还为 False, 说明当前位是 8, 但前一位还不是 8。
            在这种情况下, 我们把 pre_eight 设置为 True, 表示我们已经发现了一个 8, 但还需要继续检查后面的数字。
            """
            pre_eight = True
        else:
            pre_eight = False
        n //= 10
    return False
