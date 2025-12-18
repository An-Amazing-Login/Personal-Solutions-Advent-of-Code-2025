"""first half:playground junction boxes"""

with open("input puzzle 8", "r", encoding="utf-8") as inputFile:
    auto_input = list(inputFile)

manual_input = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]

raw_input = [string.split(",") for string in auto_input]
positions = [(int(pos[0]), int(pos[1]), int(pos[2])) for pos in raw_input]
# print(positions)


dsquares = []
for i, pos1 in enumerate(positions):
    for j, pos2 in enumerate(positions):
        if j > i:
            dsquares.append(
                (
                    (pos1[0] - pos2[0]) ** 2
                    + (pos1[1] - pos2[1]) ** 2
                    + (pos1[2] - pos2[2]) ** 2,
                    pos1,
                    pos2,
                )
            )

# print(dsquares)
dsquares_sort = sorted(dsquares)
# print(dsquares_sort)

"""disjoint set forests. I did learn about this in data structures class"""
parents = [[p, 0, 1] for p in positions]
circuits = dict(zip(positions, parents))


def find_set(p):
    """finds the representative of the set by recursing to the fixpoint node."""
    if p != circuits[p][0]:
        circuits[p][0] = find_set(circuits[p][0])
    return circuits[p][0]


def link_sets(p1, p2):
    """links two set representatives and updates their rank"""
    if p1 == p2:
        return None

    if circuits[p1][1] > circuits[p2][1]:
        circuits[p2][0] = p1
        circuits[p1][2] = circuits[p1][2] + circuits[p2][2]
    else:
        circuits[p1][0] = p2
        circuits[p2][2] = circuits[p1][2] + circuits[p2][2]
        if circuits[p1][1] == circuits[p2][1]:
            circuits[p2][1] = circuits[p2][1] + 1


def disjoint_union(p1, p2):
    """makes a union of the sets that p1 and p2 are members of."""
    link_sets(find_set(p1), find_set(p2))


for n in range(10):
    first = dsquares_sort[n][1]
    second = dsquares_sort[n][2]
    disjoint_union(first, second)

# sizes_of_junctions = [x[2] for x in circuits.values()]
sizes_of_junctions = []
for key, (p, _, x) in circuits.items():
    if key == p:
        sizes_of_junctions.append(x)

SOFsort = sorted(sizes_of_junctions, reverse=True)
# print(SOFsort)
print(SOFsort[0] * SOFsort[1] * SOFsort[2])

"""second half in next file"""
