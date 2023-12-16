import numpy as np


def point_in_polygon_crossproduct(point, polygon):
    previous_cross_product = None
    end_check = polygon[0][0]
    for current_vertex, next_vertex in polygon:
        if next_vertex == end_check:
            return True
        # Calculate vector from point to current vertex
        vector_1 = np.array(
            [point[0] - current_vertex[0], point[1] - current_vertex[1]]
        )

        # Calculate vector from point to next vertex
        vector_2 = np.array([point[0] - next_vertex[0], point[1] - next_vertex[1]])

        # Calculate cross product
        cross_product = np.cross(vector_1, vector_2)

        if previous_cross_product == None:
            previous_cross_product = cross_product
        elif not np.equal(np.sign(cross_product), np.sign(previous_cross_product)):
            return False
        previous_cross_product = cross_product

    return True
