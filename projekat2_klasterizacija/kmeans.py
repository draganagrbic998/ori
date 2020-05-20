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
        kmeans = KMeans(i)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
        print ("FINISHED ITERATION: {}".format(i))
    plt.plot(sse, 'bx-')
    plt.show()

def get_clusters(data, clusters_number):

    kmeans = KMeans(clusters_number)
    kmeans.fit(data)
    temp = pandas.concat([data, pandas.DataFrame({'cluster': kmeans.labels_})], axis=1)

    clusters = {}
    for i in set(kmeans.labels_):
        clusters[i] = temp.loc[temp['cluster'] == i]
    return clusters, kmeans.labels_

def get_descritpion_index(cluster_sizes, size):

    for i in range(len(cluster_sizes)):
        if cluster_sizes[i] == size:
            return i
    return None

def clusters_visualization(data, labels):

    data = data.astype(float32)
    pca = PCA(2)
    dist = 1 - cosine_similarity(data)
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
        0: 'korisnici koji ne kupuju cesto, imaju manje novca na racunu, krace im traje kartica i uglavnom kupuju unapred', #ova grupa ima oko 700 korisnika
        1: 'korisnici koji osrednje menjaju stanje racuna, ne kupuju puno, retko kupuju jednokratno, uglavnom na rate, imaju ok kredit limit',  #ova grupa ima oko 1200 korisnika
        2: 'korisnici koji imaju osrednji do visok kredit limit, dosta uplacuju na racun, ne trose puno novca i uglavnom kupuju unapred',   #ova grupa ima oko 1400 korisnika
        3: 'korisnici koji imaju puno novca na racunu, trose vise od ostalih, imaju osrednji do visok kredit limit, retko kupuju unapred',  #ova grupa ima oko 1700 korisnika
        4: 'korisnici koji imaju osrednji kredit limit, manje trose od ostalih, uglavnom kupuju na rate',   #ova grupa ima oko 1800 korisnika
        5: 'korisnici koji cesto menjaju stanje racuna, slabiji kredit limit imaju, cesto placaju unapred'  #ova grupa ima oko 1900 korisnika
    }

    pca_table = pandas.DataFrame({'x': x, 'y': y, 'cluster': labels})
    clusters = pca_table.groupby('cluster')
    figure, ax = plt.subplots(figsize=(20, 13))
    cluster_sizes = sorted([len(cluster) for id, cluster in clusters])

    for id, cluster in clusters:
        ax.plot(cluster.x, cluster.y, marker='o', linestyle='', color=colors[id],
                label=descriptions[get_descritpion_index(cluster_sizes, len(cluster))], ms=5, mec='none')
        ax.set_aspect('auto')
        ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
        ax.tick_params(axis='y', which='both', left='off', top='off', labelleft='off')
    ax.legend()
    ax.set_title("Klasterizacija korisnika kreditnih kartica")
    plt.show()

if __name__ == '__main__':

    data, old_data = read_data()
    clusters, labels = get_clusters(data, 6)
    clusters_visualization(data, labels)
    cluster_analysis(clusters, old_data)
