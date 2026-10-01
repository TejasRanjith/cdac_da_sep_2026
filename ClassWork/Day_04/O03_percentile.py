from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
vals = np.random.normal(0,0.5,10000)
plt.hist(vals,bins=50)
plt.show()

percentiles = np.percentile(vals, [50, 90, 20])
print("50th percentile:", percentiles[0])
print("90th percentile:", percentiles[1])
print("20th percentile:", percentiles[2])