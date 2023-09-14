# https://judge.softuni.org/Contests/Practice/Index/3596#2

def forecast(*args):
    weather_locations = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for arg in args:
        location, weather = arg
        if weather in weather_locations:
            weather_locations[weather].append(location)

    result = ""
    for weather, locations in weather_locations.items():
        for location in sorted(locations):
            result += f"{location} - {weather}\n"

    return result


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("Plovdiv", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
