import dit
from PIL import Image
from numpy import asarray

from projekat1 import pso


def setup_probs(pixels, level_nums, thresholdi, probs):
    N = 0

    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            for k in range(0, len(thresholdi)):
                if pixels[i][j][0] < thresholdi[k]:
                    level_nums[k] += 1
                    break
            if pixels[i][j][0] >= thresholdi[len(thresholdi) - 1]:
                level_nums[len(level_nums) - 1] += 1
            N += 1

    for i in range(0, len(probs)):
        probs[i] = level_nums[i] / N


def tsallis(thresholdi, pixels):
    level_num = len(thresholdi) + 1
    level_nums = [0] * level_num
    probs = [0] * level_num

    level_names = [''] * level_num

    for i in range(0, level_num):
        level_names[i] = "L" + str(i)

    setup_probs(pixels, level_nums, thresholdi, probs)
    dist = dit.Distribution(level_names, probs)
    #order je ono q (index entropije). To se izgleda eskperimentalno podesava. Ja stavio ovo za sad:
    return dit.other.tsallis_entropy(dist=dist, order=(1 - 1/level_num))


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

#Nemoj slike vece od 512x512. Dugo ces cekati.
def main():
    image = Image.open("images/3.2.25.tiff")
    pixels = asarray(image)
    pixels = pixels.copy()
    pixels.setflags(write=True)

    thresholdi, max = pso.pso(tsallis, pixels=pixels, n_var=3)
    print(thresholdi)
    print(max)
    pixels = convert_pixels(pixels, thresholdi)

    image = Image.fromarray(pixels)
    image.save("output.tiff")


#ako ovo iz main stavis ovde onda ce ti na nekim mestima pisati da ti parametar fje "shadow-uje" to isto iz sireg opsega
if __name__ == '__main__':
    main()