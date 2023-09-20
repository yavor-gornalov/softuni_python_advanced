n = int(input())

length_longest_intersection = 0
longest_intersection_numbers = []
for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_set = {x for x in range(first_start, first_end + 1)}
    second_set = {x for x in range(second_start, second_end + 1)}
    intersection_numbers = first_set & second_set

    if len(intersection_numbers) > length_longest_intersection:
        longest_intersection_numbers = intersection_numbers
        length_longest_intersection = len(intersection_numbers)

print(f"Longest intersection is [{', '.join(str(x) for x in sorted(longest_intersection_numbers))}] "
      f"with length {length_longest_intersection}")
