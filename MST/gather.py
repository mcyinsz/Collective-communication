import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import Node

from typing import List

# function for one node
def mst_gather(
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
    srce = right if root <= mid else left
    
    # recurse direction
    if me <= mid:
        if root <= mid:
            # left sub tree, left root
            mst_gather(node_list, me, root, left, mid, depth + 1)
        else:
            # left sub tree, right root
            mst_gather(node_list, me, srce, left, mid, depth + 1)
    else:
        if root <= mid:
            # right sub tree, left root
            mst_gather(node_list, me, srce, mid + 1, right, depth + 1)
        else:
            # right sub tree, right root
            mst_gather(node_list, me, root, mid + 1, right, depth + 1)

    if root <= mid:
        # root node: send
        if me == srce:
            print(f"[depth:{depth}]"+node_list[me].accumulate(dest=node_list[root], data_segment=(mid+1,right+1)))
        
        # dest node: receive
        elif me == root:
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[srce]))
    if root > mid:
        # root node: send
        if me == srce:
            print(f"[depth:{depth}]"+node_list[me].accumulate(dest=node_list[root], data_segment=(left,mid+1)))
        
        # dest node: receive
        elif me == root:
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[srce]))