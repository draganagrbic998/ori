import pandas
import matplotlib.pyplot as plt
from numpy import median, mean, var, std, quantile
from matplotlib.pyplot import boxplot
from scipy import stats
from sklearn.preprocessing import StandardScaler, normalize

column_names = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
            "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
            "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]

def descriptive_statistic(data, column_name):

    n = len(data)
    mini = min(data)
    maxi = max(data)
    mo = stats.mode(data)
    me = median(data)
    mn = mean(data)
    sn2 = var(data)
    sn = std(data)
    sn2_ = sn2 * n / (n - 1)
    sn_ = sn2_ ** 0.5
    q1 = quantile(data, 0.25)
    q2 = quantile(data, 0.5)
    q3 = quantile(data, 0.75)
    iqr = q3 - q1
    mi4 = mean((data - mean(data)) ** 4)
    mi3 = mean((data - mean(data)) ** 3)
    mi2 = mean((data - mean(data)) ** 2)
    ks = mi4 / mi2 ** 2
    ka = mi3 / mi2 ** 1.5

    print ("Velicina uzorka: {}".format(n))
    print ("Minimum uzorka: {}".format(mini))
    print ("Maksimum uzorka: {}".format(maxi))
    print ("Modusi uzorka: ")
    for i in range(len(mo[0])):
        print (str(mo[0][i]) + ": " + str(mo[1][i]))
    print ("Medijana uzorka: {}".format(me))
    print ("Aritmeticka sredina uzorka: {}".format(mn))
    print ("Varijansa uzorka: {}".format(sn2))
    print ("Devijacija uzorka: {}".format(sn))
    print ("Popravljena varijansa uzorka: {}".format(sn2_))
    print ("Popravljena devijacija uzorka: {}".format(sn_))
    print ("Koeficijent spljostenosti uzorka: {}".format(ks))
    print ("Koeficijent asimetrije uzorka: {}".format(ka))
    print ("Prvi kvartil uzorka: {}".format(q1))
    print ("Drugi kvartil uzorka: {}".format(q2))
    print ("Treci kvartil uzorka: {}".format(q3))
    print ("Intermedijalni razmak uzorka: {}".format(iqr))
    boxplot(data)
    plt.title("BOX PLOT FOR COLUMN {}".format(column_name))
    plt.show()

def read_data():

    data = pandas.read_csv("credit_card_data.csv")
    data = data.fillna(data.mean())
    temp = data
    data = data.drop("CUST_ID", axis=1)
    #lm = sm.OLS(data["CASH_ADVANCE_TRX"], data["CASH_ADVANCE_FREQUENCY"]).fit()
    #print (lm.summary())
    data = data.drop("CASH_ADVANCE_TRX", axis=1)
    #lm = sm.OLS(data["PURCHASES_TRX"], data[["PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY"]]).fit()
    #print (lm.summary())
    data = data.drop("PURCHASES_TRX", axis=1)
    data = data.values
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    data = normalize(data)
    data = pandas.DataFrame(data)
    data.columns = column_names
    return data, temp

def cluster_analysis(clusters, old_data):

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
            suma += ("med: {:30}|").format(median(old_cluster[j]))
            counter += 1
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

if __name__ == '__main__':

    data, old_data = read_data()
    for i in column_names:
        print ("**********DESCRIPTIVE STATISTIC FOR COLUMN {}**********".format(i))
        descriptive_statistic(old_data[i], i)
        print ("-" * 50)