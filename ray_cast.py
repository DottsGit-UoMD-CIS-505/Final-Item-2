def point_in_polygon_raycast(point, edges):
    intersections = 0
    for edge_point_1, edge_point_2 in edges:
        x1, y1 = edge_point_1
        x2, y2 = edge_point_2
        dx = x2 - x1
        dy = y2 - y1
        # Check if ray from point could potentially intersect with the edge
        if (point[1] < y1) != (point[1] < y2) and (
            point[0] < (x1 + ((point[1] - y1) / dy) * dx)
        ):
            # Calculate intersection point with edge using parametric line equation
            intersections += 1
    if intersections % 2 == 1:
        return True
    return False
