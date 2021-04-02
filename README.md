# Python Classes and Methods

Python is an “object-oriented programming language.” This means that almost all the code is implemented using a special construct called classes. Programmers use classes to keep related things together. This is done using the keyword “class,” which is a grouping of object-oriented constructs.

By the end of this tutorial you will be able to:

1. Define what is a class
2. Describe how to create a class
3. Define what is a method
4. Describe how to do object instantiation
5. Describe how to create instance attributes in Python


## What is a class?

A class is a code template for creating objects. Objects have member variables and have behavior associated with them. In python a class is created by the keyword class.

An object is created using the constructor of the class. This object will then be called the instance of the class. In Python we create instances in the following manner:

```md
Instance = class(arguments)
```

## How to create a class?

The simplest class can be created using the class keyword. For example, let's create a simple, empty class with no functionalities.


```
>>> class Snake:
...     name = "python" # set an attribute `name` of the class
...
```

## Attributes and Methods in class:
A class by itself is of no use unless there is some functionality associated with it. Functionalities are defined by setting attributes, which act as containers for data and functions related to those attributes. Those functions are called methods.

### Attributes:
You can define the following class with the name Snake. This class will have an attribute name.

