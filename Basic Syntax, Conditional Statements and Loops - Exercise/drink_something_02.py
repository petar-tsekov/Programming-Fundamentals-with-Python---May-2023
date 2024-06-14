person_age = int(input())

if person_age <= 14:
    print(f"drink toddy")
elif 14 < person_age <= 18:
    print(f"drink coke")
elif 18 < person_age <= 21:
    print(f"drink beer")
else:
    print(f"drink whisky")