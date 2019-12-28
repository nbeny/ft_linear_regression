from sklearn import preprocessing
import numpy as np

x = np.array([5, 8, 12, 15])
y = np.array([1, 2, 3, 4])

# Using Sklearn
normalizer_x = preprocessing.Normalizer(norm="l2").fit(x)
normalizer_y = preprocessing.Normalizer(norm="l2").fit(y)
x_norm = normalizer_x.transform(x)[0]
y_norm = normalizer_y.transform(y)[0]
print(x_norm)
print(y_norm)
