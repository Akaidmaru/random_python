def reverse_seq(n):
    final = [i for i in range(1, n+1)]
    return final[::-1]

def reverse_seq(n):
    return list(range(n, 0,-1))

print(reverse_seq(5))