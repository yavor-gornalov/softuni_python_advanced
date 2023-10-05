from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

total_pizzas_prepared = 0
while orders and employees:
    current_order = orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue
    employee_capacity = employees.pop()

    if current_order > employee_capacity:
        current_order -= employee_capacity
        orders.appendleft(current_order)
        total_pizzas_prepared += employee_capacity
    else:
        total_pizzas_prepared += current_order

if not orders:
    print(f"""All orders are successfully completed!
Total pizzas made: {total_pizzas_prepared}
Employees: {', '.join([str(e) for e in employees])}
""")
elif not employees:
    print(f"""Not all orders are completed.
Orders left: {', '.join([str(o) for o in orders])}""")
