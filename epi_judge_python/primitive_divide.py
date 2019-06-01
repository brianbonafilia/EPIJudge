from test_framework import generic_test

MAX_INT = 32

def divide(x, y):
    """  example x = 64, y = 3
          x = 0b1000000 y = 0b11
          when power goes from 32 -> 16
          x >= y_power x = 64, y = 48
          subtract 48 from 64 = 16 = x and result = 1 << 4 = 32
          when power goes to 2,  y_power = 12 which is less than 16
          result + (1 << 2) = 20
          x = 4 and y = 3
          result + 1 = 21   answer is 21.

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
