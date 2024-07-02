lines_qty = int(input())

total_sum = 0

for line in range(lines_qty):
    character_entered = input()
    total_sum += ord(character_entered)

print(f"The sum equals: {total_sum}")