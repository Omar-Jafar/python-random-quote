import random


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    for i in range(int(input())):
        rnd = random.randint(0, last)
        print(quotes[rnd])


if __name__ == "__main__":
    primary()
