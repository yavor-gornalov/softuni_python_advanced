def flights(*args):
    flight_dict = {}
    for idx in range(1, len(args), 2):
        destination = args[idx - 1]
        if destination == "Finish":
            break
        if destination not in flight_dict:
            flight_dict[destination] = 0
        flight_dict[destination] += args[idx]
    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
