__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter10_3.py was created on May 23 2022 @ 10:28 AM
# Project: FluentPython
#


from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional,Callable,NamedTuple


class Customer(NamedTuple):
    name: str
    fidelity: int

class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self):
        return self.price * self.quantity

@dataclass(frozen=True)
class Order:  # the context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None # callable takes an Order argument, and returns a decimal

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))
    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order Total: {self.total():.2f} due: {self.due():.2f} {self.promotion.__name__}'

def fidelity_promo(order: Order) -> Decimal:
    """ 5% discount for customer with 1,000 fidelity points"""
    name: str = 'Fidelity'
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('.05')
    else:
        return Decimal(0)

def bulk_item_promo(order: Order) -> Decimal:
    """10% discount for each item with 20 or more units"""
    discount = Decimal(0)

    for item in order.cart:
        if item.quantity >= 20:
            discount = item.total() * Decimal('0.1')
    return discount

def large_order_promo(order: Order):
    """7% discount for order with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)

promos = [fidelity_promo, bulk_item_promo,large_order_promo]

def best_promo(order: Order) -> Decimal:
    """Compute best discount possible"""
    return(max(promo(order) for promo in promos))

if __name__ == '__main__':
    ann = Customer('Ann Smith', 1100)
    joe = Customer('John Doe', 0)

    cart = (
        LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)),
    )

    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    banana_cart = (
        LineItem('banana', 30, Decimal('.5')),
        LineItem('apple', 10, Decimal(1.5)),
    )

    print(Order(joe, banana_cart, bulk_item_promo))
    long_cart = tuple(LineItem(str(sku), 1, Decimal(1)) for sku in range(10))
    print(Order(joe, long_cart, large_order_promo))

    print(Order(joe, long_cart, best_promo))
    print(Order(joe,banana_cart,best_promo))
    print(Order(ann, cart, best_promo))