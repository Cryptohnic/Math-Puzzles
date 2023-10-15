import random

# How to equally divide a group of chips into two stacks with equal amount of any specified color chip facing up while blindfolded
# Only information you need is the the amount of at least one of the colors of the chips and which color they are
num_coins=int(input("""
                    The Evil Professor is back to his shenanigans. The professor has placed a large
                    pile of coins on his desk. Each coin is identical, one side is painted red, and one side is
                    painted black. The two sides are indistinguishable by feel.
                    The Professor blindfolds you and says that currently, 25 coins have the red side facing
                    up. He then says that he will fail you unless you separate the coins into two piles with an
                    equal amount of coins with the red side facing up.
                    Can you divide the coins even though you are blindfolded or are you doomed to repeat
                    their class?
                    
                    
                    How many number of coins should be on the table? (Must be >= to 25): """))
num_red=25
random_pile=['B' for _ in range(num_coins-num_red)]+['R' for _ in range(num_red)]
random.shuffle(random_pile)
print(f'\nHere is our full pile: {random_pile} - It has {random_pile.count("B")} black coins and {random_pile.count("R")} red coins.')
red_len_pile,other_pile=random_pile[:num_red],random_pile[num_red:]
print(f'\nHere is our first subpile from the main - It has {red_len_pile.count("B")} black coins and {red_len_pile.count("R")} red coins. It\'s size is {num_red} or the same as the amount of red coins')
print(f'Here is our second subpile from the main - It has {other_pile.count("B")} black coins and {other_pile.count("R")} red coins. It\'s size is {num_coins-num_red}')
red_len_pile=['B' if item=='R' else 'R' for item in red_len_pile]
print(f'Here is the first subpile after flipping each of the coins - It has {red_len_pile.count("B")} black coins and {red_len_pile.count("R")} red coins.')
print("""
                    As you can see they have the same amount of red coins.
                    This works because you know the exact amount of one color of the coins. Since you know there are 
                    25 red coins, if you make a group of 25 random coins from the group, the amount of black coins in the
                    pile will be equal to the leftover amount of reds in the main pile. By flipping every coin in this pile
                    of 25, you will now have an equal amount of reds.
      """ if red_len_pile.count('R')==other_pile.count('R') else 'Didn\'t work')