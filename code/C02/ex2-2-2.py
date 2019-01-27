#!/usr/bin/env python3.7
def shipping_cost(n):
    return 3 + ((n - 1) * 0.75 if n > 1 else 0)

def total_cost(cover_price, discount, n):
    return cover_price * discount * n + shipping_cost(n)

if __name__ == '__main__':
    print(total_cost(24.95, 0.4, 60))
