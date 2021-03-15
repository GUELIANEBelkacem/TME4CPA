# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""
import time
import heapq
import matplotlib.pyplot as plt

class Edge:
    __slots__ = 'x', 'y'
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    
class Node:
    __slots__ = 'idn', 'neighbours'
    def __init__(self, idn):
        self.idn = idn
        self.neighbours = []
    def __lt__(self, other):
        return (self.d < other.d) or ((self.d == other.d) and (self.idn < other.idn))

    def __repr__(self):
        return "Node "+ str(self.idn)
    
    @property
    def d(self):
        return len(self.neighbours)
    def copyn(self):
        n= Node(self.idn)
        n.neighbours = self.neighbours[:]
        return n
            
        
class Graph:
    """ class Graph(String s) takes the path to the .txt file containing a list of edges.
        \n contains methids for generating an Edge List, an Adjacency Matrix and/or 
        an Adjacency Array, along with print methodes for all 3 data structures"""
    def __init__(self, s):
        self.s = s
        
    #data structure makers--------------------------------------------------
    
    def mkEdgeList(self):
        """ mkEdgeList() makes an edge list from the given .txt file inserted when creating an instance of Graph""" 
        listy = []
        f = open(self.s, "r")
        lines = f.readlines()
        for line in lines:
            temp = line.split()
            e = Edge(int(temp[0]), int(temp[1]))
            listy.append(e)
        f.close()
        print("number of edges: " + str(self.nedges(listy)))
        print("number of nodes: " + str(self.nnodes(listy))+"\n\n")
        return listy
    
    
    
    
    def mkAdjMatrix(self, l):
        """ mkAdjMatrix(EdgeList l) makes an adjacincy matrix from a given edge list""" 
        n = self.nnodes(l)
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ] 
        for e in l:
            matrix[e.x][e.y] = 1
        return matrix
    
    
    
    
    def mkAdjArray(self,l):
        """ mkAdjArray(EdgeList l) makes an adjacincy array from a given edge list""" 
        
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)
            listy[k.y].neighbours.append(k.x)
        return listy
    

    
    def mkadjarray2(self, l):
        """ mkAdjArray2(EdgeList l) makes an adjacincy array from a given edge list 
        with the particulatity of it turned into a directed graph 
        (useful for detecting triangles)""" 
        listy = {}
        n = self.nnodes(l)
        for i in range(n):
            listy[i] = (Node(i))
        for k in l:
            listy[k.x].neighbours.append(k.y)

        return listy
    
            
    #support functions------------------------------------------------------                     
    def nedges(self,listy):
        return len(listy)
    def nnodes(self,listy):
        s= 0
        for n in listy:
            if(s<n.x):
                s=n.x
            if(s<n.y):
                s=n.y
        return s+1
    
    #prints-----------------------------------------------------------------
    def print_edges(self, listy):
        f = open("EdgeList.txt", "w")
        for e in listy:
            f.write(str(e.x)+"   "+str(e.y)+"\n")
        f.close()    
    def print_matrix(self, matrix):
        f = open("AdjMatrix.txt", "w")
        s = ""
        f.write("the adjacency matrix:\n")
        s = ""
        for i in matrix:
            for j in i:
                s= s+(str(j) + " ")
            s= s+("\n")
            f.write(s)
        
        f.close() 
        
    def print_adjarray(self, listy):
        f = open("AdjArray.txt", "w")
        s = ""
        print("the adjacency array:\n")
        for i in listy:
            n = listy[i]
            s = ""
            s = s+str(n.idn)+" -> "            
            for neighbour in n.neighbours:
                s = s+str(neighbour)+" -> "
            s = s+"/\n"
            f.write(s)
            #print(s)
        f.close()


   
class KCore:
    
    def __init__(self, e, a):
        self.li = list(a.values())
        heapq.heapify(self.li) 
        self.edges = e
        self.nodes = a
        self.n = len(self.nodes)
        self.c = [-1 for i in range(self.n)]
        self.order = {}
        self.d = []
        self.coreValue = 0
    def getDegrees(self):
        for i in range(self.n):
            self.d.append(self.nodes[i].d)
        
    def kCore(self):
        n = self.n
        c = 0
        for i in range(n, 0, -1):
            #print(i)
            v = heapq.heappop(self.li)
            c = max(c, v.d)
            self.c[v.idn] = c
            self.order[v.idn] = i
            for nei in v.neighbours:
                temp = self.nodes[nei].copyn()
                temp.neighbours.remove(v.idn)
                self.li.remove(self.nodes[nei])
                heapq.heappush(self.li, temp) 
                self.nodes[temp.idn] = temp
            if(c>self.coreValue):
                self.coreValue = c
    def getStats(self):
        print("core value of the graph: " + str(self.coreValue))
        x = []
        for i in range(len(self.c)):
            if(self.c[i] == self.coreValue):
                x.append(self.d[i])
                
        averageDegreeDensity = sum(x) / (len(x)*2)
        print("evrage degree density: "+str(averageDegreeDensity))
        edgeDensity = (sum(x)/2)/((len(x)*(len(x)-1))/2)
        print("edge densty of the subgraph: "+str(edgeDensity))
        print("size of densest core: "+str(len(x)))
                     
    def plotCoreDegree(self):
        plt.figure()
        plt.scatter(self.d, self.c, )
        #plt.title("Coreness by Degree")
        plt.xlabel("Degree")
        plt.ylabel("Coreness")


    def printVect(self):
        f = open("cc.txt", "w")
        f2 = open("dd.txt", "w")
        for i in range(self.n):
            f.write(str(self.c[i])+"\n")
            f2.write(str(self.d[i])+"\n")
        f.close()
        f2.close()