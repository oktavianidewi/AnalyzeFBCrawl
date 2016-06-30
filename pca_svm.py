import matplotlib.pyplot as plt
import seaborn
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# load data with np
arrcolumn = [0] + [ x for x in range(12, 932) ]
# arrcolumn = [ x for x in range(12, 932) ]
data = pd.read_csv('like_english_all.csv', usecols=arrcolumn)
data.head()
# print data
# print len(data)

pivoted = data.pivot_table(index = ['userid'], columns = ['Community'], fill_value = 0)
pivoted.head()
x = pivoted.values
print x.shape

Datapca = PCA(0.9).fit_transform(x)
print Datapca.shape()
