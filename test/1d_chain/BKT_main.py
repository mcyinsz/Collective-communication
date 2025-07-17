import os,sys
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from BKT import bkt_allgather, bkt_reducescatter
from utils import Node, list_node_datas, complete_transmissions

def test_bde_reducescatter(
    node_num: int = 4, 
):
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]

    for i,node in enumerate(node_list):
        node.data = [1] * len(node_list)


    for i,node in enumerate(node_list):
        bkt_reducescatter(
            node_list=node_list,
            me=i,
            left=0,
            right=node_num - 1,
        )
    
    complete_transmissions(node_list)

    list_node_datas(node_list)

def test_bde_allgather(
    node_num: int = 4, 
):
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    for i,node in enumerate(node_list):
        node.data = [0] * len(node_list)
        node.data[i] = 1


    for i,node in enumerate(node_list):
        bkt_allgather(
            node_list=node_list,
            me=i,
            left=0,
            right=node_num - 1
        )
    
    complete_transmissions(node_list)

    list_node_datas(node_list)

def test_bde_allreduce(
    node_num: int = 4, 
):
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    # (0+15) * 16 / 2 = 120
    # for i,node in enumerate(node_list):
    #     node.data = [j%len(node_list) for j in range(i, i+len(node_list))]
    for i,node in enumerate(node_list):
        node.data = [1] * len(node_list)

    for i,node in enumerate(node_list):
        bkt_reducescatter(
            node_list=node_list,
            me=i,
            left=0,
            right=node_num - 1
        )
    
    complete_transmissions(node_list)
    list_node_datas(node_list)

    for i,node in enumerate(node_list):
        bkt_allgather(
            node_list=node_list,
            me=i,
            left=0,
            right=node_num - 1
        )
    
    complete_transmissions(node_list)

    list_node_datas(node_list)

if __name__ == "__main__":

    print("="*50)
    print("start testing BDE all-gather:")
    test_bde_allgather(
        node_num=16,
    )

    print("="*50)
    print("start testing BDE reduce-scatter:")
    test_bde_reducescatter(
        node_num=8,
    )

    print("="*50)
    print("start testing BDE all-reduce:")
    test_bde_allreduce(
        node_num=16,
    )