import numpy as np

def get_position(n_var):

    lista = [0] * n_var
    for i in range(n_var):
        lista[i] = np.random.uniform(-1, 1) #ovo cemo promeniti da ne uzima vrednost od -1 do 1, nego od
                                            #minimalnog nivoa sivile slike do maksimalnog nivoa sivila slike
    return np.array(lista)


def pso(f, n_var = 1, w = 0.9, wLow = 0.4, cpi = 0.5, cpf = 2.5, cgi = 2.5, cgf = 0.5, particle_num = 100, iter_num = 100, show_iter = 0):

    best_position = None
    best_value = np.inf

    deltaW = abs(w - wLow) / iter_num * 1.0
    deltaCp = abs(cpi - cpf) / iter_num * 1.0
    deltaCg = abs(cgi - cgf) / iter_num * 1.0

    cp = cpi
    cg = cgi

    population = []

    for i in range(0, particle_num):

        pos = get_position(n_var)
        fpoz = f(pos)

        if fpoz < best_value:
            best_position = pos
            best_value = fpoz

        particle = {
            'speed': get_position(n_var),
            'position': pos,
            'best_position': pos,
            'value': fpoz,
            'best_value': fpoz,
        }

        population.append(particle)

    population = np.array(population)

    for i in range(0, iter_num):

        for p in population:

            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)

            v = w * p['speed'] + cp * r1 * (p['best_position'] - p['position']) + cg * r2 * (best_position - p['position'])

            p['speed'] = v
            p['position'] += v
            p['value'] = f(p['position'])

            if p['value'] > p['best_value']:    #radimo maksimizaciju, pa ne treba da stoji "<"
                p['best_position'] = p['position']
                p['best_value'] = p['value']

            if p['best_value'] > best_value:    #radimo maksimizaciju pa ne treba da stoji "<"
                 best_position = p['best_position']
                 best_value = p['best_value']

        w += deltaW
        cp += deltaCp
        cg -= deltaCg

        if show_iter:
            print ("Iteration: " + str(i + 1) + ", best value: " + str(best_value))

    return best_position, best_value

#STA POSLE OVOGA

#treba da vidimo kako mozemo ucitati grayscale sliku kao numpy niz
#posto cemo prvo raditi sa slikama koje imaju 256 nivoa sive, treba da odredimo koje cemo K za pocetak koristiti
#=> K-thresholding => koliko threshold-a cemo imati
#kada odredimo K, onda ce nam inicijalne cestice biti dimenzije K i vrednosti ce biti od minimalnog sivila slike
#do maksimalnog sivila slike
#e sada kada nam PSO izracuna tu K-dimenzionalnu velicinu, trebalo bi da njene koordinate budu nasi thresholdi
#=> prva provera koju bismo trebali da uradimo jeste da se ne desi da ta K-dimenzionalna velicina ima neke iste koordinate
#jer svaka koordinata predstavlja novi threshold
#e kada dobijemo tu K-dimenzionalnu velicinu, treba da vidimo kako sliku da sredimo tako da piksele slike grupisemo u pragova
#kojima pripadaju
#i jos treba da vidimo koje parametre cemo koristiti
#i treba da vidimo kako da implementiramo Tsallis funkciju (ako ima neka bibiloteka sa ugradjenom Tsallis funkcijom super)
