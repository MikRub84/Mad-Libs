import random


print("You are Wellcome to the Game of Craps.Try your luck!")

player = input('Press enter to roll dice: ')
n = random.randint(1, 6)
m = random.randint(1, 6)
sum = n + m
print('The sum of dice is: ', n, ' + ', m, ' = ', sum)
if sum == 7 or sum == 11:
    print('Congrats, You Win!')
    print('Game Over')
elif sum == 2 or sum == 3 or sum == 12:
    print('Sorry, You Lose!')
    print('Game Over')
elif sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10:
    goal = 0
    print('Now your GOAL number is: ', sum)
    while goal != sum or goal != 7:
        player = input('Press enter to roll dice: ')
        goal = 0
        n = random.randint(1, 6)
        m = random.randint(1, 6)
        res = n + m
        goal += res
        print('The sum of dice is: ', n, ' + ', m, ' = ', goal)       
        if goal == 7:
            print('Sorry, You Lose!')
            print('Game Over')
            break
        elif goal == sum:
            print('Congrats, You Win!')
            print('Game Over]')
            break
        
