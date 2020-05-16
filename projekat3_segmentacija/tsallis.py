import dit
from numpy import zeros

def setup_probs(thresholds, pixels, level_nums):

    N = len(pixels)
    levels = []

    for i in range(len(thresholds)):
        if i == 0:
            levels.append([0, thresholds[0]])
        else:
            levels.append([thresholds[i - 1], thresholds[i]])

    levels.append([thresholds[len(thresholds) - 1], 255])

    for i in range(len(levels)):
        if i == 0:
            level_nums[i] = pixels[(pixels >= levels[i][0]) & (pixels <= levels[i][1])].size
        else:
            level_nums[i] = pixels[(pixels > levels[i][0]) & (pixels <= levels[i][1])].size

    return level_nums / N


def tsallis(thresholds, pixels):

    level_num = len(thresholds) + 1
    level_nums = zeros(level_num)
    level_names = [''] * level_num

    for i in range(0, level_num):
        level_names[i] = "L" + str(i)

    probs = setup_probs(thresholds, pixels, level_nums)
    dist = dit.Distribution(level_names, probs)
    return dit.other.tsallis_entropy(dist=dist, order=4)
