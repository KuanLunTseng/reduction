from algorithm import *
from copy import deepcopy as cpy 
from graph_class import *
from heap import *
from pysmt import *
from mfriend import *
    
def init_graph_toy_clique_problem():
  
    name = 'abcdef'
    vertices = [Vertex(n) for n in name]
    
    e1 = Edge((vertices[0], vertices[1]), directed=False)
    e2 = Edge((vertices[1], vertices[2]), directed=False)
    e3 = Edge((vertices[2], vertices[3]), directed=False)
    e4 = Edge((vertices[3], vertices[0]), directed=False)
    e5 = Edge((vertices[0], vertices[4]), directed=False)
    e6 = Edge((vertices[4], vertices[5]), directed=False)
    e7 = Edge((vertices[5], vertices[0]), directed=False)
    
    graph = Graph()
    
    edges = [e1, e2, e3, e4, e5, e6, e7]
    
    init_graph(graph, vertices, edges)
    
    return graph
    
def init_graph_mfriend(k):
    
    jfile = mfriend(k)
    vertices = [Vertex(j.name) for j in jfile]
    
    edges = []
    
    for j in jfile:
        for u in vertices:
            if j.name == u.name:
                for f in j.friend_list:
                    for v in vertices:
                        if v.name == f:
                            uv = Edge((u, v), directed=False)
                            edges.append(uv)
                            for e in edges:
                                if (uv.source.name, uv.target.name) == (e.source.name, e.target.name) or (uv.target.name, uv.source.name) == (e.source.name, e.target.name):
                                    pass
                                    
    
    graph = Graph()
    init_graph(graph, vertices, edges)
        
    return graph