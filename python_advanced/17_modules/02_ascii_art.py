from pyfiglet import figlet_format


def figlet_message(message, font="big"):
    print(figlet_format(message, font=font))


text = input()
figlet_message(text)
