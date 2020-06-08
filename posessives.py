from random import choice
from data import male_nouns, female_nouns, possessives


def toss():
    return choice([0, 1])


def main():
    while True:
        possessive = choice(possessives)

        selection = toss()
        if selection == 0:
            noun = choice(male_nouns)
        else:
            assert selection == 1
            noun = choice(female_nouns)


        plural = toss()
        if plural == 1:
            show_noun = noun[1] + 's'
            answer_noun = noun[0] + 's'
            answer_possessive = possessive[-1]
        else:
            assert plural == 0
            show_noun = noun[1]
            answer_noun = noun[0]
            answer_possessive = possessive[selection + 1]

        print('>', possessive[0], ',', show_noun)
        s = input('< ')
        answer = answer_possessive + ' ' + answer_noun

        if s == answer:
            print("Correct")
        else:
            print("Incorrect. Correct is {}".format(answer))


if __name__ == '__main__':
    main()
