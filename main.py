import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('Moores_Law.csv', delimiter=',', skip_header=1, usecols=(1, 2), dtype=float, filling_values=np.nan)
data = data[~np.isnan(data).any(axis=1)]

year = data[:, 1]
transistor_count = data[:, 0]

print('year:\t\t', year[:10])
print('trans. cnt:\t', transistor_count[:10])
plt.figure(figsize=(10, 6))
plt.scatter(year, transistor_count, color='blue', label='Data Points')
plt.yscale('log')
plt.xlabel('Year')
plt.ylabel('Transistor Count (log scale)')
plt.title("Moore's Law: Transistor Count Over Years")
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.legend()
plt.show()
