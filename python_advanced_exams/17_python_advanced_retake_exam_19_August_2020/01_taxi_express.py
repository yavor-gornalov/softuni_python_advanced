from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))

total_time = 0
while customers and taxis:
    first_customer = customers.popleft()
    last_taxi = taxis.pop()
    if first_customer > last_taxi:
        customers.appendleft(first_customer)
        continue
    total_time += first_customer

if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations\n"
          f"Customers left: {', '.join([str(x) for x in customers])}")
