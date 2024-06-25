command_entered = input()
count_coffee = 0
while command_entered != "END":
    if command_entered.isupper():
        if command_entered == "CODING":
            count_coffee += 2
        elif command_entered == "DOG" or command_entered == "CAT":
            count_coffee += 2
        elif command_entered == "MOVIE":
            count_coffee += 2
    elif command_entered.islower():
        if command_entered == "coding":
            count_coffee += 1
        elif command_entered == "dog" or command_entered == "cat":
            count_coffee += 1
        elif command_entered == "movie":
            count_coffee += 1

    command_entered = input()

if count_coffee > 5:
    print( "You need extra sleep")
else:
    print(count_coffee)


