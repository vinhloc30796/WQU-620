# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:59:40 2021

@author: User
"""


from itertools import combinations, chain, product


def sigma_algebra_set(input_set):
    size = len(input_set)
    combs = (combinations(input_set, k) for k in range(1, size + 1))
    empty_powerset = ((),)
    return chain(empty_powerset, *combs)


def cartesian_product(Up, Down, N):
    """
    return the list of all the computed tuple
    using the product() method
    """
    return list(product([Up, Down], repeat=N))


def tuple_product(tuple_path):
    res = 1
    for item in tuple_path:
        res *= item
    return res


def tree_outcome(S0, tree_path):
    tree_outcome = []
    for item in tree_path:
        tree_outcome.append(S0 * tuple_product(item))
    return tree_outcome


def fil_sigma_set(tree_outcome, fil_lev):
    no_outcome = len(tree_outcome)
    no_block_item = int(no_outcome / 2 ** fil_lev)
    list_fil_set = []

    list_fil_set = lambda outcome_list, n=no_block_item: [
        outcome_list[i : i + n] for i in range(0, no_outcome, n)
    ]
    return list_fil_set(tree_outcome)


def filtration_set(S0, u, d, N, n):
    tree_path = cartesian_product(u, d, N)
    tree = tree_outcome(S0, tree_path)
    sigma_set = fil_sigma_set(tree, n)
    f_n = list(sigma_algebra_set(sigma_set))
    return f_n
