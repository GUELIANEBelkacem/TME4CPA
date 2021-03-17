# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:01:20 2021

@author: Belkacem GUELIANE & Jae-Soo LEE
"""


from tme4Opt import *
import time
files = ["amazon.txt"]
for f in files:
    start = time.time()
    g = Graph(f)
    l = g.mkEdgeList()
    #m = g.mkAdjMatrix(l)
    a = g.mkAdjArray(l)
    end = time.time()
    print("creating EdgeList + AdjArray time is: "+ str(end-start)+"\n")
    
    k = KCore(l,a)
    k.getDegrees()
    start = time.time()
    k.kCore()
    end = time.time()
    print("KCore time is: "+ str(end-start)+"\n")
    k.getStats()
    
    
g = Graph("net.txt")
l = g.mkEdgeList()   
a = g.mkAdjArray(l)
k = KCore(l,a)
k.getDegrees()
start = time.time()
k.kCore()
end = time.time()
print("KCore time is: "+ str(end-start)+"\n")
k.getStats()
k.printVect()
k.plotCoreDegree()




















# import heapq
# class Node:
#     __slots__ = 'idn', 'neighbours'
#     def __init__(self, idn):
#         self.idn = idn
#         self.neighbours = []
#     def __lt__(self, other):
#         return (self.d < other.d) or ((self.d == other.d) and (self.idn < other.idn))

#     def __repr__(self):
#         return "Node "+ str(self.idn)
    
#     @property
#     def d(self):
#         return len(self.neighbours)

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)

# n2.neighbours.append(n3.idn)
# n2.neighbours.append(n1.idn)
# n2.neighbours.append(n4.idn)
# n4.neighbours.append(n2.idn)
# n3.neighbours.append(n2.idn)
# n1.neighbours.append(n2.idn)
# n1.neighbours.append(5)
# print(n3.d)
# print(n2.d)
# # initializing list 
# li = [ n2, n3, n4, n1 ] 
  
# # using heapify to convert list into heap 
# heapq.heapify(li) 
  
# # printing created heap 
# print ("The created heap is : ",end="") 
# print (list(li)) 

# n1.neighbours.clear()
# n1.idn = 44
# heapq.heapify(li) 
# print ("The created heap is : ",end="") 
# print (list(li)) 
# print(heapq.heappop(li))

  
# # using heappush() to push elements into heap 
# # pushes 4 
# # heapq.heappush(li, n1) 
# # heapq.heappush(li, n2) 
# # heapq.heappush(li, n3) 
# # heapq.heappush(li, n4) 
# # printing modified heap 
# print ("The modified heap after push is : ",end="") 
# print (list(li)) 
  
# # using heappop() to pop smallest element 
# print ("The popped and smallest element is : ",end="") 
# print (heapq.heappop(li)) 