import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from Orange.data import Table
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib

train = np.array(in_data)

plt.figure(figsize=(14,12))
for digit_num in range(0,70):
    plt.subplot(7,10,digit_num+1)
    grid_data = train[digit_num][1:].reshape(28,28)  # reshape from 1d to 2d pixel array
    plt.imshow(grid_data, interpolation = "none", cmap = "afmhot")
    plt.title(str(int(train[digit_num][0])))
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()

