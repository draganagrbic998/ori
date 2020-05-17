import timeit

from numpy import arange, infty
from sklearn import preprocessing, mixture
from matplotlib import pyplot
import pandas


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


def find_best(data):
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
            gmm.fit(data)
            bic.append(gmm.bic(data))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                best_gmm = gmm

    print("Results:\n  Covariance Type: " + str(best_gmm.covariance_type) + "\n  Num. Components: " + str(best_gmm.n_components))
    print("Time elapsed: " + str(timeit.default_timer() - start))

    return best_gmm


def gaussian_mixture():
    data = pandas.read_csv("credit_card_data.csv", sep=",", usecols=range(1, 18))
    data.fillna(data.mean(), inplace=True)

    #x = data.values
    #min_max_scaler = preprocessing.MinMaxScaler()
    #x_scaled = min_max_scaler.fit_transform(x)
    #data = pandas.DataFrame(x_scaled)

    data = data[1:]  # take the data less the header row
    data.columns = x_labels  # set the header row as the df header

    model = mixture.GaussianMixture(n_components=8,
                                          covariance_type="full")#find_best(data)
    model.fit(data)
    data['cluster'] = model.predict(data)
    data = data.groupby('cluster')[x_labels].mean()

    visualize(data, model.n_components)


if __name__ == '__main__':
    gaussian_mixture()
