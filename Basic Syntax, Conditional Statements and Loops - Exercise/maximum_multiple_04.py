divisor_entered = int(input())
boundry_entered = int(input())
list = []

for number in range(1, boundry_entered +1):
    if number % divisor_entered == 0 and number > 0 and number <= boundry_entered:
        list.append(number)

print(max(list))