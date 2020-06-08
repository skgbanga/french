#!/usr/bin/python3

import time
from random import choice
from collections import deque
from functools import wraps

from data import verbs, pronouns, dictionary, vowels


def toss():
    options = [0] * 3 + [1] * 7
    return choice(options)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        taken = time.time() - start
        print('Time taken: {:0.2f}'.format(taken))

        return taken

    return wrapper


@timer
def question(answer):
    for i in range(3):
        s = input('< ')
        if s == answer:
            print('correct. ', end='')
            break

        if i != 2:
            print("wrong! Try again...")
    else:
        print("the answer is {}.".format(answer), end='')


def liason(pronoun, conjugation):
    exceptions = ['elle', 'tu']
    if pronoun in exceptions:
        return

    if pronoun[-1] in vowels and conjugation[0] in vowels:
        return pronoun[:-1] + "'" + conjugation

def answer(pronoun, verb):
    conjugation = dictionary[verb[0]][pronoun[0]]

    ans = liason(pronoun[0], conjugation)
    if ans:
        return ans

    return pronoun[0] + ' ' + conjugation


def main():
    lasts = deque(maxlen=5)
    chances = 10

    total = 0
    attempts = 0
    while attempts < chances:
        pronoun = choice(pronouns)
        verb = choice(verbs)
        try:
            right = answer(pronoun, verb)
        except KeyError:
            continue

        if right in lasts:
            continue
        lasts.append(right)

        print('>', pronoun[toss()], ',', verb[toss()])
        total += question(right)
        attempts += 1

    print('Average time taken {:.2f} secs'.format(total / chances))


## tests
def test_answer():
    assert answer(('je', 'i'), ('avoir', 'to have')) == "j'ai"
    assert answer(('elle', 'she'), ('etre', 'to be')) == "elle est"


if __name__ == '__main__':
    main()
