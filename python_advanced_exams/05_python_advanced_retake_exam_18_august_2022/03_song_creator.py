# https://judge.softuni.org/Contests/Practice/Index/3534#2

def add_songs(*kwargs):
    song_lyrics = {}

    for title, lyrics in kwargs:
        if title not in song_lyrics:
            song_lyrics[title] = []
        song_lyrics[title].extend(lyrics)

    result = ""
    for title, lyrics in song_lyrics.items():
        result += f"- {title}\n"
        for lyric in lyrics:
            result += f"{lyric}\n"
    return result


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
