LAB_SOURCE_FILE=__file__


HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    return (1 if n % 10 == 8 else 0) + num_eights(n // 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        return abs(n % 10 - (n // 10) % 10) + digit_distance(n // 10)
    
    """
    Alternative:
    def helper(n, pre_digit):
        if n == 0:
            return 0
        else:
            cur_digit = n % 10
            return abs(cur_digit - pre_digit) + helper(n // 10, cur_digit)
    return helper(n // 10, n % 10)
    """


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n % 2 == 1: # n is odd
        return odd_func(n) + interleaved_sum(n - 1, odd_func, even_func)
    else: # n is even
        return even_func(n) + interleaved_sum(n - 1, odd_func, even_func)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    coins = [1, 5, 10, 25]

    def count_coins_helper(amount, coin_index):
        if amount == 0: # 如果余额为0，则证明找到了一种组合
            return 1
        elif amount < 0: # 没有找到组合
            return 0
        elif coin_index >= len(coins):
            return 0
        
        coin = coins[coin_index] # 当前硬币面额

        # 1. 使用当前硬币
        # 2. 不使用当前硬币，直接尝试下一个硬币
        return count_coins_helper(amount - coin, coin_index) + count_coins_helper(amount, coin_index + 1)
    return count_coins_helper(total, 0)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        spare = 6 - start - end
        move_stack(n - 1, start, spare)
        print_move(start, end)
        move_stack(n - 1, spare, end)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else mul(x, f(f)(sub(x, 1))))
    # 外层lambda: 定义了一个接受函数 f 的 lambda 表达式，它返回的是 f(f)
    # 内层lambda: 首先接收一个参数 f, 然后返回一个函数, 这个返回的函数接受一个整数 x
                # 对于 x > 0 时, 它使用 mul(x, f(f)(sub(x, 1))) 来计算阶乘:
                    # x * (x-1) * (x-2) * ... * 1
                    # 这里的 mul(x, ...) 用于乘法，sub(x, 1) 用于计算 x - 1
    # 当调用 make_anonymous_factorial()(n) 时，
    # 首先会调用 (lambda f: f(f))，这会将 f(f) 作为参数传递进去，从而使 f 能够递归调用自己。
    # 然后再递归内层lambda

    """
    Alternative: 没有递归
    return lambda n: reduce(mul, range(1, sub(n, 0) + 1), 1)

    Alternative 2: 有递归
    return (lambda f: f(f, x))(lambda f, x: 1 if x == 0 else x * f(f, x - 1))
    """

