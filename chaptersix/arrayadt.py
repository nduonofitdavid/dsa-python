from custom_excp import Empty

class ArrayStack:
    """This implementation of the stack adt uses a list for the adapter pattern"""
    def __init__(self):
        self._store = []
        self._idx = -1

    def push(self, k):
        """Add an item to the top of the stack"""
        self._store.append(k)

    def is_empty(self):
        return len(self._store) == 0

    def pop(self):
        """Remove an item from the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._store.pop()
    
    def top(self):
        """Return a reference to the item at the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._store[-1]
    
    def __iter__(self):
        """returns self by default"""
        return self
    
    def __next__(self):
        """definition on how to iterate over the stack"""
        try:
            item = self._store[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx -= 1
        return item
    
    def __len__(self):
        return len(self._store)
    

class ArrayQueueIneffcient:
    """An inefficient implementation of the Queue ADT using a list"""
    def __init__(self) -> None:
        self._store = []

    def enqueue(self, k) -> None:
        self._store.append(k)
    
    def is_empty(self) -> bool:
        return len(self._store) == 0

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty')
        return self._store.pop(0)
    
    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty')
        return self._store[0]
    
    def __len__(self):
        return len(self._store)
    

class ArrayQueue:
    """Efficient implementation of the Queue ADT using a list"""

    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        self._store = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        """return the number of elements in the queue."""
        return self._size
    
    def is_empty(self) -> bool:
        """return true if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """
        Returns a reference to the element at the front of the queue
        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._store[self._front]
    

    def dequeue(self):
        """Remove and return the first element of the queue"""

        if self.is_empty():
            raise Empty('The Queue is empty')
        answer = self._store[self._front]
        self._store[self._front] = None
        self._front = (self._front + 1 ) % len(self._store)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to a queue"""

        if self._size == len(self._store):
            self._resize(2 * len(self._store))
        avail = (self._front + self._size) % len(self._store)
        self._store[avail] = e
        self._size += 1
    

    def _resize(self, caap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._store
        self._store = [None] * caap
        walk = self._front
        for k in range(self._size):
            self._store[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


# enqueue ( front + no_of_elements ) % length of the array -> index to append to.
# dequeue ( front + 1 ) % length of the array -> new index for the front.

