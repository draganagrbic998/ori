from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas

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
    data = pandas.concat([data, pandas.DataFrame({'cluster': kmeans.labels_})], axis=1) #tabeli dodamo jos jednu kolonu koja ce biti broj klastera

    clusters = {}
    for i in set(kmeans.labels_):
        clusters[i] = data.loc[data['cluster'] == i]

    return clusters


