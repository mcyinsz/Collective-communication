# Collective Communication algorithms

## MST (minimum spanning tree)

* broadcast: (1 -> n)
* reduce: (n -> 1)
* scatter: (1 -> n)
* gather: (n -> 1)

![alt text](imgs/MST_node.png)

## BDE (bidirectional exchange)

* reduce-scatter: (n -> n)
* all-gather: (n -> n)

![alt text](imgs/BDE.png)

## BKT (bucket / ring algorithm)

* reduce-scatter: (n -> n)
* all-gather: (n -> n)

![alt text](imgs/BKT.png)