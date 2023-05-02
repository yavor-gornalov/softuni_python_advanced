# https://judge.softuni.org/Contests/Practice/Index/3744#0

from collections import deque

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

food_portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

defeated = False
conquered_peaks = []
for peak, difficulty in peaks.items():
    while True:
        if not food_portions or not stamina:
            defeated = True
            break

        current_portion = food_portions.pop()
        current_stamina = stamina.popleft()
        check_sum = current_portion + current_stamina

        if check_sum >= difficulty:
            conquered_peaks.append(peak)
            break
    if defeated:
        break

if len(peaks) == len(conquered_peaks):
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep='\n')
