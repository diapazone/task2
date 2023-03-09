import random
from random import randint

loopers_words = []
your_word = input("ты: ")

while your_word != "пока":
    loopers_words.append(your_word)
    loopers_words += your_word.split()
    for i in range (0, randint(2, 8)):
        print(str(loopers_words[randint(0, len(loopers_words)-1)]), end = " ")
    print()
    your_word = input("ты: ")
    
