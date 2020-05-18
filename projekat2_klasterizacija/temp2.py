from projekat2_klasterizacija.temp import read_data
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
from projekat2_klasterizacija.temp import descriptive_statistic

x_labels = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES", "INSTALLMENTS_PURCHASES",
            "CASH_ADVANCE",
            "PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CASH_ADVANCE_TRX", "PURCHASES_TRX", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]


if __name__ == '__main__':


    data = read_data()
    #model = sm.OLS(data["PURCHASES_TRX"], data[["PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY"]]).fit()
    #print (model.summary())
    #plt.boxplot(data["CREDIT_LIMIT"])
    #plt.show()
    data = data.values
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    data = pd.DataFrame(data)
    #print (data)

    #print (temp)
    #plt.boxplot(data[13])
    #plt.show()
    #print (data[13])

    #n_clusters = 30
    #sse = []
    #for i in range(1, n_clusters):
     #   kmeans = KMeans(i)
      #  kmeans.fit(data)
      #  sse.append(kmeans.inertia_)
      #  print ("FINISHED ITERATION: {}".format(i))

    #plt.plot(sse, 'bx-')
    #plt.show()

    data.columns = x_labels  # set the header row as the df header

    #print (data["BALANCE"])


    kmeans = KMeans(6)
    kmeans.fit(data)

    #data = data.groupby('cluster')[x_labels].mean()
    #print (data)
    #print (mama)



    labels = kmeans.labels_
    #print (labels)
    #print (min(labels)) #klaster 0
    #print (max(labels)) #klaster 1
    #print (len(labels))




    mama = data.groupby(labels)




    clusters = pd.concat([data, pd.DataFrame({'cluster': labels})], axis=1)
    print (clusters)

    klusteri = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],

    }

    klusteri[0] = clusters.loc[clusters['cluster'] == 0]
    klusteri[1] = clusters.loc[clusters['cluster'] == 1]
    klusteri[2] = clusters.loc[clusters['cluster'] == 2]
    klusteri[3] = clusters.loc[clusters['cluster'] == 3]
    klusteri[4] = clusters.loc[clusters['cluster'] == 4]
    klusteri[5] = clusters.loc[clusters['cluster'] == 5]


    print ("DESKRIPTIVNA STATISTIKA ZA KLASTER 0")
    print ("BALANCE")
    descriptive_statistic(klusteri[0]["BALANCE"])

    #print (len(clusters))
    for c in clusters:
        #grid = sns.FacetGrid(clusters, col='cluster')
        #grid.map(plt.hist, c)
        #plt.show()
        #print (c)
        pass




