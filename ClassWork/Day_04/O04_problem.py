import numpy as np

prices = [2,3,4,5,6,7,8]

# need to find IQR (Interquartile Range)
# import statistics
# q1, q2, q3 = statistics.quantiles(prices, n=4)
# iqr = q3 - q1
# print(iqr)
prices = sorted(prices)
median_1st = np.median(prices)
