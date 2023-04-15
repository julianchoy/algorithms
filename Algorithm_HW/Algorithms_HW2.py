import math


# 1 Split in Half

def split_in_half(user_submit):
    str_length = len(user_submit) / 2
    first_part = user_submit[:math.ceil(str_length)]
    second_part = user_submit[math.ceil(str_length):]
    return second_part + first_part


user_word = input('submit a word: ')
print(split_in_half(user_word))


# 2 Unique Characters in String

def verify_unique(user_submit2):
    char_set = set()
    for char in user_submit2:
        if char in char_set:
            return 'dupe'
        char_set.add(char)
    return 'unique'


user_word2 = input('submit a word: ')
print(verify_unique(user_word2))
