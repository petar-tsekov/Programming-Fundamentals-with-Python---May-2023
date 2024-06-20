string_qty = int(input())

for string in range(string_qty):
    string_entered = input()

    if "," in string_entered or "." in string_entered or "_" in string_entered:
        print(f"{string_entered} is not pure!")
    else:
        print(f"{string_entered} is pure.")