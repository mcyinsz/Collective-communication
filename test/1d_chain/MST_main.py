import os,sys
import copy
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from MST import Node, mst_broadcast,list_node_datas, mst_reduce, complete_transmissions, mst_gather, mst_scatter

def test_mst_broadcast(
    node_num: int = 4,
    root_id: int = 1
):
    data = list(range(node_num))
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    node_list[root_id].data = data
    node_list[root_id].has_data = True
    
    for node_id in range(node_num):
        mst_broadcast(
            node_list=node_list,
            me=node_id,     
            root=root_id,    
            left=0,          
            right=node_num-1 
        )

    complete_transmissions(node_list)

    list_node_datas(node_list)

def test_mst_reduce(
    node_num: int = 4,
    root_id: int = 1
):
    data = list(range(node_num))
    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    for node in node_list:
        node.data = copy.deepcopy(data)
    
    for node_id in range(node_num):
        mst_reduce(
            node_list=node_list,
            me=node_id,     
            root=root_id,    
            left=0,          
            right=node_num-1 
        )
    
    complete_transmissions(node_list)
    list_node_datas(node_list)

def test_mst_gather(
    node_num: int = 4,
    root_id: int = 1
):

    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    for i,node in enumerate(node_list):
        node.data = [0] * len(node_list)
        node.data[i] = 1
    
    for node_id in range(node_num):
        mst_gather(
            node_list=node_list,
            me=node_id,     
            root=root_id,    
            left=0,          
            right=node_num-1 
        )
    
    complete_transmissions(node_list)
    list_node_datas(node_list)

def test_mst_scatter(
    node_num: int = 4,
    root_id: int = 1
):

    node_list = [Node(i, data_size=node_num) for i in range(node_num)]
    node_list[root_id].data = [1] * len(node_list)
    
    for node_id in range(node_num):
        mst_scatter(
            node_list=node_list,
            me=node_id,     
            root=root_id,    
            left=0,          
            right=node_num-1 
        )
    
    complete_transmissions(node_list)
    list_node_datas(node_list)

if __name__ == "__main__":

    print("="*50)
    print("start testing MST broadcast:")
    test_mst_broadcast(
        node_num=16,
        root_id=0
    )

    print("="*50)
    print("start testing MST reduce:")
    test_mst_reduce(
        node_num=16,
        root_id=1
    )

    print("="*50)
    print("start testing MST gather:")
    test_mst_gather(
        node_num=16,
        root_id=2
    )

    print("="*50)
    print("start testing MST scatter:")
    test_mst_scatter(
        node_num=16,
        root_id=3
    )