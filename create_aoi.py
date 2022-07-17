import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect1 = patches.Rectangle((1420, 560), 80, 80, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((3670, 560), 80, 80, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((750, 350), 50, 300, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((3000, 350), 50, 300, linewidth=1, edgecolor='r', facecolor='none')
rect5 = patches.Rectangle((950, 750), 200, 150, linewidth=1, edgecolor='r', facecolor='none')
rect6 = patches.Rectangle((3200, 750), 200, 150, linewidth=1, edgecolor='r', facecolor='none')
rect7 = patches.Rectangle((650, 580), 100, 100, linewidth=1, edgecolor='r', facecolor='none')
rect8 = patches.Rectangle((2900, 580), 100, 100, linewidth=1, edgecolor='r', facecolor='none')
rect9 = patches.Rectangle((460, 490), 70, 70, linewidth=1, edgecolor='r', facecolor='none')
rect10 = patches.Rectangle((2710, 490), 70, 70, linewidth=1, edgecolor='r', facecolor='none')
rect11 = patches.Rectangle((130, 450), 80, 80, linewidth=1, edgecolor='r', facecolor='none')
rect12 = patches.Rectangle((2380, 450), 80, 80, linewidth=1, edgecolor='r', facecolor='none')

# [460, 490, 70, 70], [2710, 490, 70, 70],



number_image = 7
number_difference = 6

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
ax.add_patch(rect11)
ax.add_patch(rect12)
""""
ax.add_patch(rect5)
ax.add_patch(rect6)
ax.add_patch(rect7)
ax.add_patch(rect8)
"""

#plt.savefig(f"AOI_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
plt.savefig(f"AOI_seven_diff/test_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
