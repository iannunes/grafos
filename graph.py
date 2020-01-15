import edge
import vertice
from operator import itemgetter, attrgetter, methodcaller

class graph(object):
    """contains graph data structures and some functions"""
    def __init__(self, *args, **kwargs):
        self.__edges = {}
        self.__edgeslist = []
        self.__vertices = {}
        self.__distances = {}
        self.__times = {}

        return super().__init__(*args, **kwargs)

    def addVertice(self, vertice):
        if (self.hasVertice(vertice)):
            return

        v1Id = vertice.getId()
        self.__vertices[v1Id]=vertice
        if v1Id not in self.__edges:
            self.__edges[v1Id] = {}
        if len(vertice.getEdges())>0:
            for i,a in vertice.getEdges().items():
                #self.__edges[v1Id][a.getVertice2().getId()] = a
                self.__edges[v1Id][i] = a
                self.addVertice(a.getVertice2())

    def hasVertice(self, vertice):
        if (vertice.getId() in self.__vertices):
            return True
        return False
    def addEdge(self, edge):
        self.__createEdgesDictionary(v1,v2,False)

        self.__edges[arc.getVertice1().getId()][arc.getVertice2().getId()] = edge
        self.__edges[arc.getVertice2().getId()][arc.getVertice1().getId()] = edge
        self.__edgeslist.append(edge)
    
    def getVertices(self):
        return self.__vertices

    def addDistance(self,v1,v2,distance):
        self.__createArcsDictionary(v1,v2)

        self.__arcs[v1.getId()][v2.getId()].setDistance(distance)
        self.__arcs[v2.getId()][v1.getId()].setDistance(distance)

    def addTime(self,v1,v2,time):
        self.__createEdgesDictionary(v1,v2)

        self.__arcs[v1.getId()][v2.getId()].setTime(time)
        self.__arcs[v2.getId()][v1.getId()].setTime(time)

    def __createEdgesDictionary(self, v1, v2, create=True):
        newEdge = False
        v1Id = v1.getId()
        v2Id = v2.getId()
        if v2Id not in self.__edges[v1Id]:
            self.__edges[v1Id] = {}
            self.__edges[v1Id][v2Id] = {}
            newEdge = True
        if v1Id not in self.__edges[v2Id]:
            newEdge = True
            if create==False:
                self.__edges[v1Id][v2Id] = {}

        if newEdge and create:
            a = edge.edge(v1,v2)
            self.__edges[v1Id][v2Id] = a
            self.__edges[v2Id][v1Id] = a
            v1.addEdge(a)
            v2.addEdge(a)
            self.__edgeslist.append(a)

        return self.__edges[v1Id][v2Id]
            
    #def removeArc(self, v1, v2):
    #    v1.removeArc(v2);
    #    v2.removeInArc(v1);
    #    v1Id = v1.getId()
    #    v2Id = v2.getId()
    #    if v1Id not in self.__arcs:
    #        if v2Id not in self.__arcs[v1Id]:
    #            self.__arcs[v1Id].pop(v2Id)
    #    if v1Id not in self.__times:
    #        if v2Id not in self.__times[v1Id]:
    #            self.__times[v1Id].pop(v2Id)
    #    if v1Id not in self.__distances:
    #        if v2Id not in self.__distances[v1Id]:
    #            self.__distances[v1Id].pop(v2Id)

    def getEdges(self):
        return self.__edgeslist.copy()

    def __addDistance(self, a):
        v1 = a.getVertice1()
        v2 = a.getVertice2()
        if (v1.getId() not in self.__distances):
            self.__distances[v1.getId()] = {}
        self.__distances[v1.getId()][v2.getId()]=a.getDistance()

    def __addTime(self, a):
        v1 = a.getVertice1()
        v2 = a.getVertice2()
        if (v1.getId() not in self.__times):
            self.__times[v1.getId()] = {}
        self.__times[v1.getId()][v2.getId()]=a.getTime()
    
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

    def loadDistances(self, path):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="a":
            line = f.readline() 

        while len(line)>0 and line[0]=="a":
            arrayLine = line.strip().split(" ")
            v1 = self.getVertices()[int(arrayLine[1])]
            v2 = self.getVertices()[int(arrayLine[2])]

            a = self.__createEdgesDictionary(v1, v2, True)
            a.setDistance(arrayLine[3])
            v1.addDistance(v2,arrayLine[3])
            v2.addDistance(v1,arrayLine[3])
            self.__addDistance(a)

            line = f.readline() 

        f.close()

    def getDistanceKruscal(self, e):
        return e.getDistance()

    def kruskal(self):
        verticesdict = {}
        returnedges = []
        #edgessortedlist = self.__edgeslist.sort(key=lambda el: el.getDistance)

        edgessortedlist = sorted(self.__edgeslist, key=methodcaller('getDistance'))
        returncost = 0
        arvore = 0
        count=0
        arvores = {}
        for e in edgessortedlist:
            #if count%1000==0:
            #    print(count)
            count=count+1
            v1 = e.getVertice1().getId()
            v2 = e.getVertice2().getId()
            if (v1 not in verticesdict and v2 not in verticesdict):
                arvore = arvore + 1
                arvores[arvore]=[]
                arvores[arvore].append(v1)
                arvores[arvore].append(v2)
                verticesdict[v1]=arvore
                verticesdict[v2]=arvore
                returnedges.append(e)
                returncost=returncost+e.getDistance()
                continue
            elif (v1 not in verticesdict):
                verticesdict[v1]=verticesdict[v2]
                arvores[verticesdict[v2]].append(v1)
                returnedges.append(e)
                returncost=returncost+e.getDistance()
                continue
            elif (v2 not in verticesdict):
                verticesdict[v2]=verticesdict[v1]
                arvores[verticesdict[v1]].append(v2)
                returnedges.append(e)
                returncost=returncost+e.getDistance()
                continue
            elif verticesdict[v2]!=verticesdict[v1]:
                if len(arvores[verticesdict[v2]]) > len(arvores[verticesdict[v1]]):
                    arvsubstituir=verticesdict[v1]
                    arvnova = verticesdict[v2]
                else:
                    arvsubstituir=verticesdict[v2]
                    arvnova = verticesdict[v1]

                for i in arvores[arvsubstituir]:
                    verticesdict[i]=arvnova
                    arvores[arvnova].append(i)

                returnedges.append(e)
                arvores.pop(arvsubstituir)
                returncost=returncost+e.getDistance()
            

        return returncost,returnedges


    
        
    