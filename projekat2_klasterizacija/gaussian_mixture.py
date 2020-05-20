import timeit

from numpy import  infty
from sklearn import mixture
from matplotlib import pyplot

import matplotlib.pyplot as plt
import pandas
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from numpy import float32
from projekat2_klasterizacija.util import read_data
from projekat2_klasterizacija.util import cluster_analysis




def find_best(podaci):
    lowest_bic = infty
    bic = []
    n_components_range = range(1, 13)
    cv_types = ['spherical', 'tied', 'diag', 'full']
    best_gmm = None

    print("Finding best covariance type and number of components...")
    start = timeit.default_timer()

    for cv_type in cv_types:
        for n_components in n_components_range:
            # Fit a Gaussian mixture with EM
            gmm = mixture.GaussianMixture(n_components=n_components,
                                          covariance_type=cv_type)
            gmm.fit(podaci)
            bic.append(gmm.bic(podaci))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                best_gmm = gmm

    print("Results:\n  Covariance Type: " + str(best_gmm.covariance_type) + "\n  Num. Components: " + str(best_gmm.n_components))
    print("Time elapsed: " + str(timeit.default_timer() - start))

    pyplot.plot(bic, 'bx-')
    pyplot.axvline(x=12)
    pyplot.axvline(x=24)
    pyplot.axvline(x=36)
    pyplot.show()

    return best_gmm


def gaussian_mixture(podaci):
    model = mixture.GaussianMixture(n_components=7,covariance_type="full")#find_best(podaci)
    model.fit(podaci)
    cluster_val = model.predict(podaci)
    podaci['cluster'] = cluster_val

    clusteri = {}
    for i in set(podaci['cluster']):
        clusteri[i] = podaci.loc[podaci['cluster'] == i]

    return clusteri, cluster_val



def clusters_visualization(data, labels):
    d = data.astype(float32)
    dist = 1 - cosine_similarity(d)
    pca = PCA(2)
    pca.fit(dist)
    pca_data = pca.transform(dist)

    x, y, = pca_data[:, 0], pca_data[:, 1]

    colors = {
        0: 'red',
        1: 'blue',
        2: 'green',
        3: 'yellow',
        4: 'orange',
        5: 'purple',
        6: 'teal',
        7: 'magenta',
        8: 'grey',
        9: 'darkblue'
    }

    descriptions = {
        0: 'opis za klaster 0',
        1: 'opis za klaster 1',
        2: 'opis za klaster 2',
        3: 'opis za klaster 3',
        4: 'opis za klaster 4',
        5: 'opis za klaster 5',
        6: 'opis za klaster 6',
        7: 'opis za klaster 7',
        8: 'opis za klaster 8',
        9: 'opis za klaster 9'
    }

    pca_table = pandas.DataFrame({'x': x, 'y': y, 'cluster': labels})
    clusters = pca_table.groupby('cluster')

    figure, ax = plt.subplots(figsize=(20, 13))

    for id, cluster in clusters:
        ax.plot(cluster.x, cluster.y, marker='o', linestyle='', ms=5,
                color=colors[id], label=descriptions[id], mec='none')
        ax.set_aspect('auto')
        ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
        ax.tick_params(axis='y', which='both', left='off', top='off', labelleft='off')
    ax.legend()
    ax.set_title("Klasterizacija korisnika kreditnih kartica")
    plt.show()



if __name__ == '__main__':
    data, data_orig = read_data()
    clusters, labels = gaussian_mixture(data)
    cluster_analysis(clusters, data_orig)


    clusters_visualization(data, labels)