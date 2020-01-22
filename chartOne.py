import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color= 'green', linestyle='dashdot', label='dash-dot')
plt.plot([2, 3, 4, 5], [2, 3, 4, 5], color= '#2B5B84', linestyle='dashed', label='dashed')
plt.ylabel('Important Figures')
plt.legend()
plt.show()