import vertice
import arc
import graph

g = graph.graph()

verticesfile = "datasets\\USA-road-d.NY.co"
distancesfile = "datasets\\USA-road-d.NY.gr"
timesfile = "datasets\\USA-road-t.NY.gr"

g.loadVertices(verticesfile)
g.loadDistances(distancesfile)
g.loadTimes(timesfile)


v1 = vertice.vertice(1,1,1)
v2 = vertice.vertice(2,2,2)
a = arc.arc(v1,v2,2,5)
print(len(g.getVertices()))
print(len(g.getArcs()))
