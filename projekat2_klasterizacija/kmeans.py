import pandas
import matplotlib.pyplot as plt
from numpy import float32
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from projekat2_klasterizacija.util import read_data
from projekat2_klasterizacija.util import cluster_analysis

def calculate_cluster_number(data):

    sse = []
    for i in range(1, 30):
        kmeans = KMeans(i)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
        print ("FINISHED ITERATION: {}".format(i))
    plt.plot(sse, 'bx-')
    plt.show()

def get_clusters(data, cluster_number):

    kmeans = KMeans(cluster_number)
    kmeans.fit(data)
    temp = pandas.concat([data, pandas.DataFrame({'cluster': kmeans.labels_})], axis=1)

    clusters = {}
    for i in set(kmeans.labels_):
        clusters[i] = temp.loc[temp['cluster'] == i]

    return clusters, kmeans.labels_

def clusters_visualization(data, labels):

    data = data.astype(float32)

    dist = 1 - cosine_similarity(data)
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
        5: 'purple'
    }

    descriptions = {
        0: 'opis za klaster 0',
        1: 'opis za klaster 1',
        2: 'opis za klaster 2',
        3: 'opis za klaster 3',
        4: 'opis za klaster 4',
        5: 'opis za klaster 5'
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
    data, old_data = read_data()

    calculate_cluster_number(data)

    clusters, labels = get_clusters(data, 6)

    clusters_visualization(data, labels)
    cluster_analysis(clusters, old_data)
