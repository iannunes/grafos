import sys
import arc

class vertice(object):
    def __init__(self, id, x, y, *args, **kwargs):
        self.__x=int(x)
        self.__y=int(y)
        self.__id = int(id)
        self.__arcs = {}
        self.__inArcs = {}
        self.__distances = {}
        self.__times = {}
        self.__edges = {}

        #return super().__init__(*args, **kwargs)

    def addArc(self, a):
        if (a in self.__arcs):
            return
        v2 = a.getVertice2()
        self.__arcs[v2.getId()]=a
        if a.getDistance()!=None:
            self.addDistance(v2,a.getDistance())
        if a.getTime()!=None:
            self.addTime(v2,a.getTime())

    def addInArc(self, a):
        if (a in self.__inArcs):
            return
        v2=a.getVertice2()
        if (self.__id==v2.getId()):
            v1Id=a.getVertice1().getId()
            if (v1Id not in self.__arcs):
                self.__inArcs[v1Id] = {}
            self.__inArcs[v1Id]=a

    def addEdge(self, a):
        v1 = self
        v2 = a.getVertice2()
        if (v2.getId() == v1.getId()):
            v2= a.getVertice1()
        v1Id = v1.getId()
        v2Id = v2.getId()
        if (v2Id not in self.__edges):
            self.__edges[v2.getId()]=a
            if a.getDistance()!=None:
                self.addDistance(v2,a.getDistance())
            if a.getTime()!=None:
                self.addTime(v2,a.getTime())
        if (v1Id not in v2.getEdges()):
            v2.addEdge(a)

    def addDistance(self, v, distance):
        self.__distances[v.getId()]=int(distance)

    def getDistance(self, v):
        return self.__distances[v.getId()]

    def addTime(self, v, time):
        self.__times[v.getId()]=int(time)

    def getTime(self, v):
        return self.__times[v.getId()]

    def getId(self):
        return self.__id
    
    def getArcs(self):
        return self.__arcs

    def getEdges(self):
        return self.__edges

