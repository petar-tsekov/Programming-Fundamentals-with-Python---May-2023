lines = int(input())

for first in range(0,lines):
    for second in range(0,lines):

        for third in range(0,lines):
                new_word = chr(97 + first) + chr(97 + second) + chr(97 + third)
                print(new_word)

    