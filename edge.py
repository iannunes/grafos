class edge(object):
    def __init__(self, v1, v2, distance=None, time=None):
        self.__vertice1 = v1
        self.__vertice2 = v2
        self.__distance = None
        self.__time = None
        if (time != None):
            self.__time=time
        if (distance != None):
            self.__distance=distance
        v1.addEdge(self)
        v2.addEdge(self)

    def setTime(self,t):
        self.__time=int(t)

    def setDistance(self,d):
        self.__distance=int(d)

    def getTime(self):
        if self.__time==None:
            return None
        return int(self.__time)

    def getDistance(self):
        if self.__distance ==None:
            return None
        return int(self.__distance)

    def getVertice1(self):
        return self.__vertice1

    def getVertice2(self):
        return self.__vertice2


