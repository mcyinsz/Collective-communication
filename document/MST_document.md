# minimum spanning tree collective communication

## transmit logic (network perspective)

each time, split the chain to two parts, do the same thing for sub-chain.

![alt text](/imgs/MST.png)

## node behavior

let node index be `me`, the current operative node segment is (`left`, `right`), middle node index is (`left`+`right`)//2

* send/recv
    * if `me` is `root` node, send `me`->`dest`
    * if `me` is `dest` node, send `root`->`me`
    * for gather/scatter send data segment depends on the relative position between `me` and `mid` node
        * `me`  <-> `mid`: send(`left`, `mid`)
        * `mid` <-> `me`: send(`mid`+ 1, `right`)
* recursive process
    * the next sub-process for `me` is another same cc for a sub node segment
    * if `me` is at the different half node segment with `root` position, the next sub-process's root for `me` would be the current `dest`
    * the next sub-process's node segment is the half segment which consists `me`'s position

![alt text](/imgs/MST_node.png)
