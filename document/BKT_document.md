# bucket collective communication

at each step, node `me` send one element to the neighbor node, first send the element the furthermost node requires.

* reduce-scatter: first send the `prev` element to the `next` node, at each step subtract element index
* all-gather: first send the `me` element to the `next` node, at each step accumulate element index

![alt text](/imgs/BKT.png)