import dit
from PIL import Image
from numpy import asarray, zeros
import timeit
from projekat1 import pso


def setup_probs(pixels, level_nums, thresholdi):
    N = len(pixels)

    for i in range(N):
        for j in range(len(thresholdi)):
            if pixels[i] < thresholdi[j]:
                level_nums[j] += 1
                break
        if pixels[i] >= thresholdi[len(thresholdi) - 1]:
            level_nums[len(level_nums) - 1] += 1

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
                        pixels[i][j][0:3] = thresholdi[0] / 2
                    else:
                        pixels[i][j][0:3] = (thresholdi[k] + thresholdi[k - 1]) / 2
                    break
            if pixels[i][j][0] >= thresholdi[len(thresholdi) - 1]:
                pixels[i][j][0:3] = (255 + thresholdi[len(thresholdi) - 1]) / 2
    return pixels


#Treba nam samo jedna RGB vrednost jer su kod greyscale one iste
def simplify_pixels(pixels):
    new_pixels = []

    for pixel_row in pixels:
        for pixel in pixel_row:
            new_pixels.append(pixel[0])

    return asarray(new_pixels)


#Nemoj slike vece od 512x512. Dugo ces cekati.
def main():
    #Pazi: onih 6 iz pdf-a se zavrsavaju na tif a ostale na tiff
    image = Image.open("images/lena.tif")
    pixels = asarray(image)
    pixels = pixels.copy()
    pixels.setflags(write=True)

    new_pixels = simplify_pixels(pixels)

    start = timeit.default_timer()
    thresholdi, max = pso.pso(tsallis, pixels=new_pixels, n_var=3, w=0.4, wLow=0.1, cpi=2, cpf=2, cgi=2, cgf=2, particle_num=10, iter_num=10)
    print(thresholdi)
    print(max)
    pixels = convert_pixels(pixels, thresholdi)
    print(timeit.default_timer() - start)
    image = Image.fromarray(pixels)
    image.save("output.tiff")


#ako ovo iz main stavis ovde onda ce ti na nekim mestima pisati da ti parametar fje "shadow-uje" to isto iz sireg opsega
if __name__ == '__main__':
    main()