class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otherNode):
        return (self.x == otherNode.x) and (self.y == otherNode.y)


class Path:
    def __init__(self, node):
        self.path = [node]

    def get_last_node(self):
        return self.path[-1]


class PathList:
    def __init__(self, path):
        self.pathList = [path]

    def append(self, newPath):
        self.pathList.append(newPath)

    def isEmpty(self):
        return len(self.pathList) == 0

    def get_smaller_path(self, pathList=None):
        if pathList == None:
            pathList = self.pathList

        smaller = (0, len(pathList[0]))
        for index, path in enumerate(pathList[1:]):
            if len(path) < smaller[1]:
                smaller = (index, len(path))

        smaller = (smaller[0], pathList[smaller[0]])

        return smaller

    def pop_smaller_path(self):
        smaller = self.get_smaller_path()

        del self.pathList[smaller[0]]

        return smaller[1]

    def dont_have_path_end_with_node(self, endNode):
        pathsWithNode = [path for path in self.pathList if path[-1] == endNode]

        return len(pathsWithNode) == 0

    def get_smaller_path_end_with_node(self, endNode):
        pathsWithNode = [path for path in self.pathList if path[-1] == endNode]

        smaller = self.get_smaller_path(pathsWithNode)

        return smaller[1]

    def remove_paths_end_with_node(self, endNode):
        indexPathsWithNode = [index
                              for index, path in enumerate(self.pathList)
                              if path[-1] == endNode]

        for pathIndex in indexPathsWithNode:
            del self.pathList[pathIndex]


def a_estrela(raiz, destino, lista_caminhos):
    lista_caminhos.append(new Caminho(raiz))

    while not lista_caminhos.isEmpty():
        caminho = lista_caminhos.pop_smaller()

        if caminho.get_last_node() == destino:
            return caminho

        filhos = caminho.get_last_node().get_childrens()
        filhos = remove_cycles(caminho, filhos)

        heuristica(caminho, filhos, lista_caminhos)


def heuristica(caminho, filhos, lista_caminhos):
    for filho in filhos:
        if lista_caminhos.dont_end_with(filho):
            caminho_filho = [].append(caminho).append(filho)
            lista_caminhos.append(caminho_filho)
        else:
            cam = lista_caminhos.get_smaller_end_with(filho)
            lista_caminhos.remove_all_end_with(filho)

            caminho_filho = [].append(caminho).append(filho)
            if caminho_filho.length() < cam.length():
                lista_caminho.append(caminho_filho)
            else:
                lista_caminhos.append(cam)
