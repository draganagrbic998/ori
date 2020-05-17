import pandas as pd
from scipy import stats
from numpy import median, mean, var, std, quantile

def read_data():

    data = pd.read_csv("credit_card_data.csv")
    data = data.fillna(data.mean())
    data = data.drop("CUST_ID", axis=1)
    return data

def descriptive_statistic(data):

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


if __name__ == '__main__':
    data = read_data()
    descriptive_statistic(data["BALANCE"])
    #descriptive_statistic(data["BALANCE_FREQUENCY"])
    #descriptive_statistic(data["PURCHASES"])
    #descriptive_statistic(data["ONEOFF_PURCHASES"])
    #descriptive_statistic(data["INSTALLMENTS_PURCHASES"])
    #descriptive_statistic(data["CASH_ADVANCE"])
    #descriptive_statistic(data["PURCHASES_FREQUENCY"])
    #descriptive_statistic(data["ONEOFF_PURCHASES_FREQUENCY"])
    #descriptive_statistic(data["PURCHASES_INSTALLMENTS_FREQUENCY"])
    #descriptive_statistic(data["CASH_ADVANCE_FREQUENCY"])
    #descriptive_statistic(data["CASH_ADVANCE_TRX"])
    #descriptive_statistic(data["PURCHASES_TRX"])
    #descriptive_statistic(data["CREDIT_LIMIT"])
    #descriptive_statistic(data["PAYMENTS"])
    #descriptive_statistic(data["MINIMUM_PAYMENTS"])
    #descriptive_statistic(data["PRC_FULL_PAYMENT"])
    #descriptive_statistic(data["TENURE"])


