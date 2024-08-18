import json
from roman import add, subtract, multiply, divide, exponentiate

def salvar_calculos(calculo):
    """
    Salva os cálculos em um arquivo JSON.
    """
    with open('calculo.json', 'w') as file:
        json.dump(calculo, file, indent=4)


def carregar_calculo():
    """
    Carrega os cálculos salvos do arquivo JSON.
    """
    try:
        with open('calculo.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def main():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide, '**': exponentiate}
    calculo = carregar_calculo()

    while True:
        operation = input("Escolha uma operação (+, -, *, /, **) ou 'exit' para sair: ")
        if operation == 'exit':
            salvar_calculos(calculo)
            print("Cálculos salvos em 'calculo.json'.")
            break

        if operation not in operations:
            print("Operação inválida.")
            continue

        try:
            num1 = input("Digite o primeiro número romano: ").upper()
            num2 = input("Digite o segundo número romano: ").upper()
            resultado = operations[operation](num1, num2)
            print("resultadoado:", resultado)
            calculo.append({'num1': num1, 'num2': num2, 'operation': operation, 'resultado': resultado})
        except ValueError:
            print("Entrada inválida. Certifique-se de que os números romanos estão corretos.")
        except ZeroDivisionError:
            print("Divisão por zero não permitida.")

if __name__ == "__main__":
    main()
