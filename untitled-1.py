#!/usr/bin/python
from fractions import Fraction
graph = { 
    1: { 2: (1,10), 4: (3,10) },
    2: { 1: (1,10), 3: (5,10), 4: (1,10) },
    3: { 2: (5,10), 5: (3,10), 6: (3,10) },
    4: { 1: (3,10), 2: (1,10), 5: (1,10) },
    5: { 3: (3,10), 4: (1,10), 6: (7,10) },
    6: { 3: (3,10), 5: (7,10) }
}
graph_d_c={}
graph_lamda={}

def graph_2to1(graph,x):
    for key1, value1 in  graph.iteritems():
        for key2, value2 in graph[key1].iteritems():
            value=x*value2[0]+value2[1]
            value1.update({key2:value})
        graph_lamda.update({key1:value1})
def graph_reversal(graph):
    for key1, value1 in  graph.iteritems():
        for key2, value2 in graph[key1].iteritems():
            value1.update({key2:(value2[1],value2[0])})
        graph_d_c.update({key1:value1})
        
def graph1(graph):
    tem_dic1={}
    for key1, value1 in  graph.iteritems():
        tem_dic2={}
        for item in graph[key1]:
            tem_dic2.update({item:(graph[key1][item][1],graph[key1][item][0])})
        tem_dic1.update({key1:tem_dic2})
    return tem_dic1
def graph2(graph,x):
    tem_dic1={}
    for key1, value1 in  graph.iteritems():
        tem_dic2={}
        for item in graph[key1]:
            xvalue=graph[key1][item][1]+x*graph[key1][item][0]
            tem_dic2.update({item:xvalue})
            tem_dic1.update({key1:tem_dic2})
    return tem_dic1
            
print graph
print graph1(graph)
print graph
print "++++++++++++++++++++++++++++++++++++++++++++++"
print graph2(graph,Fraction(4,7))
print graph

      