import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

def read_data():

    return pd.read_csv("credit_card_data.csv")

def descriptive_statistic(data):

    print (data["BALANCE"])

def temp():
    data = read_data()
    mama = data.isnull().sum().sort_values(ascending=False).head()
    print(mama)
    data.loc[(data['MINIMUM_PAYMENTS'].isnull() == True), 'MINIMUM_PAYMENTS'] = data['MINIMUM_PAYMENTS'].mean()
    data.loc[(data['CREDIT_LIMIT'].isnull() == True), 'CREDIT_LIMIT'] = data['CREDIT_LIMIT'].mean()
    mama = data.isnull().sum().sort_values(ascending=False).head()
    print(mama)

def hura():

    raw_data = pd.read_csv("credit_card_data.csv")
    data = raw_data.drop('CUST_ID', axis=1)
    data.loc[(data['MINIMUM_PAYMENTS'].isnull() == True), 'MINIMUM_PAYMENTS'] = data['MINIMUM_PAYMENTS'].mean()
    data.loc[(data['CREDIT_LIMIT'].isnull() == True), 'CREDIT_LIMIT'] = data['CREDIT_LIMIT'].mean()
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    data = normalize(data)
    sse = {}
    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
        sse[k] = kmeans.inertia_
        print ("ITERATION {} FINISHED".format(k))

    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of cluster")
    plt.ylabel("SSE")
    plt.show()


if __name__ == '__main__':


    temp = pd.read_csv("credit_card_data.csv")
    missing = temp.isna().sum()
    print (missing)
    temp = temp.fillna(temp.mean())
    missing = temp.isna().sum()
    print (missing)
    temp = temp.iloc[:, 1:].values
    wcss = []
    for i in range(1, 30):
        kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300)
        kmeans.fit_predict(temp)
        wcss.append(kmeans.inertia_)
        print ("ITERATION {} FINISHED".format(i))
    plt.plot(wcss, 'ro-', label="WCSS")
    plt.title("Computing WCSS for KMeans++")
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.show()





