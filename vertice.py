import sys
import arc

class vertice(object):
    def __init__(self, id, x, y, *args, **kwargs):
        self.__x=x
        self.__y=y
        self.__id = id
        self.__arcs = {}
        self.__inArcs = {}
        self.__distances = {}
        self.__times = {}

        #return super().__init__(*args, **kwargs)

    def addArc(self, a):
        self.__arcs[a.getVertice2().getId()]=a
        if a.getDistance()!=None:
            self.addDistance(a.getVertice2(),a.getDistance())
        if a.getTime()!=None:
            self.addTime(a.getVertice2(),a.getTime())

    def addInArc(self, a):
        v2=a.getVertice2()
        if (self.__id==v2.getId()):
            v1=a.getVertice1()
            if (v1.getId() not in self.__arcs):
                self.__inArcs[v1.getId()] = {}
            self.__inArcs[v1.getId()]=a

    def addDistance(self, v, distance):
        self.__distances[v.getId()]=distance

    def getDistance(self, v):
        return self.__distances[v.getId()]

    def addTime(self, v, time):
        self.__times[v.getId()]=time

    def getTime(self, v):
        return self.__times[v.getId()]

    def getId(self):
        return self.__id
    
    def getArcs(self):
        return self.__arcs


