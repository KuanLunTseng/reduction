from graph_class import *
from heap import *
from problem_set import *
import math
from pysmt.shortcuts import *
from pysmt.typing import *
import random

#@profile
def clique_to_sat(graph, k):

    """
    Clique problem:
    
    For a given graph G = (V, E) and an integer k, the k-Clique problem is to find
    whether G contains a clique of size >= k
    
    Return a list of CNF clauses that encodes a clique problem to a SAT problem
    """
    clause = 0
    flatten = lambda list : [item for sublist in list for item in sublist]
    flat_vertices = flatten(copy_k_vertices(graph.vertices, k))
    variables = [Symbol(v.name, INT) for v in flat_vertices]
    first_formula = And([And(GE(v, Int(0)), LE(v, Int(1))) for v in variables])
    clause += 2*len(variables)
    
    # 1st Constraint
    temp_list = ([[v for v in variables if str(v)[-len(str(r)):] == str(r)] for r in range(k)])
    sum_first_constraint = [Equals(Plus(l), Int(1)) for l in temp_list]
    first_constraint = And(sum_first_constraint)
    clause += len(temp_list)
    
    # 2nd Constraint
    temp_list = [[v for v in variables if i.name == str(v)[:len(i.name)]] for i in graph.vertices]
    sum_second_constraint = And([LE(Plus(l), Int(1)) for l in temp_list])
    clause += len(temp_list)
    
    # 3rd Constraint
    non_edge_vertices = []
    non_edge_vertices = [((i, j)) for i in graph.vertices for j in graph.vertices if i != j and i not in j.neighbors]
    non_edge_group_variables = list(set([(Symbol(u.name+str(i), INT), Symbol(v.name+str(j), INT)) for j in range(k) for i in range(k) for (u, v) in non_edge_vertices if i != j]))
    third_constraint = And([Or(Not(Equals(u, Int(1))), Not(Equals(v, Int(1))))for (u, v) in non_edge_group_variables]) 
    phi = And(first_constraint, sum_second_constraint, third_constraint, first_formula)
    clause += len(non_edge_group_variables)
    return get_model(phi), clause
        
def is_clique(vertices):
    """
    We can think this function as an oracle that returns true if given set of vertices can form a clique, otherwise, false.
    Running time : O(n^2)
    """
    return(all(u in v.neighbors for u in vertices for v in vertices if u != v))
         
def brute_force_kclique(graph):
    """
    An oracle that tells the maximum size of clique in a given graph.
    """
    # 1-clique
    clique = [[v] for v in graph.vertices]
    
    # Exhaustive DFS search to find the maximum size clique in the given graph, extend solution from 1-cliques
    for c in clique:
        for v in graph.vertices:
            if v not in c:
                c.append(v)
                if not is_clique(c):
                    c.remove(v)
                    
    k = len(graph.vertices)
    ans = max(len(c) for c in clique)
    print('Maximum size of clique in graph size of %d is %d' % (k, ans))
    
    # print out all possible ways that forms a clique in a given graph
    #print([[v.name for v in c]for c in clique if len(c) == ans])
    return ans, [[v.name for v in c]for c in clique if len(c) == ans]
    
    
    
    
    
    
    
    
    