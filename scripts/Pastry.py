#!/usr/bin/python
import numpy as np
from collections import deque

def common_start(sa, sb):
    """ returns the longest common substring from the beginning of sa and sb """
    def _iter():
        for a, b in zip(sa, sb):
            if a == b:
                yield a
            else:
                return

    return ''.join(_iter())

def find_row_col(nodes_list=[], node="", node_size=6, row="", i=0):
    row_candidates = [-1] * node_size
    for idx, val in np.ndenumerate(row):
        tmp_candidates = []
        for n in nodes_list:
            if n[i] == str(idx[0]):
                common = common_start(n, node)
                if i == 0:
                    tmp_candidates.append(n)
                    break
                if i > 0 and len(common) >= i:
                    tmp_candidates.append(n)
                    break

        if len(tmp_candidates) > 0:
            row_candidates[idx[0]] = tmp_candidates[0]
    return list(row_candidates)

def printRoutingTable(nodes_list=[], node=-1, node_size=6):
    assert(node != -1)

    table = np.full_like(np.empty(len(node) * node_size, dtype=str), "").reshape(len(node), node_size)

    rown = 0
    new_table = None
    for row in table:
        result = np.array(find_row_col(nodes_list=nodes_list, node=node, row=row, i=rown, node_size=node_size))
        if new_table is not None:
            new_table = np.vstack((new_table, result))
        else:
            new_table = np.array(result)
        rown += 1

    print(new_table)

def printLeafSet(nodes_list=[], node_index=-1):
    assert(node_index != -1)
    nodes_list_pool = deque(nodes_list)
    _ = nodes_list_pool[node_index]
    nodes_list_pool.rotate(2)
    previous_2 = nodes_list_pool[node_index]
    nodes_list_pool.rotate(-1)
    previous_1 = nodes_list_pool[node_index]

    nodes_list_pool.rotate(-1)
    nodes_list_pool.rotate(-1)
    next_1 = nodes_list_pool[node_index]
    nodes_list_pool.rotate(-1)
    next_2 = nodes_list_pool[node_index]
    print("Leaf set:", [previous_2, previous_1, next_1, next_2])

nodes_list = ["0023","0113","0133","0322","1002","1010","1132","1223","2000","2112","2210","2231"]
nodes_list.sort(reverse=False)
node = "0023"
node_index = nodes_list.index(node)

printLeafSet(nodes_list=nodes_list, node_index=node_index)
printRoutingTable(nodes_list=nodes_list, node=node, node_size=4)

