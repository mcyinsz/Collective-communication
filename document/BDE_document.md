# bidirectional exchange collective communication

The whole process is splited into several stages, at each stage, the whole node chain would be splited into two halves,

* each node `me` would find its partner first, its partner is the node with the same relative position in the other half chain
* `me` would send the data segement which its partner requires, other half chain segment for reduce-scatter, current half chain segment for all-gather

![alt text](/imgs/BDE.png)