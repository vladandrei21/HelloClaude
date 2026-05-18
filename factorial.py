def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(factorial(n))