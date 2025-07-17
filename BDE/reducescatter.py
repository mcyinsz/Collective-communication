import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import Node
from math import log2

from typing import List

def bde_reducescatter(
    node_list: List[Node],
    me: int,            # current node ID
    left: int,          # current left bound
    right: int,         # current right bound
    depth: int = 0      # recursive depth   
):
    
    if left == right:
        return
    
    size = right - left + 1
    assert log2(size).is_integer(), f"BDE algorithm has to implement on node array with size 2^p, get p={log2(size)}"

    mid = (left + right)//2

    if me <= mid:
        partner = me + (size // 2)
    else:
        partner = me - (size // 2)

    if me <= mid:
        print(f"[depth:{depth}]"+node_list[me].accumulate(dest=node_list[partner], data_segment=(mid+1, right+1)))
        print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[partner]))
    else:
        print(f"[depth:{depth}]"+node_list[me].accumulate(dest=node_list[partner], data_segment=(left, mid+1)))
        print(f"[depth:{depth}]"+node_list[me].recv(srce=node_list[partner]))

    if me <= mid:
        bde_reducescatter(node_list, me, left, mid, depth + 1)
    else:
        bde_reducescatter(node_list, me, mid+1,right, depth + 1)