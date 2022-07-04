import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect1 = patches.Rectangle((355, 40), 45, 45, linewidth=1, edgecolor='r', facecolor='none')
rect2 = patches.Rectangle((50, 40), 45, 45, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((795, 40), 45, 45, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((795, 40), 45, 45, linewidth=1, edgecolor='r', facecolor='none')


number_image = 30
number_difference = 3

fig, ax = plt.subplots()
img = plt.imread(f"../seven_diff/img/img_{number_image}_{number_difference}.png")
plt.axis('off')
plt.imshow(img)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)

plt.savefig(f"AOI_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
