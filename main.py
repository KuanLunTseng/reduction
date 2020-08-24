from algorithm import *
from graph_class import *
from heap import *
from memory_profiler import *
from problem_set import *
import sys
import time

if __name__ == "__main__":
    
    ## k-clique reduction test case
    # Example case
    if sys.argv[1] == '-e':
        graph = init_graph_toy_clique_problem()
        print(graph)
        print('')
        k, brute_ans = brute_force_kclique(graph)
        print(brute_ans)
        print('')
        sat_ans, clause = clique_to_sat(graph, k)    
        print(sat_ans)
        print('number of clauses in SAT solver: %d' % (clause))
        
    ## json file transform to a graph test case
    
    # Analysis mode
    if sys.argv[1] == '-a':
        for i in range(1, 100):
            #mem_usage = memory_usage(-1, interval=.2, timeout=1)
            graph = init_graph_mfriend(i)
            
            output = open('output.txt', 'a') 
            
            brute_time = time.time()
            k, brute_ans = brute_force_kclique(graph)
            brute_cost = time.time() - brute_time
            
            sat_time = time.time()
            sat_ans, clause = clique_to_sat(graph, k)
            sat_cost = time.time() - sat_time
            
            
            output.write("%s,%s,%s,%s\n" % (i, brute_cost, sat_cost, clause))
        