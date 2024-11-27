"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    pig_out = False
    all_dices = [dice() for i in range(num_rolls)]
    """
    这是一个列表推导式，表示通过 range(num_rolls) 生成一个包含 num_rolls 个元素的列表，
    每个元素都是 dice() 函数的返回值，也就是说，它会执行 num_rolls 次掷骰子的操作。
    """
    for side in all_dices:
        if side == 1:
            pig_out = True
    return 1 if pig_out else sum(all_dices)
    """Other way:
    result = 0
    for _ in range(num_rolls):
    # 其中的 _ 被用作一个占位符，表示你不需要关心循环变量的具体值。
        roll = dice()
        # 每次调用 dice()，获取一个骰子的结果
        if roll == 1:
            return 1
        result += roll
    return result
    """
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    assert player_score < 100 or opponent_score < 100, 'The game should be over.'
    return max(abs(3 * ((opponent_score // 10) % 10) - player_score % 10), 1)
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    else:
        return roll_dice(num_rolls, dice=six_sided)
    "记得带上函数形参"
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    count = 0
    k = 1
    while k <= n:
        if n % k == 0:
            count += 1
        k += 1
    return count
    """Other way:
    count = 0
    for i in range(1, n+1):    
        if n % i == 0:    # If i is a divisor of n
                count+= 1
    return count
    """
    """Other way:
    上面这个方法的时间复杂度是 O(n)，如果 n 较大，可以优化为 O(√n)，通过只遍历到 √n 来减少计算量。
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 1
            if i != n //i:     # 当 n = 15, i range (1, 4), but n // 3 = 5, 
                               # i 取不到 5, 但 count 要加上
                count += 1
    return count
    """
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if num_factors(score) in [3, 4]:
        "满足是 3 or 4, 可以 [3, 4] 表达"
        while not is_prime(score):
            "while not 用法"
            score += 1
    return score
    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    total_score = player_score + take_turn(num_rolls, player_score, opponent_score, dice=six_sided)
    return sus_points(total_score)
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            "Player 0's turn"
            num_rolls = strategy0(score0, score1)
            score0 = update(num_rolls, score0, score1, dice)
        else:
            "Player 1's turn"
            num_rolls = strategy1(score1, score0)
            score1 = update(num_rolls, score1, score0, dice)
        
        "After the turn, switch to the other player"
        """The expression who = 1 - who
        ensures that the value of who switches between 0 and 1 after each turn.
        """
        who = 1 - who 
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def strategy(score0, score1):
        """This is the strategy function returned by always_roll(n).
        It always returns n, regardless of the scores.
        """
        return n
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    "Get the first roll value from strategy"
    first_roll = strategy(0, 0)

    "Test the strategy with various score combinations"
    for score0 in range(0, goal, 1):
        "Test player 0 scores from 0 to goal in steps of 1"
        for score1 in range(0, goal, 1):
            "Test opponent scores from 0 to goal in steps of 1"
            if strategy(score0, score1) != first_roll:
                return False
    return True
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    因为四个数字分别调用了 10 次, 在 40 次 sample_count 中。
    平均值为 3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def average(*args):
        total = 0
        for _ in range(samples_count):
            total += original_function(*args)
        return total / samples_count
    return average
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"

    "Initialize a variable to store the maximum average score and the number of rolls that gives it"
    max_avg_score = 0
    best_num_rolls = 1

    for num_rolls in range(1, 11):
        "range(a, b) 表示从 a 开始，直到 b-1 结束的整数序列。"
        averaged_roll = make_averaged(roll_dice, samples_count)
        avg_score = averaged_roll(num_rolls, dice)
        "对于 dice = make_test_dice(), 依次从投 1 个, 到投 max_roll 个, 分别计算 avg_score, 取最高值的 num_roll"

        "If this average score is better than the previous best, update the best number of rolls"
        if avg_score > max_avg_score:
            max_avg_score = avg_score
            best_num_rolls = num_rolls

    return best_num_rolls
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    boar_brawl_score = boar_brawl(score, opponent_score)
    "如果 Boar Brawl 得分大于等于阈值，选择不掷骰子"
    if boar_brawl_score >= threshold:
        return 0
    "否则，选择掷 `num_rolls` 个骰子"
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    new_score = sus_update(num_rolls, score, opponent_score, dice=six_sided)

    "判断分数的增长是否大于等于 threshold"
    "如果分数增长大于等于 threshold, 返回 0, 不掷骰子"
    if new_score - score >= threshold:
        return 0
    else:
        return num_rolls  # Remove this line once implemented.
    "否则，继续按照 num_rolls 掷骰子"
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    "If the player is close to the goal, be more conservative."
    if score > 90:
        return 1
    
    elif score < opponent_score:
        "If the player is behind and needs to catch up, roll more dice."
        return 7
    elif score > opponent_score:
        "If the player is behind and needs to catch up, roll more dice."
        return 3
    
    "Default strategy: roll 6 dice."
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()