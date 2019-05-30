from test_framework import generic_test

MAX_INT = 32

def divide(x, y):
    """  example x = 64, y = 3
          x = 1000000 y = 11
          when power goes from 32 -> 5
          x >= y_power x = 64, y = 48
    """      
    result, power = 0, MAX_INT
    while x >= y:
        y_power = y << power 
        if x >= y_power:
            result += 1 << power
            x -= y_power
        power -= 1           
    return result


if __name__ == '__main__':
    divide(23, 5)
    #exit(
     #   generic_test.generic_test_main("primitive_divide.py",
      #                                 "primitive_divide.tsv", divide))
