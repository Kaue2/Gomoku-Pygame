from queue import PriorityQueue
from Peca import Peca


class PriorityQueueGame:
    def __init__(self):
        self.queue = PriorityQueue()
    
    def enqueue(self, piece:Peca):
        self.queue.put(piece)

    def dequeue(self)->Peca:
        if(not self.queue.empty()):
            return self.queue.get()
        return None