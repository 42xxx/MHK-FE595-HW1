import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2 * np.pi,0.01)
ysin = np.sin(x)
ycos = np.cos(x)

plt.plot(x, ysin,color='black', linewidth=1, alpha=0.6, label="sin(x)")
plt.plot(x, ycos,color='red', linewidth=1, alpha=0.6, label='cos(x)')
plt.show()