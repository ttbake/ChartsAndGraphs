from itertools import groupby

import csv
import matplotlib.pyplot as plt

input_file = 'iris.csv'
plt.figure(figsize=(7.5, 4.25))
plt.style.use('classic')

with open(input_file, 'r') as iris_data:
    irises = list(csv.reader(iris_data))

irises.pop()

petal_lengths = []

for species, group in groupby(irises, lambda i: i[4]):
    petal_lengths.append([float(petal[2]) for petal in group])

plt.boxplot(petal_lengths)
plt.axis([0, 4, 0, 10])
plt.xticks([1, 2, 3], ['Setosa', 'Versicolor', 'Virginica'])

plt.title("Fisher's Iris Data Set, Petal Length", fontsize=12, loc="left")
plt.xlabel("Iris Variety", fontsize=10)
plt.ylabel("Petal length (cm)", fontsize=10)

plt.show()