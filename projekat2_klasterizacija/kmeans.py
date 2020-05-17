from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def calculate_cluster_number(data):

    sse = {}
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, max_iter=1000).fit(data)
        sse[i] = kmeans.inertia_
        print ("ITERATION {} FINISHED".format(i))
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()

