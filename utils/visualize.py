from .Node import Node
from typing import List

def list_node_datas(
    node_list: List[Node]
):
    for node in node_list:
        print(f"Node{node.id} data: {node.data}")