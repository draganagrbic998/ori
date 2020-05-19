from scipy import stats
from numpy import median, mean, var, std, quantile
from matplotlib.pyplot import boxplot

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
    #print ("Minimum uzorka: {}".format(mini))
    #print ("Maksimum uzorka: {}".format(maxi))
    #print ("Modusi uzorka: ")
    #for i in range(len(mo[0])):
        #print (str(mo[0][i]) + ": " + str(mo[1][i]))
    print ("Medijana uzorka: {}".format(me))
    #print ("Aritmeticka sredina uzorka: {}".format(mn))
    #print ("Varijansa uzorka: {}".format(sn2))
    #print ("Devijacija uzorka: {}".format(sn))
    #print ("Popravljena varijansa uzorka: {}".format(sn2_))
    #print ("Popravljena devijacija uzorka: {}".format(sn_))
    #print ("Koeficijent spljostenosti uzorka: {}".format(ks))
    #print ("Koeficijent asimetrije uzorka: {}".format(ka))
    #print ("Prvi kvartil uzorka: {}".format(q1))
    #print ("Drugi kvartil uzorka: {}".format(q2))
    #print ("Treci kvartil uzorka: {}".format(q3))
    #print ("Intermedijalni razmak uzorka: {}".format(iqr))
    #boxplot(data)


