def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        is_prime = True
        for i in range(2, (number // 2) + 1):   # проверка на принадлежность к простым
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print('Простое')
        else:
            print('Составное')
        return number
    return wrapper


@is_prime
def sum_three(a,b,c):
    """Функция, которая складывает 3 числа """
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

