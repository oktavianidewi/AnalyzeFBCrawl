import matplotlib.pyplot as plt
import seaborn
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

from mpl_toolkits.mplot3d import Axes3D

# load data with np
# arrcolumn = [0] + [ x for x in range(12, 932) ]
arrcolumn = [ x for x in range(12, 932) ]
# arrcolumn = [ x for x in range(12, 932) ]
data = pd.read_csv('like_english_all.csv', usecols=arrcolumn)
X = data.values
X = scale(X)

# X = scale(data)
# print 'scale aja : ', X

pca = PCA(n_components=40)
pca.fit(X)
var = pca.explained_variance_ratio_
# var1 = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print var