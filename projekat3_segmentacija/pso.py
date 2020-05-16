import numpy as np

def get_position(n_var):

    lista = sorted(np.random.randint(0, 255, n_var))
    return np.array(lista)

def pso(f, pixels, n_var = 1, wi = 0.9, wf = 0.4, cpi = 0.5, cpf = 2.5, cgi = 2.5, cgf = 0.5, particle_num = 10, iter_num = 10):

    best_position = None
    best_value = np.inf * (-1)

    deltaW = abs(wi - wf) / float(iter_num)
    deltaCp = abs(cpi - cpf) / float(iter_num)
    deltaCg = abs(cgi - cgf) / float(iter_num)

    w = wi
    cp = cpi
    cg = cgi

    population = []

    for i in range(0, particle_num):

        pos = get_position(n_var)
        fpoz = f(pos, pixels)

        if fpoz > best_value:
            best_position = pos
            best_value = fpoz

        particle = {
            'speed': 0,
            'position': pos,
            'value': fpoz,
            'best_position': pos,
            'best_value': fpoz,
        }

        population.append(particle)

    population = np.array(population)

    for i in range(0, iter_num):
        for p in population:

            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)

            p['speed'] = w * p['speed'] + r1 * cp  * (p['best_position'] - p['position']) + r2 * cg * (best_position - p['position'])
            p['position'] = np.add(p['position'], p['speed'], casting="unsafe")
            p['position'] = np.sort(p['position'])

            for j in range(0, n_var):
                if p['position'][j] > 254:
                    p['position'][j] = 254
                elif p['position'][j] < 1:
                    p['position'][j] = 1

            p['value'] = f(p['position'], pixels)

            if p['value'] > p['best_value']:
                p['best_position'] = p['position']
                p['best_value'] = p['value']

            if p['best_value'] > best_value:
                best_position = p['best_position']
                best_value = p['best_value']

        w += deltaW
        cp += deltaCp
        cg -= deltaCg

    return best_position, best_value



