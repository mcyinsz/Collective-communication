from typing import List
import copy
from .Node import Node

def complete_transmissions(nodes: List[Node]):
    # Get topological order of nodes (assuming we have a way to determine dependencies)
    topo_order = mrt_topological_sort(nodes)
    
    changed = True
    while changed:
        changed = False
        for node in topo_order:
            # Store current state to detect changes
            before = (len(node.receive_fifo), len(node.send_fifo) if node.send_fifo else 0)
            
            node.check()
            
            # Check if this call caused any changes
            after = (len(node.receive_fifo), len(node.send_fifo) if node.send_fifo else 0)
            if before != after:
                changed = True

# find the first <receive> node
def mrt_topological_sort(nodes:List[Node]):

    copied_nodes: List[Node] = copy.deepcopy(nodes)
    in_degree: List[int] = [len(node.receive_fifo) for node in nodes]
    order: List[Node] = []

    while not all(map(lambda x:x<0,in_degree)):

        # loop exists
        if all(map(lambda x:x>0,in_degree)):
            print("loop exists, return original order")
            return nodes

        # BFS
        stage_chosen_ids: List[int] = []

        for i,d in enumerate(in_degree):
        
            if d == 0:
                order.append(nodes[i])
                stage_chosen_ids.append(i)
                in_degree[i] = -1
            elif d == -1:
                stage_chosen_ids.append(i) 

        # each time step, each node could only send message once
        for chosen_id in stage_chosen_ids:
            if copied_nodes[chosen_id].send_fifo:
                send_pack = copied_nodes[chosen_id].send_fifo.popleft()
                in_degree[send_pack[0].id] -= 1
    
    return order