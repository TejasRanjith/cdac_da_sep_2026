import numpy as np

np.random.seed(41)
roll_a_die = np.random.randint(1, 7,size = 30)
print(roll_a_die)

# roll 2 dice

die1 = np.random.randint(1, 7, size=30)
die2 = np.random.randint(1, 7, size=30)
print("Rolls of die 1:", die1)
print("Rolls of die 2:", die2)
total_rolls = die1 + die2
# for item in total_rolls:
    # print(item, end = " | ")
count = 0
values =[int(x) for x in np.random.uniform(low=-10.0, high=10.0, size=100)]
# need to display in the form of a line graph now
import matplotlib.pyplot as plt

plt.plot(values)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Graph of Random Values")
plt.show()