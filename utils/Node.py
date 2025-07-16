from collections import deque
from .CommType import CommType
from typing import Tuple, Optional, List

class Node:
    
    def __init__(
        self, 
        node_id: int, 
        data_size: int = 0
    ):
        self.id: int = node_id          # node ID
        self.data_size = data_size
        self.data: List[int] = [0] * data_size  # data stored in node
        
        self.receive_fifo: deque[Node] = deque()
        self.send_fifo: deque[Tuple[Node,CommType,Tuple[int,int]]] = deque()
    
    def check(
        self
    ):
        # handle receive fifo
        while self.receive_fifo:

            source_node: Node = self.receive_fifo[0]
            
            if source_node.send_fifo:
                source_node_target: Node = source_node.send_fifo[0][0]
                comm_type: CommType = source_node.send_fifo[0][1]
                data_segment: Tuple[int,int] = source_node.send_fifo[0][2]
            else:
                break

            if source_node_target.id == self.id:
                
                # source_node.check()

                self.receive_fifo.popleft()
                source_node.send_fifo.popleft()

                if comm_type == CommType.SEND:
                    # print(f"[actual {source_node.id} -> {self.id}]", source_node.data[data_segment[0]: data_segment[1]])
                    self.data[data_segment[0]: data_segment[1]] = source_node.data[data_segment[0]: data_segment[1]]
                elif comm_type == CommType.ACCUMULATE:
                    self.data[data_segment[0]: data_segment[1]] = [self.data[i] + source_node.data[i] for i in range(*data_segment)]
            else:
                break
    
    def recv(
        self,
        srce: 'Node'
    ):
        
        self.receive_fifo.append(srce)    
        return f"[Receive] Node:{self.id} <-- Node:{srce.id}"

    def send(
        self,
        dest: 'Node',
        data_segment: Optional[Tuple[int, int]] = None
    ) -> str:
        
        data_segment = (0, self.data_size) if data_segment is None else data_segment
        assert data_segment[1] > data_segment[0], f"invalid data segment, {data_segment}"
        
        self.send_fifo.append((dest,CommType("send"), data_segment))
        return f"[Send] Node:{self.id} -- {data_segment} --> Node:{dest.id}"

    def accumulate(
        self,
        dest: 'Node',
        data_segment: Optional[Tuple[int, int]] = None
    ) -> str:
        
        data_segment = (0, self.data_size) if data_segment is None else data_segment
        assert data_segment[1] > data_segment[0], f"invalid data segment, {data_segment}"

        self.send_fifo.append((dest,CommType("accumulate"), data_segment))
        
        return f"[Accumulate] Node:{self.id} -- {data_segment} --> Node:{dest.id}"