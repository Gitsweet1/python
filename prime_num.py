def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

num = int(input("Please enter a number ant I'll tell you if it's prime or not: "))
print(is_prime(num))