def stock_availability(items, command, *args):
    if command == "delivery":
        for item in args:
            items.append(item)
    elif command == "sell":
        if not args:
            if items:
                items.pop(0)
        elif isinstance(args[0], int):
            for _ in range(args[0]):
                if not items:
                    break
                items.pop(0)
        else:
            for item in args:
                while item in items:
                    items.pop(items.index(item))

    return items


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
