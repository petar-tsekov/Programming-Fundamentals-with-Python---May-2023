command_entered = input()

while command_entered != "Welcome!":
    if command_entered == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(command_entered) < 5:
        print(f"{command_entered} goes to Gryffindor.")
    elif len(command_entered) == 5:
        print(f"{command_entered} goes to Slytherin.")
    elif len(command_entered) == 6:
        print(f"{command_entered} goes to Ravenclaw.")
    elif len(command_entered) > 6:
        print(f"{command_entered} goes to Hufflepuff.")

    command_entered = input()

else:
    print(f"Welcome to Hogwarts.")