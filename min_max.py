# 1
def min_max(lst):
    min_num = min(lst)
    max_num = max(lst)
    return [min_num, max_num]

# Refactor
def min_max(lst):
    return [min(lst), max(lst)]

print(min_max([1,2,3,4,5]))
