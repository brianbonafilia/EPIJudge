from test_framework import generic_test

def buy_and_sell_stock_once(prices):
    cur_min, largest_sell = prices[0], 0
    for price in prices:
        cur_min = min(cur_min, price)
        largest_sell = max(largest_sell, price - cur_min)
    return largest_sell


def buy_and_sell_stock_once_original_solution(prices):
    # TODO - you fill in here.
    cur_min = prices[0]
    largest_sell = 0
    for price in prices:
        if price < cur_min:
            cur_min = price
        if price - cur_min > largest_sell:
            largest_sell = price - cur_min
    return largest_sell


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
