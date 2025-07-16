import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import Node

from typing import List

def bde_allgather(
    node_list: List[Node],
    me: int,            # current node ID
    left: int,          # current left bound
    right: int,         # current right bound
    depth: int = 0      # recursive depth   
):
    
    if left == right:
        return
    
    size = right - left + 1

    mid = (left + right)//2

    if me <= mid:
        partner = me + (size // 2)
    else:
        partner = me - (size // 2)

    if me <= mid:
        bde_allgather(node_list, me, left, mid, depth + 1)
    else:
        bde_allgather(node_list, me, mid+1,right, depth + 1)

    if depth >= 0:

        if me <= mid:
            print(f"[depth:{depth}]"+node_list[me].send(dest=node_list[partner], data_segment=(left, mid+1)))
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[partner]))
        else:
            print(f"[depth:{depth}]"+node_list[me].send(dest=node_list[partner], data_segment=(mid+1, right+1)))
            print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[partner]))