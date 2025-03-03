import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8, 6), dpi=200)
fig.suptitle('N log(N)(t)')
ax1 = plt.subplot()
plt.grid()
plt.ylabel("$N log(N)$")
plt.xlabel("$t$, c")
t = np.array([4 * 10**(-6), 4 * 10**(-5), 0.000368, 0.004547, 0.0515, 0.499334, 6.31149,31.7601 ,63.6609])
yyy = np.array([20, 200, 2000, 20000, 200000, 2000000, 20000000, 100000000, 200000000])
yyy = np.log(yyy) * yyy
z = np.polyfit(t, yyy, 1)
p = np.poly1d(z)

plt.plot(t, yyy, "b", marker='.', markersize=5, label='Г(t)', linestyle='None')
y = [p(min(t)), p(max(t))]
x = [min(t), max(t)]
plt.plot(x, y, '--b')
plt.show()
print(z[0])