def primes(n):
    output = [i for i in range(2, n+1)]
    num_to_remove = [i for i in range(2,(n//2)+1)]
    some_set = set()
    while num_to_remove:
        num = num_to_remove[0] * 2
        while num < n:
            some_set.add(num)
            num = num + num_to_remove[0]
        num_to_remove.pop(0)
    for item in some_set:
        output.remove(item)
    return output


def is_prime(m):
    if m in primes(m):
        return True
    else:
        return False


print(primes(70900))
