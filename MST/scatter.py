from .utils import Node
from typing import List

# function for one node
def mst_scatter(
    node_list: List[Node],
    me: int,            # current node ID
    root: int,          # current tree root node
    left: int,          # current left bound
    right: int,         # current right bound
    depth: int = 0      # recursive depth   
):

    if left == right:
        return
    
    # mid point
    mid = (left + right) // 2
    
    # dest direction
    dest = right if root <= mid else left

    if root <= mid:
        # root node: send
        if me == root:
            print(f"[depth:{depth}]"+node_list[me].send(dest=node_list[dest], data_segment=(mid+1,right+1)))
        
        # dest node: receive
        elif me == dest:
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[root]))

    if root > mid:
        # root node: send
        if me == root:
            print(f"[depth:{depth}]"+node_list[me].send(dest=node_list[dest], data_segment=(left,mid+1)))
        
        # dest node: receive
        elif me == dest:
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[root]))

    # recurse direction
    if me <= mid:
        if root <= mid:
            # left sub tree, left root
            mst_scatter(node_list, me, root, left, mid, depth + 1)
        else:
            # left sub tree, right root
            mst_scatter(node_list, me, dest, left, mid, depth + 1)
    else:
        if root <= mid:
            # right sub tree, left root
            mst_scatter(node_list, me, dest, mid + 1, right, depth + 1)
        else:
            # right sub tree, right root
            mst_scatter(node_list, me, root, mid + 1, right, depth + 1)