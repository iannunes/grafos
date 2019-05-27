import arc
import vertice

class graph(object):
    """contains graph data structures and some functions"""
    def __init__(self, *args, **kwargs):
        self.__arcs = {}
        self.__vertices = {}
        return super().__init__(*args, **kwargs)

    def addVertice(self, vertice):
        self.__vertices[vertice.getId()]=vertice
        self.__arcs[vertice.getId()] = vertice.getArcs()

    def addArc(self,arc):
        #if (arc.getVertice1().getId() in self.__arcs):
        #    self.__arcs[arc.getVertice1().getId()] = {}
        self.__arcs[arc.getVertice1().getId()][arc.getVertice2().getId()]=arc
        arc.getVertice2().addInArc(arc)
        #if (arc.getVertice2().getId() in self.__arcs):
        #    self.__arcs[arc.getVertice2().getId()] = {}
        #self.__arcs[arc.getVertice2().getId()][arc.getVertice1().getId()]=arc
    
    def getVertices(self):
        return self.__vertices

    def getArcs(self):
        return self.__arcs