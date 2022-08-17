import matplotlib.pyplot as plt
import matplotlib.patches as patches
from aoi import *

"""
trial 0_0
rect1 = patches.Rectangle((1927, 693), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((1595, 569), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((1942, 259), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((753, -415), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
"""
'''
[[500, 550, 80, 100, 60], [1510, 550, 80, 100, 60], [630, 1010, 170, 130, 78], [1640, 1010, 170, 130, 78]],

[[410, 340, 40, 50, 0], [1420, 340, 40, 50, 0], [620, 610, 220, 80, 64], [1630, 610, 220, 80, 64], [100, 0, 85, 410, 0], 
[1110, 0, 85, 410, 0], [320, 950, 50, 80, 10], [1330, 950, 50, 80, 10]],

[[440, 470, 50, 40, 53], [1450, 470, 50, 40, 53], [445, 1080, 60, 100, 0], [1455, 1080, 60, 100, 0], [360, 595, 90, 55,
 40], [1370, 595, 90, 55, 40], [445, 395, 60, 45, 0], [1455, 395, 60, 45, 10], [400, 160, 100, 40, 10],
  [1410, 160, 100, 40, 10]],

[[850, 560, 65, 150, 60], [3120, 560, 65, 150, 60], [1300, 805, 50, 50, 0], [3570, 805, 50, 50, 0]],

[[1740, 150, 180, 160, 0], [4010, 150, 180, 160, 0], [1980, 720, 95, 95, 0], [4250, 720, 95, 95, 0], 
[1680, 980, 415, 200, 0], [3950, 980, 415, 200, 0]],
'''


def generate_image_aoi():
    rect1 = patches.Rectangle((1900, 200), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect2 = patches.Rectangle((4380, 200), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect3 = patches.Rectangle((2000, 230), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect4 = patches.Rectangle((4480, 230), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect5 = patches.Rectangle((150, 150), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect6 = patches.Rectangle((2630, 150), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect7 = patches.Rectangle((2000, 700), 230, 430, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect8 = patches.Rectangle((4480, 700), 230, 430, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect9 = patches.Rectangle((250, 50), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    rect10 = patches.Rectangle((2730, 50), 200, 200, 0, linewidth=3, edgecolor='r', facecolor='none')
    number_image = 2
    number_difference = 5

    fig, ax = plt.subplots(figsize=(47.24, 11.81))
    img = plt.imread(f"../seven_diff/img/img_{number_image}_{number_difference}.png")
    plt.axis('off')
    plt.imshow(img)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    ax.add_patch(rect4)
    ax.add_patch(rect5)
    ax.add_patch(rect6)
    ax.add_patch(rect7)
    ax.add_patch(rect8)
    ax.add_patch(rect9)
    ax.add_patch(rect10)

    # plt.savefig(f"aoi_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0,
    # dpi=250)

    print(img.shape[1], "x", img.shape[0])
    plt.tight_layout(pad=0)
    plt.savefig(f"AOI_seven_diff/test.png", bbox_inches=0, pad_inches=0, dpi=100)


def gen_img_aoi():
    cpt = 0
    for aois in AOI_seven_diff:
        fig, ax = plt.subplots(figsize=(shape_img[cpt][0] / 100, shape_img[cpt][1] / 100))
        img = plt.imread(f"../seven_diff/img/{list_img[cpt]}")
        plt.axis('off')
        plt.imshow(img)
        print(img.shape[1], "x", img.shape[0], f"cpt = {cpt}")
        for aoi in aois:
            for i in range(len(aoi)):
                if len(aoi) == 4:
                    locals()["rect" + str(i)] = patches.Rectangle((aoi[0], aoi[1]), aoi[2], aoi[3], linewidth=3,
                                                                  edgecolor='r', facecolor='none')
                    ax.add_patch(locals()["rect" + str(i)])
                elif len(aoi) == 5:
                    locals()["rect" + str(i)] = patches.Rectangle((aoi[0], aoi[1]), aoi[2], aoi[3], aoi[4], linewidth=3,
                                                                  edgecolor='r', facecolor='none')
                    ax.add_patch(locals()["rect" + str(i)])
                plt.tight_layout(pad=0)
                plt.savefig(f"AOI_seven_diff/{list_img[cpt][:-4]}_aoi.png", bbox_inches=0.0, pad_inches=0, dpi=100)
        cpt += 1


generate_image_aoi()
# gen_img_aoi()
