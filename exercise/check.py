word = "Baananas"
word = word.upper()
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
vowels = ['A', 'E', 'I', 'O', 'U']
# match="na"
letter_v = []
letter_c = []
score_0 = 0
score_1 = 0
player1 = input("player_1 for vowels")
player2 = input("player_1 for consonants")
result = {player1: score_0, player2: score_1}
print(player1)
for i in range(len(word)):
    if word[i] in consonants and word[i] not in letter_c:
        letter_c.append(word[i])
    elif word[i] in vowels and word[i] not in letter_v:
        letter_v.append(word[i])
print(letter_v, letter_c)

for index in range(2):
    if index == 0:
        letter_chosen = letter_v
    else:
        letter_chosen = letter_c
    sub_add=0
    for l in letter_chosen:
        initial = word.count(l)
        sub_add = 0 + initial
        for j in range(initial):
            pos = word.index(l)
            for i in range(pos + 1, len(word)):
                sub_add += 1
                print(word)
            word = word.replace(word[pos], '', 1)
        print(sub_add)
    if (index == 0):
        player1 = sub_add
    else:
        player2=sub_add

if (result[player1] > result[player2]):
    print(f'{player1} {result[player1]}')
elif (result[player2] > result[player1]):
    print(f'{player2} {result[player2]}')
else:
    print("Draw")

#         test_word=word
#         for test in range(word.count(l)):
#             match = ''
#             for k in range(test_word.index(l), len(test_word)):
#                 match += test_word[k]
#                 print(match)
