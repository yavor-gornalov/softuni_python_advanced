from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bowls_of_ramen and customers:
    current_bowl = bowls_of_ramen.pop()
    current_customer = customers.popleft()

    if current_bowl > current_customer:
        current_bowl -= current_customer
        bowls_of_ramen.append(current_bowl)
    elif current_bowl < current_customer:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}") if bowls_of_ramen else None
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}") if customers else None
