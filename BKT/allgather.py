import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import Node

from typing import List

def bkt_allgather(
    node_list: List[Node],
    me: int,            # current node ID
    left: int,          # current left bound
    right: int         # current right bound  
):
    
    size = right - left + 1
    
    # logic ring
    prev = (me + size - 1) % size
    next = (me + 1) % size

    curi = me
    for _ in range(size-1): # only need to send size-1 elements(vector segments)
        print(node_list[me].send(dest=node_list[next],data_segment=(curi,curi+1)))
        curi = (curi + size - 1) % size
        print(node_list[me].recv(srce=node_list[prev]))