import random

# print('Welcome to game')
# print('[r] - rock\n[s] - scissors\n[p] - paper')
#
# user_score = 0
# active_game = 'yes'
# bot_score = 0
# variants = ['r', 's', 'p']
#
# while active_game == 'yes':
#     print('---- BEGINNING ----')
#     for i in range(3):
#         print(f'---- ROUND #{i+1} ----')
#         user_choice = input('Your choice: ')
#         bot_choice = random.choice(variants)
#         print(f'\tYou: {user_choice}\tbot: {bot_choice}')
#         if user_choice == bot_choice:
#             print('Draw')
#             user_score += 1
#             bot_score += 1
#         elif user_choice == 'r':
#             if bot_choice == 's':
#                 user_score += 1
#                 print('Player won!')
#             else:
#                 bot_score += 1
#                 print('Bot won!')
#         elif user_choice == 's':
#             if bot_choice == 'p':
#                 user_score += 1
#                 print('Player won!')
#             else:
#                 bot_score += 1
#                 print('Bot won!')
#         elif user_choice == 'p':
#             if bot_choice == 'r':
#                 user_score += 1
#                 print('Player won!')
#             else:
#                 bot_score += 1
#                 print('Bot won!')
#         else:
#             print('Something wrong')
#         print('-'*20)
#     if user_score > bot_score:
#         print(f'Player won game with score {user_score}')
#     elif user_score < bot_score:
#         print(f'Bot won game with score {bot_score}')
#     else:
#         print(f'Draw! {user_score}:{bot_score}')
#     active_game = input('Do you wanna play again? yes/no? ')
#     if active_game != 'yes' or active_game != 'no':
#         print('Sorry, i do not understand you')


points = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

cards = dict(zip([6, 7, 8, 9, 10, 2, 3, 4, 11], ['6', '7', '8', '9', '10', 'V', 'Q', 'K', 'A']))

print('Welcome to game "21 point"')
print(f'Here are all the meanings of the cards: {cards}')

sum_cards = points.pop(points.index(random.choice(points))) + points.pop(points.index(random.choice(points)))
sum_cards_bot = points.pop(points.index(random.choice(points))) + points.pop(points.index(random.choice(points)))

print(sum_cards)

while True:
    one_more_card = input('Do you want to take one more card ? yes/no: ')
    if one_more_card == 'no':
        break
    elif one_more_card == 'yes':
        point = points.pop(points.index(random.choice(points)))
        sum_cards += point
        print(f'You take card: {cards.get(point)}\n Your score: {sum_cards}')
    else:
        continue

while sum_cards_bot < 21:
    sum_cards_bot += points.pop(points.index(random.choice(points)))

print(f'Your score: {sum_cards}')
if sum_cards > 21:
    if sum_cards_bot > 21:
        print('Nobody won!')
    elif sum_cards_bot <= 21:
        print('Bot won!')
elif sum_cards == 21:
    if sum_cards_bot == 21:
        print('Everyone won')
    else:
        print('Player won')
elif sum_cards < 21:
    if 21 > sum_cards_bot > sum_cards:
        print('Bot won')
    else:
        print('Player won')

print(f'---- Scores---- \nYou: {sum_cards}\nBot: {sum_cards_bot}')
