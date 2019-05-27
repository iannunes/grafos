class arc(object):
    def __init__(self, v1, v2, distance=None, time=None):
        self.__vertice1 = v1
        self.__vertice2 = v2
        self.__distance = None
        self.__time = None
        if (time != None):
            self.__time=time
        if (distance != None):
            self.__distance=distance
        v1.addArc(self)
        v2.addInArc(self)

    def setTime(self,t):
        self.__time=t

    def setDistance(self,d):
        self.__distance=d

    def getTime(self):
        return self.__time

    def getDistance(self):
        return self.__distance

    def getVertice1(self):
        return self.__vertice1

    def getVertice2(self):
        return self.__vertice2


