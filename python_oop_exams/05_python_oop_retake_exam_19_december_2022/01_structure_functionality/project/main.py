from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Singer", "Drummer", "Guitarist"]
names = ["Lilly", "Vanilly", "Alex", "George"]

app = ConcertTrackerApp()

for i in range(4):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[0].learn_new_skill("sing low pitch notes"))
print(app.musicians[1].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("sing low pitch notes"))
print(app.musicians[2].learn_new_skill("play the drums with drum brushes"))
print(app.musicians[3].learn_new_skill("play jazz"))

print(app.create_band("JazzName"))
for i in range(4):
    print(app.add_musician_to_band(names[i], "JazzName"))

print(app.create_concert("Jazz", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
try:
    print(app.start_concert("Sofia", "JazzName"))
except Exception as ex:
    print(str(ex))
print(app.remove_musician_from_band("Vanilly", "JazzName"))
