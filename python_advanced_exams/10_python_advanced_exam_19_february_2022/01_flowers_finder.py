from collections import deque

words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

vowels = deque(x for x in input().split())
consonants = deque(x for x in input().split())

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    word_found = False
    for x in vowel, consonant:
        for current_word in words:
            if x in current_word:
                words[current_word] = words[current_word].replace(x, "")
            if not words[current_word]:
                print(f"Word found: {current_word}")
                word_found = True
                break
        if word_found:
            break
    if word_found:
        break
else:
    print("Cannot find any word!")

print(f"Vowels left: {' '.join(vowels)}") if vowels else None
print(f"Consonants left: {' '.join(consonants)}") if consonants else None
