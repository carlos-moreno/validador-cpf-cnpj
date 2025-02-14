import string
from random import choice, randint

TWO = 2
DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 17,
    'B': 18,
    'C': 19,
    'D': 20,
    'E': 21,
    'F': 22,
    'G': 23,
    'H': 24,
    'I': 25,
    'J': 26,
    'K': 27,
    'L': 28,
    'M': 29,
    'N': 30,
    'O': 31,
    'P': 32,
    'Q': 33,
    'R': 34,
    'S': 35,
    'T': 36,
    'U': 37,
    'V': 38,
    'X': 39,
    'W': 40,
    'Y': 41,
    'Z': 42,
}

CPF = {
    'first_digit': [10, 9, 8, 7, 6, 5, 4, 3, 2],
    'second_digit': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
}

CNPJ = {
    'first_digit': [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    'second_digit': [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
}


def calculate_digit(digits, weights):
    total_sum = sum([d * w for d, w in zip(digits, weights)])
    remainder = total_sum % 11
    return 0 if remainder < TWO else 11 - remainder


def generate_cpf():
    base_digits = [randint(0, 9) for _ in range(9)]
    first_digit = calculate_digit(base_digits, CPF['first_digit'])
    second_digit = calculate_digit(
        base_digits + [first_digit], CPF['second_digit']
    )
    cpf = base_digits + [first_digit, second_digit]
    cpf = ''.join(map(str, cpf))
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def generate_cnpj():
    base_digits = [
        choice(string.digits + string.ascii_uppercase) for _ in range(12)
    ]
    base_digits_int = [ord(d) - 48 for d in base_digits]
    first_digit = calculate_digit(base_digits_int, CNPJ['first_digit'])
    second_digit = calculate_digit(
        base_digits_int + [first_digit], CNPJ['second_digit']
    )
    cnpj = base_digits + [str(first_digit), str(second_digit)]
    cnpj = ''.join(cnpj)
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
