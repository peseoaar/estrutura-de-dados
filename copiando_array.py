import numpy as np

array_original = np.ones(10, dtype=int)
array_copia = np.empty(10)
i=0

print(array_original)
print(array_copia)

for i in range(10):
    array_copia[i] = array_original[i]

print("--------------------------")
print(array_original)
print(array_copia)