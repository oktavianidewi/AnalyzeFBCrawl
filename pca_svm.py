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
z = data.values
scalez = scale(z)

# X = scale(data)
# print 'scale aja : ', X

pca = PCA(n_components=30)
pca.fit(scalez)
var = pca.explained_variance_ratio_(scalez)
#var1 = np.