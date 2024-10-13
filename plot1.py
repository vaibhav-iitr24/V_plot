import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('file.tsv', sep='\t', names=['x','y','frequency'])


plt.figure(figsize=(10, 6))


plt.gcf().set_facecolor('white')
scatter=plt.scatter(data['x'], data['y'], c=data['frequency'], s=50, alpha=0.6, cmap='inferno')
plt.colorbar(scatter, label='frequency')
plt.title('V-Plot: Position v/s Fragment Size')
plt.xlabel('Position relative to reference point')
plt.ylabel('Fragment Size')
plt.ylim(40, 350)
plt.gca().set_facecolor('lightyellow')

plt.show()
