import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


offCoord = [[-2,-2],[-1,-2],[0,-2],[1,-2],[2,-2]]

offCoord = [[4,4]]

fig, ax = plt.subplots(1)
ax.set_aspect('equal')

for c in offCoord:
    hex = RegularPolygon((c[0], c[1]), numVertices=4, radius=2./3., alpha=0.2, edgecolor='b')
    ax.add_patch(hex)

circle = plt.Circle((4, 4), radius=0.5, fc='r')
rectangle = plt.Rectangle((3.75, 3.75), width=0.5, height=0.5, fc='b')
plt.gca().add_patch(circle)
plt.gca().add_patch(rectangle)


plt.autoscale(enable = True)
plt.show()