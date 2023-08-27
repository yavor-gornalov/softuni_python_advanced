def reverse_text(text):
    idx = len(text) - 1
    end_idx = 0
    while idx >= end_idx:
        yield text[idx]
        idx -= 1


for char in reverse_text("step"):
    print(char, end='')
