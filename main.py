from cross_product import point_in_polygon_crossproduct
from ray_cast import point_in_polygon_raycast
import time

from polygenerator import random_polygon
import matplotlib.pyplot as plt


def is_inside(point, edges):
    start_time = time.time()
    cp_result = point_in_polygon_crossproduct(point, edges)
    cp_time = time.time() - start_time

    start_time = time.time()
    rc_result = point_in_polygon_raycast(point, edges)
    rc_time = time.time() - start_time
    print(f"{'_'*23}")
    print(f"Cross Product: {cp_result}.  Runtime: {cp_time}")
    print(f"Raycast: {rc_result}. Runtime: {rc_time}")


def onclick(event):
    xp, yp = event.xdata, event.ydata
    if is_inside((xp, yp), edges):
        plt.plot(xp, yp, "go", markersize=5)
    else:
        plt.plot(xp, yp, "ro", markersize=5)
    plt.gcf().canvas.draw()


point_1 = (1, 1)
polygon = [((0, 0), (0, 2)), ((0, 2), (2, 2)), ((2, 2), (2, 0))]

print(point_in_polygon_raycast(point_1, polygon))
print(point_in_polygon_crossproduct(point_1, polygon))

polygon = random_polygon(num_points=5000)
polygon.append(polygon[0])
edges = list(zip(polygon, polygon[1:] + polygon[:1]))
plt.figure(figsize=(10, 10))
plt.gca().set_aspect("equal")
xs, ys = zip(*polygon)
plt.gcf().canvas.mpl_connect("button_press_event", onclick)
plt.plot(xs, ys, "b-", linewidth=0.8)
plt.show()
