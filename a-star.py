def is_empty(obj):
    return not (len(obj) > 0)


def get_smaller_path(list_of_paths):
    smaller = (0, len(list_of_paths[0]))
    for index, path in enumerate(list_of_paths[1:]):
        if len(path) < smaller[1]:
            smaller = (index, len(path))

    print(list_of_paths[smaller[0]])
    smaller = (smaller[0], list_of_paths[smaller[0]])

    return smaller


def pop_smaller_path(list_of_paths):
    smaller = get_smaller_path(list_of_paths)

    del list_of_paths[smaller[0]]

    return smaller[1]


def get_last_node(path):
    # print(path)
    return path[-1]


def get_childrens(node, buckets=(3, 4)):
    childrens = []
    bucketA = buckets[0]
    bucketB = buckets[1]

    if node[0] < bucketA:
        childrens.append((bucketA, node[1]))
    if node[1] < bucketB:
        childrens.append((node[0], bucketB))
    if node[0] > 0:
        childrens.append((0, node[1]))
    if node[1] > 0:
        childrens.append((node[0], 0))
    if (node[0] > 0) and (node[1] < bucketB):
        a = node[0]
        b = node[1]
        while (a > 0) and (b < bucketB):
            a -= 1
            b += 1
        childrens.append((a, b))
    if (node[1] > 0) and (node[0] < bucketA):
        a = node[0]
        b = node[1]
        while (a < bucketA) and (b > 0):
            a += 1
            b -= 1
        childrens.append((a, b))

    return childrens


def remove_cycles(path, childrens):
    cycles = [node for node in path if node in childrens]
    for cycle in cycles:
        childrens.remove(cycle)

    return childrens


def dont_have_path_end_with_node(list_of_paths, child):
    pathsWithNode = [path for path in list_of_paths if path[-1] == child]

    return len(pathsWithNode) == 0


def get_smaller_path_end_with_node(list_of_paths, child):
    pathsWithNode = [path for path in list_of_paths if path[-1] == child]

    smaller = get_smaller_path(pathsWithNode)

    return smaller[1]


def remove_paths_end_with_node(list_of_paths, child):
    indexPathsWithNode = [
        index
        for index, path in enumerate(list_of_paths)
        if path[-1] == child
    ]

    for pathIndex in indexPathsWithNode:
        del list_of_paths[pathIndex]

    return list_of_paths


def a_star(rootNode, destinationNode, pathList):
    startPath = [rootNode]
    pathList.append(startPath)

    while not is_empty(pathList):
        caminho = pop_smaller_path(pathList)

        if get_last_node(caminho) == destinationNode:
            return caminho

        childrens = get_childrens(get_last_node(caminho))
        childrens = remove_cycles(caminho, childrens)

        heuristic(caminho, childrens, pathList)


def heuristic(path, childrens, pathList):
    for child in childrens:
        pathWithChild = [node for node in path]
        pathWithChild.append(child)

        if dont_have_path_end_with_node(pathList, child):
            pathList.append(pathWithChild)
        else:
            smallerPath = get_smaller_path_end_with_node(pathList, child)
            pathList = remove_paths_end_with_node(pathList, child)

            if len(pathWithChild) < len(smallerPath):
                pathList.append(pathWithChild)
            else:
                pathList.append(smallerPath)


if __name__ == "__main__":
    root = (0, 0)
    destination = (2, 0)
    pathList = []

    print("\nSolution: ", a_star(root, destination, pathList))
