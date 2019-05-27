import vertice
import arc
class loader(object):
    def loadVertices(path,graph):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="v":
            line = f.readline() 
        while len(line)>0 and line[0]=="v":
            arrayLine = line.strip().split(" ")
            v = vertice.vertice(arrayLine[1],arrayLine[2],arrayLine[3])
            graph.addVertice(v)
            line = f.readline() 

        f.close()
    
    def loadDistances(path, graph):
        f=open(path, "r")
        line = f.readline()      
        while line[0]!="a":
            line = f.readline() 

        while len(line)>0 and line[0]=="a":
            arrayLine = line.strip().split(" ")
            v1 = graph.getVertices()[arrayLine[1]]
            v2 = graph.getVertices()[arrayLine[2]]
            a = arc.arc(v1,v2,arrayLine[3])
            graph.addArc(a)
            line = f.readline() 

        f.close()

    def loadTimes(path, graph):
        return ""


