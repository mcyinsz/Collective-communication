import os,sys
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from BDE import bde_allgather
from utils import Node, list_node_datas, complete_transmissions

def test_bde_allgather(
    node_num: int = 4, 
):
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    for i,node in enumerate(node_list):
        node.data = [0] * len(node_list)
        node.data[i] = 1


    for i,node in enumerate(node_list):
        bde_allgather(
            node_list=node_list,
            me=i,
            left=0,
            right=node_num - 1,
            depth = 0
        )
    
    complete_transmissions(node_list)

    list_node_datas(node_list)

if __name__ == "__main__":

    print("="*50)
    print("start testing BDE all-gather:")
    test_bde_allgather(
        node_num=16,
    )