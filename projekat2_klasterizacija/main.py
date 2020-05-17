from projekat2_klasterizacija.kmeans import calculate_cluster_number
from projekat2_klasterizacija.temp import read_data

if __name__ == '__main__':

    data = read_data()
    calculate_cluster_number(data)





