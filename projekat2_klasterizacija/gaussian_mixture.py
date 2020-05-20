import timeit
import pandas
from numpy import float32, median
from numpy import infty
from matplotlib import pyplot
from scipy import stats
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn import mixture
from projekat2_klasterizacija.util import read_data


column_names = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
            "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
            "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]


def find_best(data):

    lowest_bic = infty
    bic = []
    n_components_range = range(1, 13)
    cv_types = ['spherical', 'tied', 'diag', 'full']
    best_gmm = None

    print("Finding best covariance type and number of components...")
    start = timeit.default_timer()

    for cv_type in cv_types:
        for n_components in n_components_range:
            gmm = mixture.GaussianMixture(n_components=n_components,
                                          covariance_type=cv_type)
            gmm.fit(data)
            bic.append(gmm.bic(data))
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


def gaussian_mixture(data):

    model = mixture.GaussianMixture(n_components=7,covariance_type="full", max_iter=100000)
    model.fit(data)
    cluster_val = model.predict(data)
    data['cluster'] = cluster_val

    clusteri = {}
    for i in set(data['cluster']):
        clusteri[i] = data.loc[data['cluster'] == i]
    return clusteri, cluster_val


def get_descritpion_index(cluster_sizes, size):

    for i in range(len(cluster_sizes)):
        if cluster_sizes[i] == size:
            return i
    return None


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
    figure, ax = pyplot.subplots(figsize=(20, 13))
    cluster_sizes = sorted([len(cluster) for id, cluster in clusters])

    for id, cluster in clusters:
        ax.plot(cluster.x, cluster.y, marker='o', linestyle='', color=colors[id],
                label=opisi[len(cluster)], ms=5, mec='none')
        ax.set_aspect('auto')
        ax.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
        ax.tick_params(axis='y', which='both', left='off', top='off', labelleft='off')
    ax.legend()
    ax.set_title("Klasterizacija korisnika kreditnih kartica")
    pyplot.show()


def cluster_analysis(clusters, old_data):
    retval = {}

    suma = "{0:15}|".format("CLUSTER SIZE")
    for i in column_names:
        suma += ("{0:35}|").format(i)
    suma += "\n" + ("-" * 650)
    print (suma)

    for i in clusters:
        old_index = list(clusters[i].index.values)
        old_cluster = old_data.iloc[old_index, :]
        suma = ""

        counter = 0
        for j in column_names:
            if not counter:
                suma += "{:15}|".format(len(old_cluster))
            me = median(old_cluster[j])
            suma += ("med: {:30}|").format(me)
            counter += 1

            if j == "PURCHASES_FREQUENCY":
                if me < 0.1:
                    retval[len(old_cluster)] = "Vrlo retko kupuju, od toga "
                elif 0.1 <= me < 0.3:
                    retval[len(old_cluster)] = "Retko kupuju, od toga "
                elif 0.3 <= me < 0.7:
                    retval[len(old_cluster)] = "Relativno cesto kupuju, od toga "
                else:
                    retval[len(old_cluster)] = "Cesto kupuju, od toga "
            elif j == "ONEOFF_PURCHASES_FREQUENCY":
                if me <= 0.01:
                    retval[len(old_cluster)] += "prakticno nikad jednokratno, "
                elif 0.01 < me < 0.3:
                    retval[len(old_cluster)] += "retko jednokratno, "
                elif 0.3 <= me < 0.7:
                    retval[len(old_cluster)] += "relativno cesto jednokratno, "
                else:
                    retval[len(old_cluster)] += "uglavnom jednokratno, "
            elif j == "PURCHASES_INSTALLMENTS_FREQUENCY":
                if me <= 0.01:
                    retval[len(old_cluster)] += "prakticno nikad na rate, "
                elif 0.01 < me < 0.3:
                    retval[len(old_cluster)] += "retko na rate, "
                elif 0.3 <= me < 0.7:
                    retval[len(old_cluster)] += "relativno cesto na rate, "
                else:
                    retval[len(old_cluster)] += "uglavnom na rate, "
            elif j == "CASH_ADVANCE_FREQUENCY":
                if me <= 0.01:
                    retval[len(old_cluster)] += "prakticno nikad unapred, "
                elif 0.01 < me < 0.3:
                    retval[len(old_cluster)] += "retko unapred, "
                elif 0.3 <= me < 0.7:
                    retval[len(old_cluster)] += "relativno cesto unapred, "
                else:
                    retval[len(old_cluster)] += "uglavnom unapred, "
            elif j == "CREDIT_LIMIT":
                if me < 2000:
                    retval[len(old_cluster)] += "imaju nizak kredit limit"
                elif 2000 <= me < 3000:
                    retval[len(old_cluster)] += "imaju osrednji kredit limit"
                else:
                    retval[len(old_cluster)] += "imaju visok kredit limit"
            elif j == "TENURE":
                if me < 6:
                    retval[len(old_cluster)] += ", imaju kratko trajanje kartice."
                elif 6 <= me < 9:
                    retval[len(old_cluster)] += ", imaju osrednje trajanje kartice."
                else:
                    retval[len(old_cluster)] += "."
        suma += "\n"

        counter = 0
        for j in column_names:
            if not counter:
                suma += "{:15}|".format("")
            suma += ("min: {:30}|").format(min(old_cluster[j]))
            counter += 1
        suma += "\n"

        counter = 0
        for j in column_names:
            if not counter:
                suma += "{:15}|".format("")
            suma += ("max: {:30}|").format(max(old_cluster[j]))
            counter += 1
        suma += "\n"

        counter = 0
        for j in column_names:
            if not counter:
                suma += "{:15}|".format("")
            mo = stats.mode(old_cluster[j])
            for k in range(len(mo[0])):
                suma += ("mo:  {:30}|").format(str(mo[0][k]) + ": " + str(mo[1][k]))
            counter += 1

        suma += "\n" + ("-" * 650)
        print (suma)

    return retval


if __name__ == '__main__':

    data, data_orig = read_data()
    clusters, labels = gaussian_mixture(data)
    opisi = cluster_analysis(clusters, data_orig)
    clusters_visualization(data, labels, opisi)
