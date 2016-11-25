import numpy as np
import sklearn.cluster
import distance

listoks = "Breana Marquess Myrta Daigneault Maribeth Hocking Ivana Tiedemann Theodora Ortman Brianne Vierra Murray Roger Alma Haggins Rich Clinard Jone Telford Eloy Philpot Deedee Langlais Karri Lanford Eleni Kornegay Arline Griffieth Robbyn Verner Kathey Marek Laurene BrociousBrandon Barney Despina Mccain"
words = listoks.split(" ") #Replace this line
words = np.asarray(words) #So that indexing with a list will work
lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])

affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
affprop.fit(lev_similarity)
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    print(" - *%s:* %s" % (exemplar, cluster_str))