from queue import PriorityQueue

class PriorityQueueGame:
    def __init__(self):
        self.queue = PriorityQueue()
    
    def enqueue(self, piece):
        self.queue.put(piece)

    def dequeue(self):
        if(not self.queue.empty()):
            return self.queue.get()
        return None