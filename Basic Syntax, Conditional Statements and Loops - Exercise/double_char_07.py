string_entered = input()

while string_entered != "End":

    if string_entered == "SoftUni":
        string_entered = input()
        continue
    for element in string_entered:
        new_string = element + element
        print(new_string,end="")
    print()

    string_entered = input()

