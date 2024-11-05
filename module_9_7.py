def prime_decorator(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        if is_prime(number):
            print("Простое")
        else:
            print("Составное")
        return number
    return wrapper

def is_prime(n):
    number = n
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

@prime_decorator
def sum_three(a,b,c):
    return a + b + c

if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(3, 4, 7)
    print(result)
    result = sum_three(4, 5, 8)
    print(result)
    result = sum_three(5, 6, 9)
    print(result)

