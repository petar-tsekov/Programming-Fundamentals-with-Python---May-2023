orders_qty = int(input())
total_sum = 0
current_order = 0

for orders in range(orders_qty):
    capsule_price = float(input())
    days_qty = int(input())
    capsule_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100.00:
        continue
    if days_qty < 1 or days_qty > 31:
        continue
    if capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    current_order = capsule_per_day * days_qty * capsule_price
    total_sum += current_order
    print(f"The price for the coffee is: ${current_order:.2f}")

print(f"Total: ${total_sum:.2f}")