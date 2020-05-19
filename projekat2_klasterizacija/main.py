import pandas
from numpy import float32
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from projekat2_klasterizacija.kmeans import get_clusters
import matplotlib.pyplot as plt

column_names = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
            "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
            "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]

def read_data():

    data = pandas.read_csv("credit_card_data.csv")
    data = data.fillna(data.mean())    #null vrednosti zameni sa srednjom vrednoscu
    data = data.drop("CUST_ID", axis=1)     #id korisnika nam nije potreban
    #lm = sm.OLS(data["CASH_ADVANCE_TRX"], data["CASH_ADVANCE_FREQUENCY"]).fit()
    #print (lm.summary())    #kolone 'CASH_ADVANCE_TRX' i 'CASH_ADVANCE_FREQUENCY' jako zavise
    data = data.drop("CASH_ADVANCE_TRX", axis=1)    #posto kolone jako zavise, izbacujemo 'CASH_ADVANCE_TRX' iz klasterizacija
    #lm = sm.OLS(data["PURCHASES_TRX"], data[["PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY"]]).fit()
    #print (lm.summary())    #kolona 'PURCHASES_TRX' jako zavisi od kolona 'URCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY'
    data = data.drop("PURCHASES_TRX", axis=1)   #posto kolone jako zavise, izbacujemo 'PURCHASES_TRX' iz klasterizacije
    data = data.values
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    data = normalize(data)
    data = pandas.DataFrame(data)
    data.columns = column_names
    return data

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
    data = read_data()
    clusters, labels = get_clusters(data, 6)

    clusters_visualization(data, labels)



