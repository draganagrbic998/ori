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
    temp = data
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
    return data, temp

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

def temp():

    for i in clusters:
        stari_indeksi = list(clusters[i].index.values)
        stari_kluster = old_data.iloc[stari_indeksi, :]
        print ("KLASTER BROJ {}".format(i))
        print ("BALANCE")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["BALANCE"])
        print ("BALANCE_FREQUENCY")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["BALANCE_FREQUENCY"])
        print ("PURCHASES")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["PURCHASES"])
        print ("ONEOFF_PURCHASES")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["ONEOFF_PURCHASES"])
        print ("INSTALLMENTS_PURCHASES")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["INSTALLMENTS_PURCHASES"])
        print ("CASH_ADVANCE")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["CASH_ADVANCE"])
        print ("PURCHASES_FREQUENCY")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["PURCHASES_FREQUENCY"])
        print ("ONEOFF_PURCHASES_FREQUENCY")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["ONEOFF_PURCHASES_FREQUENCY"])
        print ("PURCHASES_INSTALLMENTS_FREQUENCY")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["PURCHASES_INSTALLMENTS_FREQUENCY"])
        print ("CASH_ADVANCE_FREQUENCY")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["CASH_ADVANCE_FREQUENCY"])
        print ("CREDIT_LIMIT")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["CREDIT_LIMIT"])
        print ("PAYMENTS")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["PAYMENTS"])
        print ("MINIMUM_PAYMENTS")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["MINIMUM_PAYMENTS"])
        print ("PRC_FULL_PAYMENT")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["PRC_FULL_PAYMENT"])
        print ("TENURE")
        print ("-" * 30)
        descriptive_statistic(stari_kluster["TENURE"])
        print ("#" * 30)


if __name__ == '__main__':
    data, old_data = read_data()
    clusters, labels = get_clusters(data, 6)

    #clusters_visualization(data, labels)

    from projekat2_klasterizacija.data_analysis import descriptive_statistic
    from numpy import min, max

    analiza_dict = {}

    for label in column_names:
        analiza_dict[label] = {}

    for i in clusters:
        stari_indeksi = list(clusters[i].index.values)
        stari_kluster = old_data.iloc[stari_indeksi, :]
        for label in column_names:
            analiza_dict[label][i] = stari_kluster[label]

    from numpy import median

    suma = ""
    for j in column_names:
        suma += ("{0:40}|").format(j)
    suma += "\n" + ("-" * 650)
    print (suma)

    for i in clusters:
        stari_indeksi = list(clusters[i].index.values)
        stari_kluster = old_data.iloc[stari_indeksi, :]

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



    #for i in analiza_dict:

     #   print ("ANALIZA OBELEZJA {}".format(i))
      #  for j in analiza_dict[i]:
        #    print ("REZULTATI ZA KLASTER {}".format(j))
       #     descriptive_statistic(analiza_dict[i][j])
         #   print ("-" * 30)





