import random


def rolling(amount_dice: int=2, type_dice: int=6):
    if amount_dice <= 0 or type_dice <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount_dice):
        roll: int = random.randint(1, type_dice)
        rolls.append(roll)

    return rolls


def rolling_dice():
    while True:
        try:
            amount_dice: str = input('How many dice would you like to roll? ')
            if amount_dice.lower() == 'exit':
                print('Thanks for playing!')
                break
            type_dice: str = input(f'What type of dice would you like to roll? (d4, d6, d8, d10, d12, d20) ')
            if type_dice == 'exit':
                print('Thanks for playing!')
                break
            amount = int(amount_dice)
            type_d = int(type_dice)

            rolls = rolling(amount, type_d)
            s_rolls = ', '.join(str(x) for x in rolls)
            print(f'You rolled {s_rolls} for a total of {sum(rolls)}')
        except ValueError:
            print('Please enter a valid number.')


if __name__ == '__main__':
    rolling_dice()


# rolling = True
#
#
# while rolling:
#     rolls = []
#     try:
#         amount_of_dice = int(input(f"How many dice would you like to roll?: "))
#         what_type_d = int(input("What type of die would you like to roll? (d4, d6, d8, d10, d12, d20): "))
#         if amount_of_dice <= 0 or what_type_d <= 1:
#             raise ValueError
#
#         for amount in range(1, amount_of_dice + 1):
#             rolls.append(random.randint(1, what_type_d))
#
#         s_rolls = ', '.join(str(x) for x in rolls)
#         print(f'You rolled {s_rolls} for a total of {sum(rolls)}')
#         keep_going = input("Would you like to go again? ").capitalize()
#         if keep_going != 'Yes':
#             rolling = False
#     except ValueError:
#         print('Please enter a valid number.')




