# Heap

## Parent-Child Relationship
Node	        Index
Left Child	    2 * i + 1
Right Child	    2 * i + 2
Parent	        ⌊(i - 1) / 2⌋ (floor division)


## heapify by default make it min-heap
- to make it max heap, we can use `-` sign to invert the values