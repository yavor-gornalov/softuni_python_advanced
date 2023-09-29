def negative_vs_positive(*args):
    positive_sum = 0
    negative_sum = 0
    for num in args:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num
    result = [negative_sum, positive_sum]
    if negative_sum + positive_sum < 0:
        result.append("The negatives are stronger than the positives")
    else:
        result.append("The positives are stronger than the negatives")
    return "\n".join(str(x) for x in result)


nums = [int(x) for x in input().split()]
print(negative_vs_positive(*nums))
