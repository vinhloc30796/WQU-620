# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:42:18 2021

@author: juanvarl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import csc_matrix
from scipy.stats import bernoulli
from scipy.optimize import fsolve
from scipy.stats import norm


def Binomial_Tree(N, S0, group_n):  # you can add variables to the function

    #  Assume a volatility and calculate the size of an up move, down move, and probability
    u = 1.1 + group_n / 100
    d = 1 / u

    #  Create some empty matrices to hold our stock and call prices.
    stock_prices = np.zeros((N, N))

    #  Put our initial price in the matrix
    stock_prices[0, 0] = S0

    #  Fill out the remaining values
    for i in range(1, N):
        M = i + 1
        stock_prices[i, 0] = d * stock_prices[i - 1, 0]
        for j in range(1, M):
            stock_prices[i, j] = u * stock_prices[i - 1, j - 1]

    return stock_prices


# 1)

##1.a) Calculate and show the new Binomial tree for N=6.

# Variables
N = 6  # number of layers
S0 = 1  # Initial Price
group_n = 2  # Group Number 2

stock_prices = Binomial_Tree(N, S0, group_n)

##1.b) What are the terminal values of each path? Define the appropriate filtrations for each of these values.
print(stock_prices[N - 1, :])
# We need to define the appropiate filtration

# 2) Finally, recalculate the tree for N=4,000.

##2.a) Plot the terminal prices produced by the model (You may use a histogram for this).

# Variables
S0 = 100  # Initial Price
N = 101  # number of layers
group_n = 2  # Group Number 2

stock_prices = Binomial_Tree(N, S0, group_n)
df_P_N = pd.DataFrame(stock_prices)
P_N = df_P_N.iloc[-1:].T

P_N.describe()
plt.hist(P_N, 25)


##2.b)

##2.c)
