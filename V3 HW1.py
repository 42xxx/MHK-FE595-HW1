# Version 3
# make some change according to teammate's advice
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.01)
ysin = np.sin(x)
ycos = np.cos(x)
ytan = np.tan(x)

plt.plot(x, ysin, color='black', linewidth=1, alpha=0.6, label="sin(x)")
plt.plot(x, ycos, color='red', linewidth=1, alpha=0.6, label='cos(x)')
# ------ changed by Fangchi Wu ---------##
plt.plot(x, ytan, color='blue', linewidth=1, alpha=0.6, label='tan(x)')
plt.ylim(-1, 1)
# ----------------------------------------- ##


if __name__ == "__main__":
    plt.show()
