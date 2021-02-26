# p - position
# 2p - left child 2p + 1 right child
from typing import List

class BinHeap:

    def __init__(self) -> None:
        self.heap_list: List[int] = [0]
        self.current_size: int = 0

    def perc_down(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:#
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def perc_up(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:#
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:#
            return i * 2
        else:
            return i * 2 + 1

    def del_max(self) -> int:
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_up(1)
        return ret_val

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_up(i)
            i -= 1

    def insert(self, k) -> None:
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_down(self.current_size)

    def __repr__(self):
        return f'{self.heap_list} '



class PriorityQueue:

    def __init__ (self):
        self.heap = BinHeap()


    def enqueue(self, task, priority=0 ):
        self.heap.insert((priority,task))


    def dequeue(self):
        if self.heap.current_size == 0:
            raise ValueError("Empty Queue")
        return self.heap.del_max()

if __name__ == '__main__':

    p = PriorityQueue()
    p.enqueue('хопа', 32)
    p.enqueue('что-то' ,45)
    p.enqueue('хто-то', 424)
    p.enqueue('ниче-то', 4242)
    p.enqueue('пито-то', 4242)
    p.enqueue('ааа-то', 234)
    p.enqueue('бб-то', 53)
    p.dequeue()

    print(p.__dict__)




