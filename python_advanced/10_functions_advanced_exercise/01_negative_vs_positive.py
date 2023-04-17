# https://judge.softuni.org/Contests/Practice/Index/1839#0

def total_sum(*args):
    result = ""
    sum_negatives = sum([n for n in args if n < 0])
    sum_positives = sum([n for n in args if n >= 0])
    result += f"{sum_negatives}\n{sum_positives}\n"
    if abs(sum_negatives) > sum_positives:
        result += "The negatives are stronger than the positives"
    if sum_positives > abs(sum_negatives):
        result += "The positives are stronger than the negatives"
    return result


nums = [int(x) for x in input().split()]
print(total_sum(*nums))
