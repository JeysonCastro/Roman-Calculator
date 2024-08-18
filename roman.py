def para_romano(romano):
    """
    Converte um número romano para inteiro.
    """
    numeros_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    valor_anterior = 0

    for n in reversed(romano):
        valor = numeros_romanos[n]
        if valor < valor_anterior:
            total -= valor
        else:
            total += valor
        valor_anterior = valor

    return total


def do_romano(number):
    """
    Converte um número inteiro para romano.
    """
    numeros_romanos2 = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    resultado = ''

    for valor, numeral in sorted(numeros_romanos2.items(), reverse=True):
        while number >= valor:
            resultado += numeral
            number -= valor

    return resultado


def add(a, b):
    """
    Soma dois números romanos.
    """
    return do_romano(para_romano(a) + para_romano(b))


def subtract(a, b):
    """
    Subtrai dois números romanos.
    """
    return do_romano(para_romano(a) - para_romano(b))


def multiply(a, b):
    """
    Multiplica dois números romanos.
    """
    return do_romano(para_romano(a) * para_romano(b))


def divide(a, b):
    """
    Divide dois números romanos, retornando quociente e resto.
    """
    quotient = para_romano(a) // para_romano(b)
    remainder = para_romano(a) % para_romano(b)
    return do_romano(quotient), do_romano(remainder)


def exponentiate(a, b):
    """
    Calcula a potência de um número romano.
    """
    return do_romano(para_romano(a) ** para_romano(b))
