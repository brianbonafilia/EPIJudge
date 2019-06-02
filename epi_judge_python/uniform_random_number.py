import functools
import math
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random(lower_bound, upper_bound):
    # TODO - you fill in here.
    def make_random_binary(num_bits):
        result = 0
        mask = 1
        for i in range(0, num_bits):
            if zero_one_random():
                result |= mask
            mask <<= 1
        return result
    value = upper_bound - lower_bound
    num_bits = math.ceil(math.log2(value + 1))
    result = make_random_binary(num_bits)
    while result > value:
        result = make_random_binary(num_bits)
    return result + lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(lambda : [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound
             for a in result], upper_bound - lower_bound + 1, 0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("uniform_random_number.py",
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
