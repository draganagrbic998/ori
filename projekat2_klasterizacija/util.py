from scipy import stats
from numpy import median, mean, var, std, quantile
from matplotlib.pyplot import boxplot
import pandas
from sklearn.preprocessing import StandardScaler, normalize

column_names = ["BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
            "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
            "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
            "CASH_ADVANCE_FREQUENCY", "CREDIT_LIMIT", "PAYMENTS",
            "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]


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
    boxplot(data)

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

def cluster_analysis(clusters, old_data):


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
