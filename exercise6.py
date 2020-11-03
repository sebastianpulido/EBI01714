#!/bin/python3

import math
from math import ceil, sqrt
import os
import random
import re
import sys
import math

def connectedSum(n, edges):
    # Write your code here
    print('n=', n)
    print('edges=', edges)
    
    result = 0
 
    # get nodes that are not in the edges list
    connected = set()
    isolated  = set()
    node_range = range(1, n + 1)
    for i in node_range:
        for e in edges:
            if str(i) in e:
                connected.add(i)

    for i in node_range:
        for e in edges:
            if str(i) not in e:
                if i not in connected:
                    isolated.add(i)

    print('connected=', connected)
    print('isolated=', isolated)
    
    # get sets of connected nodes
    links   = {}
    visited = {}

    nedges = range(int(len(edges)))
    for i in nedges:

        node1 = str(edges[int(i)]).split(' ')[0]
        node2 = str(edges[int(i)]).split(' ')[1]

        if not nodeInKeys(node1, visited):
            if not nodeInValues(node1, visited):
                visited.update({node1:node2})
                links.update({node1:1})
        
        elif nodeInKeys(node1, visited):
            if not nodeInValues(node1, visited):
                nvalue = int(links.get(node1)) + 1
                links.update({node1:nvalue})
                
        if nodeInKeys(node2, visited):
            nvalue = int(links.get(node2)) + 1
            links.update({node2:nvalue})
            links.pop(node1)

    print('links', links)

    result = getResult(isolated, links)
    print('result=', result)
    return result

def getResult(isolated, linked): 
    result = 0
    riso = range(1, len(isolated)+ 1)
    for i in riso:
        result += math.ceil(math.sqrt(1))

    for key, value in linked.items():
        result += ceil(sqrt(int(value) + 1))

    return result    

def nodeInKeys(node, d):
    for key, value in d.items():
        if node == key:
            return True
        else:
            return False

def nodeInValues(node, d):
    for key, value in d.items():
        if node == value:
            return True
        else:
            return False

def getKeyFromValue(val, d):
    for key, value in d.items():
        if val == value:
            return key

if __name__ == '__main__':
    n = 8
    edges = ['8 1', '5 8', '7 3', '8 6']
    connectedSum(n, edges)

    print('')
    n = 4
    edges = ['1 2', '2 4']
    connectedSum(n, edges)