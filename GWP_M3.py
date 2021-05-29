# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:42:18 2021

@author: juanvarl
@author: Kanittha-Set
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import comb

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

    return stock_prices

def binomialFreq(N):
    """
    Define the frequency as the binomial coefficient (nCr) 
    for each terminal value of each path
    """
    freq_arr = []
    for i in range(N+1):
            freq_arr.append(comb(N, i, exact=True))
    return freq_arr
