# Stacks, Queues, and Deques

The stack is an abstract data type or ADT that follows the LIFO principle, i.e last-in first-out. It has many areas of application such as the following:

- A web browser stores recently visited webpages in a stack, that way you can go back to previously visited pages.

- Text editors provide an undo functionality by storing recently performed operations in the stack in order to know how to reverse that operation.

# Operations Supported by a Stack ADT

1. push -> adds an item to the top of the stack.
2. pop -> removes and returns the item at the top of the stack, raises an error if the stack is empty.
3. top or peek -> returns a reference to the element at the top of the stack, raises an error if the stack is empty.
4. isempty -> returns true if the stack if empty.
5. len -> returns the length of the stack.

# The Adapter Pattern

The adapter design pattern applies to any context where we effectively want to modify an existing class so that its methods match those of a related, but different, class or interface.

A general way to apply the adapter pattern is to define a new class, in such a way that it contains an instance of the existing class as a hidden field, and then to implement each method of the new class using methods of the hidden instance variable.

the stack's lifo nature makes it a general tool to reverse a data sequence. For example, if the values 1, 2, and 3 are pushed onto a stack in that order, they will be popped from the stack in the order of 3,2,1

You can use a stack to reverse a sequence,this can be done by pushing each item of the sequence on to the stack, then poping from the stack bearing in mind that the last data would be poped out first.

example, reversing the contents of a file.


# Queues

Queues operate using the FIFO principle, where elements inserted into the queue are the first to exit the queue.

The queue adt supports the following methods for a queue Q:

Q.enqueue(e): Add elements e to the back of queue Q.
Q.dequeue(): Removes and return the first element from queue Q; an error occurs if the queue is empty.
Q.first(): Returns a reference to the element at the front of the queue Q. without removing it; an error occurs if the queue is empty.
Q.is_empty(): Return True if queue Q does not contain any elements.
len(Q): Return the number of elements in queue Q;

If an algorithm is of Θ(n), it means that the running time of the algorithm as n (input size) gets larger is proportional to g(n).

If an algorithm is of O(g(n)), it means that the running time of the algorithm as n gets larger is at most proportional to g(n).


# Double-Ended Queues

A double-ended queue is a queue-like data structure that supports insertion and deletion at both the front and th back of the queue.

It is also writen as deque, pronounced as deck.

The deque ADT Is defined so thet deque D supports the following methods:

D.add_first -> add an element to the front of the queue
D.add_last -> add an element to the back of the queue
D.delete_first -> remove an element from the front of the queue
D.delete_last -> remove an element from the back of the queue
D.first -> return the first element but dont remove, raise an exception if the queue is empty
D.last -> return but do not remove the last element, raise an exception if the deque is empty
D.is_empty -> return true if deque D does not contain any elements.
len(D) -> return the number of elements in deque D.

An implementation of a deque class is available in Python's standard collections module.

When you place a bound on the number of elements a deque can have, i.e when using the deque class from the collections module, and you append beyond the limit set, instead of throwing an error, an element is dropped to accomodate the new element added to the deque at that postion.

# Thoughts

So since lists in python are non-compact, I understand why we can have multiple data types inside a list, I guess this is because we can store the data at seperate locations in memory, and then add their reference into the list. since memory addresses all have the same size, we can still perform indexing in somewhat constant time.







