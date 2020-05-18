import pandas
from sklearn.preprocessing import StandardScaler, normalize
from projekat2_klasterizacija.kmeans import get_clusters

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

if __name__ == '__main__':
    data = read_data()
    clusters = get_clusters(data, 6)
    for i in clusters:
        print (clusters[i])



