
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def find_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers
print(is_prime(100000000))
