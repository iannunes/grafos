import vertice
import edge
import graph
import directed_graph as dg
import matplotlib.pyplot as plt
from datetime import datetime
start_time = datetime.now()

g = graph.graph()

verticesfile = "datasets\\USA-road-d.NY.co"
distancesfile = "datasets\\USA-road-d.NY.gr"
timesfile = "datasets\\USA-road-t.NY.gr"
verticestestfile="datasets\\teste.co"
distancestestfile = "datasets\\teste.gr"
g.loadVertices(verticesfile)
g.loadDistances(distancesfile)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
#g.loadTimes(timesfile)

start_time = datetime.now()
c,e = g.kruskal()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

print (c, len(e), len(g.getVertices()))
#for item in e:
#    print (str(item.getVertice1().getId())+" - "+str(item.getVertice2().getId()))


#v1 = vertice.vertice(1,1,1)
#v2 = vertice.vertice(2,2,2)
#a = edge.edge(v1,v2,2,5)
#g.addVertice(v1)

#print(len(g.getVertices()))
#print(len(g.getEdges()))

#dgraph = dg.directed_graph()

#dgraph.loadVertices(verticesfile)
#dgraph.loadDistances(distancesfile)

#v = dgraph.getVertices()
#a = dgraph.getArcsDict()
#print(len(v))
#print(len(a))

#f=open(distancesfile, "r")
#line = f.readline()      
#while line[0]!="a":
#    line = f.readline() 

#counter=0
#founditem = {}
#founditemcount = 0
#while len(line)>0 and line[0]=="a":
#    arrayLine = line.strip().split(" ")
#    #v1 = self.getVertices()[arrayLine[1]]
#    #v2 = self.getVertices()[arrayLine[2]]
    
#    found=False
    
#    for i,a in dgraph.getArcsDict()[arrayLine[1]].items():
#        if (a.getVertice1().getId() == arrayLine[1] and a.getVertice2().getId() == arrayLine[2]):
#            found=True
#            if arrayLine[1]+"_"+arrayLine[2] in founditem:
#                print (line + "_" + a.getDistance())
#                founditemcount = founditemcount+1
#            founditem[arrayLine[1]+"_"+arrayLine[2]] = 1
#            break
    
#    if found==False:
#        print(line)

#    line = f.readline() 
#    counter = counter+1
    
#    if counter%50000==0:
#        print (counter)
#        end_time = datetime.now()
#        print('Duration: {}'.format(end_time - start_time))

#f.close()
#print (founditemcount)



end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))