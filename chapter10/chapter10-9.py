__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter10-9.py was created on May 23 2022 @ 4:05 PM
# Project: FluentPython
#
from decimal import Decimal
from typing import Callable

from chapter10.chapter10_3 import Order, LineItem, Customer

Promotion = Callable[[Order], Decimal]

promos: list[Promotion] = []

def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo

def best_promo(order: Order) -> Decimal:
    """Compute best discount possible"""
    return(max(promo(order) for promo in promos))

@promotion
def fidelity(order: Order) -> Decimal:
    """ 5% discount for customer with 1,000 fidelity points"""
    name: str = 'Fidelity'
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('.05')

    return Decimal(0)
@promotion
def bulk_item(order: Order) -> Decimal:
    """10% discount for each item with 20 or more units"""
    discount = Decimal(0)

    for item in order.cart:
        if item.quantity >= 20:
            discount = item.total() * Decimal('0.1')
    return discount

@promotion
def large_order(order: Order):
    """7% discount for order with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)

if __name__ == '__main__':
    ann = Customer('Ann Smith', 1100)
    joe = Customer('John Doe', 0)

    cart = (
        LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)),
    )

    print(Order(joe, cart, fidelity))
    print(Order(ann, cart, fidelity))

    banana_cart = (
        LineItem('banana', 30, Decimal('.5')),
        LineItem('apple', 10, Decimal(1.5)),
    )

    print(Order(joe, banana_cart, bulk_item))
    long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))
    print(Order(joe, long_cart, large_order))

    print(Order(joe, long_cart, best_promo))
    print(Order(joe,banana_cart,best_promo))
    print(Order(ann, cart, best_promo))