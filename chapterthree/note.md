# Algorithm Analysis

- The number of primitive operations an algorithm performs will be proportional to the actual running time of that algorithm.

- The running time of an algorithm may sometimes involve floor and ceiling operations.

ceiling -> the largest integer less than or equal to x
flooring -> the smallest integer greater than or equal to x


## Simple Justification Techniques

Sometimes, we will want to make claims about an algorithm, such as showing that it is correct or that it runs fast. In order to rigorously make such claims, we must use mathematical notations, and in order to back up such claims, we must justify or prove our statements.

Take for example, we say there is an element x and x E S and x has the property P, so in order for us to prove this statement true, we have to check the set S to see if there is any element x that has the property P. 

Example:
Professor Amongus claims that every number of the form 2^i - 1 is a prime, when I is an integer greater than 1. Professor Amongus is wrong.

Justification
To prove professor amongus wrong, we must find a couter example based on his statement. 


### Justification by Induction

This technique amounts to showing that, for any particular n >= 1, there is a finite sequence of implications that start with something known to be true and ultimately leads to showing that q(n) is true.

