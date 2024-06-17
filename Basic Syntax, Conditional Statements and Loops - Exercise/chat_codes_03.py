messeges_qty = int(input())

for messeges in range(messeges_qty):
    code_entered = int(input())

    if code_entered == 88:
        print("Hello")
    elif code_entered == 86:
        print("How are you?")
    elif code_entered < 88 and (code_entered != 88 and code_entered != 86):
        print("GREAT!")
    else:
        print("Bye.")