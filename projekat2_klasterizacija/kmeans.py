import pandas
import matplotlib.pyplot as plt
from numpy import float32
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from projekat2_klasterizacija.util import read_data
from projekat2_klasterizacija.util import cluster_analysis

def calculate_clusters_number(data):

    sse = []
    for i in range(1, 30):
        kmeans = KMeans(i, max_iter=100)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
        print ("FINISHED ITERATION: {}".format(i))
    plt.plot(sse, 'bx-')
    plt.show()

def get_clusters(data, clusters_number):

    kmeans = KMeans(clusters_number, max_iter=100000)
    kmeans.fit(data)
    temp = pandas.concat([data, pandas.DataFrame({'cluster': kmeans.labels_})], axis=1)

    clusters = {}
    for i in set(kmeans.labels_):
        clusters[i] = temp.loc[temp['cluster'] == i]
    return clusters, kmeans.labels_


def clusters_visualization(data, labels, opisi):

    d = data.astype(float32)
    pca = PCA(2)
    dist = 1 - cosine_similarity(d)
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

    pca_table = pandas.DataFrame({'x': x, 'y': y, 'cluster': labels})
    clusters = pca_table.groupby('cluster')
    figure, ax = plt.subplots(figsize=(20, 13))

    for id, cluster in clusters:
        ax.plot(cluster.x, cluster.y, marker='o', linestyle='', color=colors[id],
                label=opisi[len(cluster)], ms=5, mec='none')
        ax.set_aspect('auto')
        ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
        ax.tick_params(axis='y', which='both', left='off', top='off', labelleft='off')
    ax.legend()
    ax.set_title("Klasterizacija korisnika kreditnih kartica")
    plt.show()

if __name__ == '__main__':

    data, old_data = read_data()
    calculate_clusters_number(data)
    clusters, labels = get_clusters(data, 6)
    opisi = cluster_analysis(clusters, old_data)
    clusters_visualization(data, labels, opisi)
