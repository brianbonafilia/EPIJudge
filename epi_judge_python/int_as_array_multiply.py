from test_framework import generic_test


def multiply(num1, num2):
    # get the sign of result
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    # now remove sign on the MSD of each num1 and num2
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    max_result_len = len(num1) + len(num2)
    result = [0] * max_result_len
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    # remove leading zeros, if all or zeros and the result is
    # None use [0] instead
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


def multiply_original_solution(num1, num2):
    # TODO - you fill in here.
    def add(A, B):
        if len(A) < len(B):
            A, B = B, A
        carry = 0
        for i, value in enumerate(B):
            A[i] = A[i] + value + carry
            carry, A[i] = A[i] // 10, A[i] % 10
        if carry:
            i = len(B)
            while i < len(A) and carry:
                value = A[i] + carry
                carry, A[i] = value // 10, value % 10
                i += 1
            if carry:
                A.append(carry)
        return A

    negative = False
    if num1[0] < 0:
        negative = True
        num1[0] = -1 * num1[0]
    if num2[0] < 0:
        negative = not negative
        num2[0] = -1 * num2[0]
    num1.reverse(), num2.reverse()
    result = []
    for i, a_value in enumerate(num1):
        add_to_result = [0] * i
        carry = 0
        for b_value in num2:
            cur_val = a_value * b_value + carry
            add_to_result.append(cur_val % 10)
            carry = cur_val // 10
        if carry:
            add_to_result.append(carry)
        result = add(result, add_to_result)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    result.reverse()
    if negative:
        result[0] = -1 * result[0]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
