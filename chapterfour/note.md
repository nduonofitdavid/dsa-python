# Recursion

Recursion is a technique by which a function makes one or more calls to itself, or a data structure relies upon smaller instances of the very same type of structure in its representation.

When one invocation of a function makes a recursive call, the invocation is suspended until the recursive call completes.

## The factorial function

The factorial of a positive integer, n denoted as n! is the product of integers from 1 to n. if n=0, then n! = 1 by convention

The factorial function is important because it is known to equal the number of ways in which n distinct items can be arranged into a sequence, that is, the number of permutations of n items.

for example, abc can be arranged in 3! = 3 * 2 * 1 = 6 ways. abc, acb, bac, bca, cab, cba.

for a positive integer n, n! can be defined as n . (n - 1)!

since 5! = 5x4x3x2x1, it is the same as saying 5(5-1)! 

that is 5(4)!, 4! being 4x3x2x1 so 5(4x3x2x1).

The illustration of the execution of a recursive function is done using a recursion trace. Each entry of the trace corresponds to a recursive call.

In python, each time a function is called, a structure known as an activation record or frame is created to store information about the progress of the function.

In recursion, there is a different activation record for each active call.


## The english ruler

The english ruler is a simple example of a fractal, that is, a shape that has a self-recursive structure at various levels of magnification.

# Binary Search

The binary search algorithm is used to efficiently locate a target value within a sorted sequence of n elements. This algorithm is very important, and it is one of the reasons data is often stored in sorted order.

When the data is unsorted, the standard approach is to use a loop to iterate over all its elements until the target value is found or the data exhausted.

This is known as the sequential search algorithm. This algorithm runs in O(n) time, (i.e it has a linear runtime) since every element is inspected in the worst case.

The binary search algorithm allows us to quickly 'home in' on a target using a variant of a child's game called high-low.

An element in the sequence is called the candidate if at the current stage of the search, we cannot rule out that this is our target.

The median candidate is the item data mid with index

mid = [(low + high)/2]


# File Systems

Modern operating sytems store files in nested structures. The operating system allows directories to be nested arbitrarily deep (as long as there is enough space in memory), although there must be some base directories that contain only files, not further directories.

# Analyzing Recursive Algorithms

When analyzing the running time of recursive algorithms, we will account for each operation that is performed based upon the particular activation of the function that manages the flow of control at the time it is executed.

This means that for each invocation of the function, we only account for the number of operations that are performed within the body of that activation.

We can then account for the overall number of operations that are executed as part of the recursive algorithm by taking the sum, over all activations, of the number of operations that take place during each individual activation. This is also the way nonrecursive functions that call other functions from within its body are analysed.