n = int(input())
evens = set()
odds = set()
for row_idx in range(1, n + 1):
    name = input()
    result = sum([ord(ch) for ch in name]) // row_idx
    if result % 2 == 0:
        evens.add(result)
    else:
        odds.add(result)

sum_odds = sum(odds)
sum_evens = sum(evens)

if sum_odds > sum_evens:
    print(', '.join([str(x) for x in odds.difference(evens)]))
elif sum_odds < sum_evens:
    print(', '.join([str(x) for x in odds.symmetric_difference(evens)]))
else:
    print(', '.join([str(x) for x in odds.union(evens)]))
