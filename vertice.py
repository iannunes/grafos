import sys
import arc

class vertice(object):
    def __init__(self, id, x, y, *args, **kwargs):
        self.__x=x
        self.__y=y
        self.__arcs = {}
        self.__arcs[id]={}
        self.__distances = {}
        self.__times = {}
        self.__id = id

        return super().__init__(*args, **kwargs)

    def addArc(self, a):
        self.__arcs[a.getVertice1().getId()][a.getVertice2().getId()]=a
        if a.getDistance()!=None:
            self.addDistance(a.getVertice2(),a.getDistance())
        if a.getTime()!=None:
            self.addTime(a.getVertice2(),a.getTime())

    def addInArc(self, arc):
        if (self.__id==arc.getVertice2().getId()):
            if (arc.getVertice1().getId() not in self.__arcs):
                self.__arcs[arc.getVertice1().getId()] = {}
            self.getArcs()[arc.getVertice1().getId()][self.__id]=arc

    def addDistance(self, v, distance):
        self.__distances[v.getId()]=distance

    def getDistance(self, v):
        return self.__distances[v.id]

    def addTime(self, v, time):
        self.__times[v.getId()]=time

    def getTime(self, v):
        return self.__times[v.id]

    def getId(self):
        return self.__id
    
    def getArcs(self):
        return self.__arcs


