import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect1 = patches.Rectangle((120, 180), 200, 200, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((2600, 180), 200, 200, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((1850, 200), 250, 150, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((4330, 200), 250, 150, linewidth=1, edgecolor='r', facecolor='none')
rect5 = patches.Rectangle((4480, 750), 200, 400, linewidth=1, edgecolor='r', facecolor='none')
rect6 = patches.Rectangle((2000, 750), 200, 400, linewidth=1, edgecolor='r', facecolor='none')
rect7 = patches.Rectangle((170, 0), 250, 180, linewidth=1, edgecolor='r', facecolor='none')
rect8 = patches.Rectangle((2650, 0), 250, 180, linewidth=1, edgecolor='r', facecolor='none')
rect9 = patches.Rectangle((2050, 180), 150, 350, linewidth=1, edgecolor='r', facecolor='none')
rect10 = patches.Rectangle((4530, 180), 150, 350, linewidth=1, edgecolor='r', facecolor='none')
number_image = 2
number_difference = 5

fig, ax = plt.subplots()
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
#plt.savefig(f"AOI_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
plt.savefig(f"AOI_seven_diff/test_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
