# Solution to question number 2

def product_of_array(values):
    """
    Input: Array of numbers
    Output: Product of elements of the array
    """
    try:
        product = 1
        for i in values:
            product = product * i
        return product
    except TypeError:
        return 'Error: No se puede multiplicar si no es número'
    except Exception:
        return 'Error: Error no esperado'

def prod_without_i_element(values):
    """
    Input: Array of numbers
    Output: Products of elements of all possible arrays when one element is removed from input array.
    """
    try:
        all_products = []
        product_all_numbers = product_of_array(values)
        for value_to_avoid in values:
            all_products.append(product_all_numbers / value_to_avoid)
        return all_products
    except TypeError:
        return 'Error: No se puede operar si no es array de números'
    except Exception:
        return 'Error: Error no esperado'

if __name__ == "__main__":
    print("Probando función i-esimo producto\n")
    values_to_test = [
      [1, 2, 3, 4],
      ['Hola', True, '5', 0, 3, 5, 10, 15],
      [1, 2, 3, 4, 5],
      [2, 2, 5],
      False,
    ]
    for this_array in values_to_test:
        print(f"  Input : {this_array}")
        print(f"  Output: {prod_without_i_element(this_array)}\n")
    print("Fin test")