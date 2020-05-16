from projekat3_segmentacija import pso
from projekat3_segmentacija.tsallis import tsallis
from PIL import Image
from numpy import array
import timeit

def simplify_pixels(pixels):

    return pixels[:,:,0].ravel()

def convert_pixels(pixels, thresholds):

    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            for k in range(0, len(thresholds)):
                if pixels[i][j][0] < thresholds[k]:
                    if k == 0:
                        pixels[i][j][0:3] = 0
                    else:
                        pixels[i][j][0:3] = (thresholds[k] + thresholds[k - 1]) / 2
                    break
            if pixels[i][j][0] >= thresholds[len(thresholds) - 1]:
                pixels[i][j][0:3] = 255
    return pixels

def main(name):

    image = Image.open("input/" + name)
    pixels = array(image)
    new_pixels = simplify_pixels(pixels)

    start = timeit.default_timer()
    thresholds, tsallis_value = pso.pso(tsallis, pixels=new_pixels, n_var=2, wi=0.4, wf=0.1, cgf=2, cpf=2, cgi=2, cpi=2, particle_num=20, iter_num=100)

    print("Thresholds: " + str(thresholds))
    print("Tsallis function value: " + str(tsallis_value))
    print("Time: " + str(timeit.default_timer() - start))

    pixels = convert_pixels(pixels, thresholds)
    image = Image.fromarray(pixels)
    image.save("output/" + name)

if __name__ == '__main__':
    main("peppers.tif")

