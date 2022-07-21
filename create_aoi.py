import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""
trial 0_0
rect1 = patches.Rectangle((1927, 693), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((1595, 569), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((1942, 259), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((753, -415), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
"""

# trial 0_2
rect1 = patches.Rectangle((1468, 624), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((803, 1278), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((1078, 957), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((1519, 628), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
number_image = 0
number_difference = 2

fig, ax = plt.subplots()
img = plt.imread(f"../seven_diff/img/img_{number_image}_{number_difference}.png")
plt.axis('off')
plt.imshow(img)
ax.add_patch(rect1)
# ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)

#plt.savefig(f"aoi_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
plt.savefig(f"AOI_seven_diff/test_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
