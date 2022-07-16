# Solución razonamiento lógico

def xepelin_3_5_function(number):
    """ XepeLin
    Input: Any number
    Output: 'Xepe' if number is divisible by 3
            'Lin' if number is divisible by 5
            'Xepelin' if number is divisible by 3 and by 5
            'No es divisible por 3 ni por 5' in other case
    """
    try:
        string = ''
        if number % 3 == 0:
            string = 'Xepe'
        if number % 5 == 0:
            string = string + 'Lin'
        if string == '':
            string = 'No es divisible por 3 ni por 5'
        return string
    except TypeError:
        return 'Error: No se puede dividir si no es número'
    except Exception:
        return 'Error: Error no esperado'


if __name__ == "__main__":
    print("Probando función XepeLin\n")
    values_to_test = ['Hola', True, '5', 0, 3, 5, 10, 15]
    for value in values_to_test:
        input_text = f"Input: {type(value)}({value})"
        output_text = f"Output: {xepelin_3_5_function(value)}"
        print(f"    {input_text:<30} | {output_text}")
    print("\nFin test")