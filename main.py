# Pseudo-Codigo

# a-estrela(raiz, destino, lista_caminhos)
# 	lista_caminhos.insere(new caminho(raiz));

# 	FAÇA
# 		caminho = lista_caminho.obtém_remove_menor_caminho();

# 		SE caminho.obtém_ultimo_no() == destino ENTÃO
# 			retorna caminho;
# 		FIM

# 		filhos = caminho.obtém_último_no().get_filhos();
# 		filhos = remove_ciclos(caminho, filhos);

# 		heuristica(caminho, filhos, lista_caminhos);

# 	ENQUANTO lista_caminhos != vazia FAÇA
# FIM

# heuristica(caminho, filhos, lista_caminhos)
# 	PARA CADA filho em filhos FAÇA

# 		SE lista_caminhos.não_tem_caminho_que_termina_em(filho) ENTÃO
# 			lista_caminhos.insere(caminho + filho);//concatena
# 		SENÃO
# 			cam = lista_caminhos.obtém_menor_caminho_que_termina_em(filho);
# 			lista_caminhos.remove_todos_caminhos_que_terminam_em(filho);

# 			SE (caminho+filho).tamanho() < cam.tamanho() ENTÃO
# 				lista_caminhos.insere(caminho+filho);
# 			ELSE
# 				lista_caminhos.insere(cam);
# 			FIM
# 		FIM

# 	FIM
# FIM


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otherNode):
        return (self.x == otherNode.x) and (self.y == otherNode.y)


class Path:
    def __init__(self, node):
        self.path = [node]

    def concat(self, node):
        """
        Return a concatenated path without change the original
            :param self:
            :param node: Node to be concatenated
        """
        concatenedPath = []
        concatenedPath.append(self.path)
        concatenedPath.append(node)

        return concatenedPath

    def get_last_node(self):
        """
        Return the last node of this path
            :param self: 
        """
        return self.path[-1]

    def length(self):
        """
        Return the length of the path
            :param self: 
        """
        return len(self.path)


class PathList:
    def __init__(self, path):
        self.pathList = [path]

    def append(self, newPath):
        """
        Append a new path to Path List
            :param self: 
            :param newPath: A Path
        """
        self.pathList.append(newPath)

    def is_empty(self):
        """
        Return true if the Path List is empty
            :param self: 
        """
        return len(self.pathList) == 0

    def get_smaller_path(self, pathList=None):
        """
        Return the smallest Path in the Path List
            :param self: 
            :param pathList=None: 
        """
        if pathList == None:
            pathList = self.pathList

        smaller = (0, len(pathList[0]))
        for index, path in enumerate(pathList[1:]):
            if path.length() < smaller[1]:
                smaller = (index, path.length())

        smaller = (smaller[0], pathList[smaller[0]])

        return smaller

    def pop_smaller_path(self):
        """
        Remove the smallest path and return them
            :param self: 
        """
        smaller = self.get_smaller_path()

        del self.pathList[smaller[0]]

        return smaller[1]

    def dont_have_path_end_with_node(self, endNode):
        """
        Return true the Path List doesn't contain any Path that ends with a certain Node
            :param self:
            :param endNode: A Node that will be compared
        """
        pathsWithNode = [path for path in self.pathList if path[-1] == endNode]

        return len(pathsWithNode) == 0

    def get_smaller_path_end_with_node(self, endNode):
        """
        Return the smallest Path that ends with a certain Node
            :param self: 
            :param endNode: A Node that will be compared
        """
        pathsWithNode = [path for path in self.pathList if path[-1] == endNode]

        smaller = self.get_smaller_path(pathsWithNode)

        return smaller[1]

    def remove_paths_end_with_node(self, endNode):
        """
        Remove all Paths that ends with a certain Node
            :param self: 
            :param endNode: A Node that will be compared
        """
        indexPathsWithNode = [index
                              for index, path in enumerate(self.pathList)
                              if path[-1] == endNode]

        for pathIndex in indexPathsWithNode:
            del self.pathList[pathIndex]


def a_star(rootNode, destinationNode, pathList):
    pathList.append(Path(rootNode))

    while not pathList.is_empty():
        caminho = pathList.pop_smaller_path()

        if caminho.get_last_node() == destinationNode:
            return caminho

        childrens = caminho.get_last_node().get_childrens()
        childrens = remove_cycles(caminho, childrens)

        heuristic(caminho, childrens, pathList)


def heuristic(path, childrens, pathList):
    for child in childrens:
        pathWithChild = path.concat(child)
        if pathList.dont_have_path_end_with_node(child):
            pathList.append(pathWithChild)
        else:
            smallerPath = pathList.get_smaller_path_end_with_node(child)
            pathList.remove_paths_end_with_node(child)

            if pathWithChild.length() < smallerPath.length():
                pathList.append(pathWithChild)
            else:
                pathList.append(smallerPath)
