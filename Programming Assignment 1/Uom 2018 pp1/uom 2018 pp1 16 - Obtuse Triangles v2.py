#Solution by Bandara M.A.G.S.S

#Obtuse Triangles


from itertools import combinations
import math


def main():
    coordinates = get_coordinates()

    obtuse_tris = count_obtuse_triangles(coordinates)

    print(obtuse_tris)


def count_obtuse_triangles(coordinates):
    counter = 0
    triangles = combinations(coordinates, 3)
    print(list(triangles))
    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]

        side_lengths = [
            distance_squared(a, b),
            distance_squared(b, c),
            distance_squared(c, a)
        ]

        if any(side <= 0 for side in side_lengths):
            continue

        max_side = max(side_lengths)
        side_lengths.remove(max_side)

        if max_side > sum(side_lengths):
            counter += 1

    return counter


def distance_squared(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def get_coordinates():
    coordinates = []
    while True:
        inp = input().strip()

        if inp == "-1":
            break

        if inp == "":
            continue

        x, y = map(int, inp.split())
        coordinates.append((x, y))

    return coordinates


main()
