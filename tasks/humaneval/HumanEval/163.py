
def generate_integers(a, b):
    start = min(a, b)
    end = max(a, b)
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            result.append(num)
    return result