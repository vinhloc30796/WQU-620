# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:42:18 2021

@author: juanvarl
@author: Kanittha-Set
@author: vinhloc30796
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.stats import binom

def binomialTree(N, S0, group_n):
    """
    Calculate the option price binomial tree
    in the form of a np.array with shape NxN
    """
    #  Assume a volatility and calculate the size of an up move, down move, and probability
    u = 1.1 + group_n / 100
    d = 1 / u

    #  Create some empty matrices to hold our stock and call prices.
    stock_prices = np.zeros((N+1, N+1))
    return_stock_prices = np.zeros((N+1, N+1))

    #  Put our initial price in the matrix
    stock_prices[0, 0] = S0

    #  Fill out the remaining values
    for i in range(1, N+1):
        M = i + 1
        stock_prices[i, 0] = d * stock_prices[i - 1, 0]
        return_stock_prices[i, 0] = np.log(
            stock_prices[i, 0]/S0
        )
        for j in range(1, M):
            stock_prices[i, j] = u * stock_prices[i - 1, j - 1]
            return_stock_prices[i, j] = np.log(
                stock_prices[i, j]/S0
            )

    return {
        "stock_prices": stock_prices,
        "return_stock_prices": return_stock_prices
    }

def binomialFreq(N, relative=True):
    """
    Calculate the frequency 
    for each terminal value of each path,
    where the frequency is the binomial coefficient (nCr).
    """
    freq_arr = np.array([])
    if relative:
        p = 0.5
        binom_dist = binom(n=N, p=p)
        freq_arr = np.array(
            [binom.pmf(k=i,n=N,p=p) for i in range(N+1)]
        )
    else:
        freq_arr = np.array(
            [comb(N, i, exact=True) for i in range(N+1)]
        )
    return freq_arr
