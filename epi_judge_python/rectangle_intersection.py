import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    # TODO - you fill in here.
    r1_l, r1_r = R1.x, R1.x + R1.width
    r2_l, r2_r = R2.x, R2.x + R2.width
    max_l, min_r = max(r1_l, r2_l), min(r1_r, r2_r)
    if max_l <= min_r:
        r1_d, r1_u = R1.y, R1.y + R1.height
        r2_d, r2_u = R2.y, R2.y + R2.height
        max_d, min_u = max(r1_d, r2_d), min(r1_u, r2_u)
        if max_d <= min_u:
            return Rectangle(max_l, max_d, min_r - max_l, min_u - max_d)
    return Rectangle(0, 0, -1, -1)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
