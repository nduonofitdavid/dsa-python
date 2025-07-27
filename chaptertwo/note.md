# Chapter two summary

- For you to be able to iterate over your own self defined data structure, you have to provide a __next__ method for that data structure, this tells python how you want the value that would be returned when you call next on that data structure to be derived. You also need to define __iter__ method which tells python that that class supports iteration, by default this method should return **self**. 

- Another way to signify that a value can be iterated upon is to define the __getitem__ method and __len__ method for that data structure, with this, python automatically would implement iteration for you.


- An arithmetic progression adds a constant to one term of the progression to produce the next.

- In a geometric progression, each value is produced by multiplying the preceedidng value by a fixed constant.

In geometric we multiply a preceeding value by a constant while in arithmetic progression we add a constant to the preceeding value.


## Abstract Base Classes

- A class is considered an abstract base class if it cannot be instantiated directly, but rather its methods are implemented through a child class.

- Take progressions, you can define a base progression class which will serve as a scafold for other classes. But why define the base progression class as a concrete class, when you know it will not be instantiated, rather it serves as a blue print for other classes, instead you define it as an abc.

- A class is an abstract base class if its only purpose is to serve as a base class through inheritance.

- A metaclass provides a template for the class definition itself.

- The **template method pattern** is when an abstract base class provides concrete behaviours that rely upon calls to other abstract behaviours. Say we have a concrete method called visit_market, in the implementation of visit market, we can call an abstract behaviour dress_up, which might be different for different classes. This way as soon as the subclass provides definitions for the missing abstract behaviours, the inherited concrete behaviours are well defined.

- If the subclass does not provide concrete implementations for the abstract methods, python cancels instantiation for those sub classes.


## Namespaces

- A namespace is ab abstraction that manages all the identifiers that are defined in a particular scope, mapping each name to its associated value.