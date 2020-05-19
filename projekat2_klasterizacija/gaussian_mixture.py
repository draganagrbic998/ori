import timeit

from numpy import arange, infty
from sklearn import mixture
from matplotlib import pyplot

from projekat2_klasterizacija.main import read_data, clusters_visualization

column_names = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
            "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
            "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]


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


if __name__ == '__main__':
    data, data_orig = read_data()
    clusters, labels = gaussian_mixture(data)

    from numpy import min, max, median

    suma = ""
    for j in column_names:
        suma += ("{0:40}|").format(j)
    suma += "\n" + ("-" * 650)
    print (suma)

    for i in clusters:
        stari_indeksi = list(clusters[i].index.values)
        stari_kluster = data_orig.iloc[stari_indeksi, :]

        suma = ""
        for j in column_names:

            if j == "BALANCE":
                suma += ("med: {:35}|" ).format(str(len(stari_kluster)) + " " + str(median(stari_kluster[j])))

            else:
                suma += ("med: {:35}|" ).format(str(median(stari_kluster[j])))

        suma += "\n"
        for j in column_names:
            suma += ("min: {:35}|").format(str(min(stari_kluster[j])))
        suma += "\n"
        for j in column_names:
            suma += ("max: {:35}|").format(str(max(stari_kluster[j])))

        from scipy import stats
        suma += "\n"

        for j in column_names:
            mo = stats.mode(stari_kluster[j])
            for k in range(len(mo[0])):
                suma += ("moo: {:35}|").format(str(mo[0][k]) + ": " + str(mo[1][k]))


        suma += "\n" + ("-" * 650)
        print (suma)

    clusters_visualization(data, labels)


