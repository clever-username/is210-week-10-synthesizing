#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program takes two dictionaries and combines them into one."""

from data import *

def sum_orders(customers, orders):
    """This function accepts two dictionaries and returns the combined dict.

    Args:
        customers(dict): TEXT.
        orders(dict): TEXT.

    Returns:
        combo_orders(dict): A new dictionary combined by customer ID.

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
            {2: {'name': 'Person One',
                 'email': 'email@one.com',
                 'orders': 2,
                 'total': 20}
             3: {'name': 'Person Two',
                 'email': 'email@two.com',
                 'orders': 1,
                 'total': 15}}
    """

    c_orders = {}
    orders = 0
    for item in CUSTOMERS:
        c_id = CUSTOMERS[item]
        if c_id == ORDERS[item]['customer_id']:
            total = CUSTOMERS[item]['total'] + ORDERS[item]['total']
            name = CUSTOMERS[item]['name']
            email = CUSTOMERS[item]['email']
            orders += 1
        else:
            tmp_orders = dict(email=email, name=name, total=total,
                              orders=orders)
            c_orders.update({customerid: temp_orders})
