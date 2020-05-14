import dit
from PIL import Image
from numpy import array, zeros
import timeit
from projekat1 import pso

def setup_probs(pixels, level_nums, thresholdi):
    N = len(pixels)

    levels = []

    for i in range(len(thresholdi)):
        if i == 0:
            levels.append([0, thresholdi[0]])
        else:
            levels.append([thresholdi[i - 1], thresholdi[i]])

    levels.append([thresholdi[len(thresholdi) - 1], 255])

    for i in range(len(levels)):
        if i == 0:
            level_nums[i] = pixels[(pixels >= levels[i][0]) & (pixels <= levels[i][1])].size
        else:
            level_nums[i] = pixels[(pixels > levels[i][0]) & (pixels <= levels[i][1])].size

    return level_nums / N


def tsallis(thresholdi, pixels):
    level_num = len(thresholdi) + 1
    level_nums = zeros(level_num)

    level_names = [''] * level_num

    for i in range(0, level_num):
        level_names[i] = "L" + str(i)

    probs = setup_probs(pixels, level_nums, thresholdi)

    dist = dit.Distribution(level_names, probs)
    return dit.other.tsallis_entropy(dist=dist, order=4)


def convert_pixels(pixels, thresholdi):





    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            for k in range(0, len(thresholdi)):
                if pixels[i][j][0] < thresholdi[k]:
                    if k == 0:
                        pixels[i][j][0:3] = 0
                    else:
                        pixels[i][j][0:3] = (thresholdi[k] + thresholdi[k - 1]) / 2
                    break
            if pixels[i][j][0] >= thresholdi[len(thresholdi) - 1]:
                pixels[i][j][0:3] = 255
    return pixels


#Treba nam samo jedna RGB vrednost jer su kod greyscale one iste
def simplify_pixels(pixels):

    #da ne prolazimo kroz svaki piksel, stavila sam da se ovo vektorski resi
    return pixels[:,:,0].ravel()    #ravel metoda ce od 2D niza napraviti 1D niz


#Nemoj slike vece od 512x512. Dugo ces cekati.
def main():
    #Pazi: onih 6 iz pdf-a se zavrsavaju na tif a ostale na tiff
    name = "peppers.tif"
    image = Image.open("images/" + name)
    pixels = array(image)
    pixels = pixels.copy()
    pixels.setflags(write=True)

    new_pixels = simplify_pixels(pixels)

    start = timeit.default_timer()
    thresholdi, max = pso.pso(tsallis, pixels=new_pixels, n_var=1, w=0.4, wLow=0.1, cgf=2, cpf=2, cgi=2, cpi=2, particle_num=20, iter_num=100)

    print("Najbolji pragovi: " + str(thresholdi))
    print("Najbolja vrednost Tsallis funkcije: " + str(max))
    print("Trajanje: " + str(timeit.default_timer() - start))

    pixels = convert_pixels(pixels, thresholdi)
    image = Image.fromarray(pixels)
    image.save("output/" + name)


#ako ovo iz main stavis ovde onda ce ti na nekim mestima pisati da ti parametar fje "shadow-uje" to isto iz sireg opsega
if __name__ == '__main__':
    main()

