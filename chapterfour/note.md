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


# Maximum Recursive Depth

Another danger in misuse of recursion is known asn an infinite recursion. If each recursive call makes another recursive call, without ever reaching a base case, then we have an infinite series of such calls.

You should make sure that each recursive call is progressing towards a base case.

Python places a limit on the number of activatioin records that can simultaneously  be active. This value is typically 1000.

If this limit is reached, a RuntimeError is raised with message, maximum recursion depth exceeded.

By default, python has a recursive depth limit set to around 1000, which should suffice for some computations, like a binary search that uses O (log n), for the recursive depth to be reached, there would need to be 2^1000 elements.

However, for some algorithms that have runtime proportional to n, this recursive depth could alter the way they function. Fortunatel, python provides a way to change the recursive limit dynamically.

``` python

import sys
old = sys.getrecursionlimit()
sys.setrecursionlimit(1000000)

```

While considering the maximum number of recursive calls that may be started from within the body of a single activation, we can classify recursion into the following.

- linear recursion -> this occurs when the recursive call starts atmost one other recursive call.

- binary recursion -> this occurs when the recursive call starts two others

- multiple recursion -> this occurs when a recursive call may start three or more others.

## Linear Recursion

The binary search algorithm is an example of linear recursion. The linear terminology reflects the structure of the recursion trace, not the asymptotic analysis of the running time.

# Note

A recursion tract is not the same as a call stack, a recursion tract shows the sequence of function calls and returns during recursive execution, While a call stack is a data structure  that keeps track of these active function calls. The stack operates in a LIFO manner.

