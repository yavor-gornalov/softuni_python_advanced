text = input()
unique_symbols_count = {x: text.count(x) for x in text}
for symbol, occurrences in sorted(unique_symbols_count.items()):
    print(f'{symbol}: {occurrences} time/s')
