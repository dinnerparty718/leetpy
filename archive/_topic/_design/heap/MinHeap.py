'''
use a array for complete tree structure
storage = [0] * capacity
size = 0

parent i // 2

left child
    2i + 1
right child
    2i + 2


has parent
    i // 2 >= 0

has left child
    2i + 1 < size

has right child
    2i + 2 < size

is full
    size == capacity



insert 
    return if is full
    add to array end
        storage[size] = data
        size +=1
        heapifyUp(current_idx)
        
delete
    return if size == 0
    data =  storage[0]
    assign last itme value to storage[0]
    size -=1
    heapifyDown(current_idx)  current_idx = 0
    return data

heapifyUp - recursive
    if has_parent and parent > current val
        swap(idx1, idx2)
        heapifyUp(parent_idx)

heapifyDown - recursive
    if has no left child (has no child either, if leaf node)
        reutrn
    check left and right and determin the smaller index
    swap if current > smaller index
    heapifyDown(smaller index)

'''
# todo


class MinHeap:
    def __init__(self, capacity: int) -> None:
        pass
