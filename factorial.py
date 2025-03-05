def factorial(n):
    if n <= 1:
        return False
    for i in range(n-1, 0, -1):
        n=n*i
    return n

num = int(input("Please enter number, I will output it's factorial: "))
print(factorial(num))