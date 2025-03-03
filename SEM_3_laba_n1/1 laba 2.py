import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6), dpi=200)
fig.suptitle('N log(N)(t)')
ax1 = plt.subplot()
plt.grid()
plt.ylabel("$N log(N)$")
plt.xlabel("$t$, c")
t = np.array([5 * 10**(-6), 1.8 * 10**(-5), 0.000188, 0.001768, 0.0202, 0.2432, 2.445, 12.4974 ,17.4636])
yyy = np.array([10, 100, 1000, 10000, 100000, 1000000, 10000000, 50000000, 70000000])
yyy = np.log(yyy) * yyy
z = np.polyfit(t, yyy, 1)
p = np.poly1d(z)

plt.plot(t, yyy, "b", marker='.', markersize=5, label='Г(t)', linestyle='None')
y = [p(min(t)), p(max(t))]
x = [min(t), max(t)]
plt.plot(x, y, '--b')
plt.show()
print(z[0])