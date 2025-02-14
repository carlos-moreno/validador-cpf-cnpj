import string
from random import choice, randint

TWO = 2

CPF = {
    'first_digit': [10, 9, 8, 7, 6, 5, 4, 3, 2],
    'second_digit': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
}

CNPJ = {
    'first_digit': [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
    'second_digit': [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
}


def calculate_digit(digits, weights):
    """Calculates a check digit based on a list of digits and their
    corresponding weights.

    This function multiplies each digit by its corresponding weight, sums
    the results, and then calculates the check digit based on the remainder
    of the division by 11.
    If the remainder is less than a predefined value (TWO), it returns 0;
    otherwise, it returns the complement to 11.

    Parameters:
        digits (list of int)
            List of digits to be used in the calculation.
        weights (list of int)
            List of weights corresponding to the digits.

    Returns:
        int:
            The calculated check digit (0 or the complement to 11).
    """

    total_sum = sum([d * w for d, w in zip(digits, weights)])
    remainder = total_sum % 11
    return 0 if remainder < TWO else 11 - remainder


def generate_cpf():
    """Generates a random CPF number (Brazilian individual taxpayer registry
    number).

    This function generates the first nine digits of a CPF randomly,
    calculates the first and second check digits using the `calculate_digit`
    function, and then formats the CPF number according to the standard
    Brazilian format: NNN.NNN.NNN-NN.

    Returns:
        str:
            The generated CPF number in the format 'NNN.NNN.NNN-NN'.
    """

    base_digits = [randint(0, 9) for _ in range(9)]
    first_digit = calculate_digit(base_digits, CPF['first_digit'])
    second_digit = calculate_digit(
        base_digits + [first_digit], CPF['second_digit']
    )
    cpf = base_digits + [first_digit, second_digit]
    cpf = ''.join(map(str, cpf))
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


def generate_cnpj():
    """Generates a random CNPJ number (Brazilian company taxpayer registry
    number).

    This function generates the first twelve digits of a CNPJ randomly,
    calculates the first and second check digits using the `calculate_digit`
    function, and then formats the CNPJ number according to the standard
    Brazilian format: SS.SSS.SSS/SSSS-NN.

    Returns:
        str:
            The generated CNPJ number in the format 'SS.SSS.SSS/SSSS-NN'.
    """

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
