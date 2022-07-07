import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect1 = patches.Rectangle((255, 390), 20, 20, linewidth=1, edgecolor='r', facecolor='none')

rect2 = patches.Rectangle((313, 445), 40, 50, linewidth=1, edgecolor='r', facecolor='none')
rect3 = patches.Rectangle((430, 425), 85, 155, linewidth=1, edgecolor='r', facecolor='none')
rect4 = patches.Rectangle((200, 580), 50, 55, linewidth=1, edgecolor='r', facecolor='none')

rect5 = patches.Rectangle((1380, 400), 20, 20, linewidth=1, edgecolor='r', facecolor='none')
rect6 = patches.Rectangle((1445, 445), 40, 50, linewidth=1, edgecolor='r', facecolor='none')
rect7 = patches.Rectangle((1560, 425), 85, 155, linewidth=1, edgecolor='r', facecolor='none')
rect8 = patches.Rectangle((1333, 568), 50, 55, linewidth=1, edgecolor='r', facecolor='none')

number_image = 23
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

plt.savefig(f"AOI_seven_diff/img_{number_image}_{number_difference}_aoi.png", bbox_inches="tight", pad_inches=0, dpi=250)
