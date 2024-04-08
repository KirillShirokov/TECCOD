"""Написать функцию, которая принимает на вход два целых числа (минимум и
 максимум) и возвращает список всех простых чисел в заданном диапазоне."""


def get_prime_numbers(min_value, max_value):
    primes = []
    for possible_prime in range(min_value, max_value + 1):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)
    return primes
