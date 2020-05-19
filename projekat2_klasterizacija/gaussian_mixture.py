import timeit

from numpy import arange, infty
from sklearn import mixture
from matplotlib import pyplot

from projekat2_klasterizacija.main import read_data, clusters_visualization

font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 9,
        }

x_labels = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES", "INSTALLMENTS_PURCHASES",
            "CASH_ADVANCE",
            "PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CASH_ADVANCE_TRX", "PURCHASES_TRX", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]

x_labels_lower = ["balance", "balance frq", "purchases", "oneoff\npurchases", "installments\npurchases",
            "cash advance",
            "purchases frq", "oneoff\npurchases frq", "purchases\ninstallments frq",
            "cash\nadvance frq", "cash\nadvance trx", "purchases trx", "credit limit", "payments",
            "min payments", "prc full\npayment", "tenure"]


def insert_data_labels(ax, bars):
    for bar in bars:
        # Get X and Y placement of label from rect.
        y_value = bar.get_height()
        x_value = bar.get_x() + bar.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.2f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.


def visualize(data, n_components):
    indx = arange(len(x_labels_lower))
    score_label = arange(0, 1.125, 0.125)

    means = []

    for i in range(0, n_components):
        means.append(list(data.T[i]))

    bar_width = 0.15

    fig, ax = pyplot.subplots()

    ax.set_xticks(indx)
    ax.set_xticklabels(x_labels_lower, fontdict=font)

    ax.set_yticks(score_label)
    ax.set_yticklabels(score_label)

    for i in range(0, n_components):
        cluster_bar = ax.bar(indx + i * 0.15 / 2, means[i], bar_width, label=('Klaster ' + str(i)))
        insert_data_labels(ax, cluster_bar)

    ax.legend()

    pyplot.xticks(rotation=60)
    pyplot.show()


def find_best(podaci):
    lowest_bic = infty
    bic = []
    n_components_range = range(1, 10)
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

    return best_gmm


def gaussian_mixture(podaci):
    model = mixture.GaussianMixture(n_components=9,covariance_type="full")#find_best(podaci)
    model.fit(podaci)
    cluster_val = model.predict(podaci)
    podaci['cluster'] = cluster_val

    clusteri = {}
    for i in set(podaci['cluster']):
        clusteri[i] = podaci.loc[podaci['cluster'] == i]

    return clusteri, cluster_val


if __name__ == '__main__':
    data = read_data()
    clusters, labels = gaussian_mixture(data)

    clusters_visualization(data, labels)
