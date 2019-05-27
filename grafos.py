import vertice
import arc
import graph
import loader

g = graph.graph()

verticesfile = "datasets\\USA-road-d.NY.co"
distancesfile = "datasets\\USA-road-d.NY.gr"
timesfile = "datasets\\USA-road-d.NY.gr"

loader.loader.loadVertices(verticesfile,g)
loader.loader.loadDistances(distancesfile,g)
loader.loader.loadTimes(timesfile,g)


v1 = vertice.vertice(1,1,1)
v2 = vertice.vertice(2,2,2)
a = arc.arc(v1,v2,2,5)
print(len(g.getVertices()))
print(len(g.getArcs()))
