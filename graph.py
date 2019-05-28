import arc
import vertice

class graph(object):
    """contains graph data structures and some functions"""
    def __init__(self, *args, **kwargs):
        self.__arcs = {}
        self.__vertices = {}
        self.__distances = {}
        self.__times = {}

        return super().__init__(*args, **kwargs)

    def addVertice(self, vertice):
        v1Id = vertice.getId()
        self.__vertices[v1Id]=vertice
        if v1Id not in self.__arcs:
            self.__arcs[v1Id] = {}
        if len(vertice.getArcs())>0:
            for i,a in vertice.getArcs().items():
                self.__arcs[v1Id][a.getVertice2().getId()] = a

    def addArc(self,arc):
        self.__createArcsDictionary(v1,v2,False)

        self.__arcs[arc.getVertice1().getId()][arc.getVertice2().getId()]=arc
    
    def getVertices(self):
        return self.__vertices

    def addDistance(self,v1,v2,distance):
        self.__createArcsDictionary(v1,v2)

        self.__arcs[v1.getId()][v2.getId()].setDistance(distance)

    def addTime(self,v1,v2,time):
        self.__createArcsDictionary(v1,v2)

        self.__arcs[v1.getId()][v2.getId()].setTime(time)

    def __createArcsDictionary(self, v1, v2, create=True):
        newArc = False
        v1Id = v1.getId()
        v2Id = v2.getId()
        if v1Id not in self.__arcs:
            self.__arcs[v1Id] = {}
            self.__arcs[v1Id][v2Id] = {}
            newArc = True
        elif v2Id not in self.__arcs[v1Id]:
            newArc = True
            if create==False:
                self.__arcs[v1Id][v2Id] = {}

        if newArc and create:
            a = arc.arc(v1,v2)
            self.__arcs[v1Id][v2Id] = a
            v1.addArc(a)
            v2.addInArc(a)

        return self.__arcs[v1Id][v2Id]
            
    def removeArc(self, v1,v2):
        v1.removeArc(v2);
        v2.removeInArc(v1);
        v1Id = v1.getId()
        v2Id = v2.getId()
        if v1Id not in self.__arcs:
            if v2Id not in self.__arcs[v1Id]:
                self.__arcs[v1Id].pop(v2Id)
        if v1Id not in self.__times:
            if v2Id not in self.__times[v1Id]:
                self.__times[v1Id].pop(v2Id)
        if v1Id not in self.__distances:
            if v2Id not in self.__distances[v1Id]:
                self.__distances[v1Id].pop(v2Id)

    def getArcs(self):
        return self.__arcs.copy()

    def loadVertices(self, path):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="v":
            line = f.readline() 
        while len(line)>0 and line[0]=="v":
            arrayLine = line.strip().split(" ")
            v = vertice.vertice(arrayLine[1],arrayLine[2],arrayLine[3])
            self.addVertice(v)
            line = f.readline()

        f.close()
    
    def __addDistance(self, a):
        v1 = a.getVertice1()
        v2 = a.getVertice2()
        if (v1.getId() not in self.__distances):
            self.__distances[v1.getId()] = {}
        self.__distances[v1.getId()][v2.getId()]=a.getDistance()

    def loadDistances(self, path):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="a":
            line = f.readline() 

        while len(line)>0 and line[0]=="a":
            arrayLine = line.strip().split(" ")
            v1 = self.getVertices()[arrayLine[1]]
            v2 = self.getVertices()[arrayLine[2]]

            a = self.__createArcsDictionary(v1, v2, True)
            a.setDistance(arrayLine[3])
            v1.addDistance(v2,arrayLine[3])
            self.__addDistance(a)

            line = f.readline() 

        f.close()

    def __addTime(self, a):
        v1 = a.getVertice1()
        v2 = a.getVertice2()
        if (v1.getId() not in self.__times):
            self.__times[v1.getId()] = {}
        self.__times[v1.getId()][v2.getId()]=a.getTime()

    def loadTimes(self, path):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="a":
            line = f.readline() 

        while len(line)>0 and line[0]=="a":
            arrayLine = line.strip().split(" ")
            v1 = self.getVertices()[arrayLine[1]]
            v2 = self.getVertices()[arrayLine[2]]

            a = self.__createArcsDictionary(v1, v2, True)
            a.setTime(arrayLine[3])
            self.__addTime(a)
            v1.addTime(v2,arrayLine[3])
            line = f.readline() 

        f.close()