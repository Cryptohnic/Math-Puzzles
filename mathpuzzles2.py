import random

print("""
Since we have ten different people, we know that one person's space can be numbered as total_of_colors%10 assuming we assign each person a numerical value (0-9)
Only one person meets the criteria of the actual total and they always will so we can use that to always know the color of their hat. Let’s also number our different hats (0-9) so we can calculate a total value based on the hats present. In this scenario, we can say that total_we_can_see+on_our_head=total_total. If we assume we are always the spot where the total%10==position and we also recognize that the total has to be <= what_we_see+9,
we can add 9 to what_we_see to get possible_total and subtract one until possible_total%10=space. This possible total will be the total that works
for this space assuming the condition that we are at the space that is equal to the total%10.
Now we can check if possible_total-what_we_see==color on head and this will be true for exactly one person. Everyone will pass the class and it will always be the person in the space==total%10
 
0 - red
1 - orange
2 - yellow
3 - green
4 - blue
5 - indigo
6 - violet
7 - maroon
8 - turquoise
9 - gray

Preconditions: Everyone is assigned a number in order (0-9) and each color is assigned a value (0-9)
----------------------\n""")
color_names=['red','orange','yellow','green','blue','indigo','violet','maroon','turquoise','gray']
people=[random.randint(0,9) for _ in range(10)]
total_colors=sum(people)
for i in range(len(people)):
    print(f'Person: {i} | Color: {people[i]} | Total: {total_colors}')
    what_we_see=total_colors-people[i]
    greatest_possible_total=what_we_see+9 # We know what we see+9 has to be greater than or equal to real total
    while greatest_possible_total%10!=i: # Get our total into our form where total%10 equals our position since that condition has to be true for one person
        greatest_possible_total-=1
    possible_total=greatest_possible_total # This number is what our total has to be if the current_position=sum%10
    guess=possible_total-what_we_see
    print(f'Our guess is: {color_names[guess]} and the color on our head is {color_names[people[i]]}\n')
    if color_names[guess]==color_names[people[i]]:
       print(f'\nIt worked! We are at spot {i} and the total of our colors ends in a {total_colors%10}')
       break
else:
    print('\nIt didn\'t work')
