Containters in python
*********************

====
List
====

  In python to declare a list insert a elements into square brackets:
  
  ::
  
    l = [1,2,3]
    l = list()
  
  There is no limitation in type of elements, same python list can contain string, integers, classes etc.
  
  ::
  
    l = [1, "element", 2.22, [2,3,4,5]]
  
  * To get a element form list type:
  
  ::
  
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[2]
    >>>Trusty Tahr
  
  * Get first 3 elements:
  
  ::
  
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[:3]
    >>["Bionic Beaver", "Xenial Xerus", "Trusty Tahr"]
  
  * Get last 2 elements:
  
  ::
  
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[-2:]
    >> ["Trusty Tahr", "Precise Pangoli"]
  
  * Get elements starts from the thirone:
  
  ::
  
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[2:]
    >>["Trusty Tahr", "Precise Pangoli"]
  
  * Get Elements without last one:
  
  ::
  
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[:-1]
    >>>["Bionic Beaver", "Xenial Xerus", "Trusty Tahr"]

  * Access elements in range:

  ::

    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l[1:3]
    >>>["Xenial Xerus", "Trusty Tahr"]

  * Add element:
  
  ::
  
    l = []
    l.apend("Bionic Beaver")
    l.append(2)
    l2 = [1,2,3]
    l.append(l2)
    print(l)
    >>>["Bionic Beaver", 2, [1,2,3]]

  * Remove element:
  
  ::

    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l.remove("Xenial Xerus")
    print(l)
    >>>["Bionic Beaver", "Trusty Tahr", "Precise Pangoli"]

  OR
  
  Remove and  return element with specified index
 
  ::

    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    l.pop()
    print(l)
    >>> l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr"]
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    removed = l.pop(2)
    print(l)
    >>> l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr"]
    print(remove)
    >>> Trusty Tahr
  
  OR

  ::

    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    del l[0]
    print(l)
    >>>["Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    
  del can also delete whole list


  ::
    l = ["Bionic Beaver", "Xenial Xerus", "Trusty Tahr", "Precise Pangoli"]
    del l
    print(l) // ERROR
    l no longer exist

  * Combining two tables:

  ::

    l = ["Bionic Beaver"]
    l2 = ["Xenial Xerus", "Trusty Tahr"]
    l3 = l1 + l2
    print(l3)
    >>>["Bionic Beaver", "Xenial Xerus", "Trusty Tahr"]

  * Multiplying tables:
  
  ::

    l = ["A", "B"]
    l2 = 3 * l
    print(l2)
    >>>["A", "B", "A", "B", "A", "B"]

======
Tuples
======

  * Tuples are created and accessible like lists but square brackets are replaced with round one. The main difference is that tuple elements and size cant be replaced with other ones:

  ::

    tup = (1,2,3)
    tup = tuple()
    tup = tuple([2,3,4,5])
    # tup[1] = 20 // ERROR, tuple elements cant be replaced


Replaced is the importat word because elements can't be replaced but can be changed:

  ::

    l = ["Bionic Beaver", "Xenial Xerus"]
    tup = (1, "element", l)
    print(tup)
    >>(1, "element", ["Bionic Beaver", "Xenial Xerus"])
    
    l[0] = "Gutsy Gibbon"
    print(tup)
    >>(1, "element", ["Gutsy Gibbon", "Xenial Xerus"])
    
    tup[2][1] = 2.2
    print(tup)
    >>(1, "element", ["Gutsy Gibbon", 2.2])

Tuples cannot be changes so del keyword can only delete whole tuple

  ::
   
    t = ("Bionic Beaver", "Xenial Xerus")
    del t
    print(t) // ERROR Tuple no longer exists
   
============
Dictionaries
============

Dictionaries are like maps in C++/Java to create empty dictionary type:

  ::
  
    d = {}
    s = dict()
    s = dict([(4.10, "Warty Warthog"), (5.04, "Hoary Hedgehog")])
    // create dictionary from list of two element tuples

* Accessing elements of dictionary:

  ::

    dict = {4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    print(dict[5.04])
    >>>"Hoary Hedgehog"

    # If key is not in the dictionary will be added
    dict[6.06] = "Dapper Drake"
    print(dict)
    >>>{4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 6.06:"Dapper Drake", 5.10:"Breezy Badger"}
    # Its important to notice that elements in dictionary are in random position

    # But if you want to access element with key that is not in dictionary it will raise a error
    print(dict[8.04])
    // ERROR
    
* There are two ways to get element from dictionary, but one protect developer from accessing elements that are not in dictionary

  ::
  
    dict = {4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    #print(dict[6.06])  // ERROR it will raise an KeyError exception
    print(dict.get(6.06))
    >>>None

* Iterate over keys/values/items these lists are always in the insertion order

  ::

    dict = {4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    for key in dict.keys():
      print(key) 
    #4.10
    #5.04
    #5.10

    for value in dict.values():
      print(value)
    # Warty Warthog
    # Hoary Hedgehog
    # Breezy Badger

    for (key, value) in dict.items():
      print(str(key) + " " + str(value))
    #4.10 Warty Warthog
    #5.04 Hoary Hedgehog
    #5.10 Breezy Badger

* Remove item with specified key from dictionary

  ::

    dict = {4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    del dict[4.10]
    print(dict)
    >>>{5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    # Same as for other containers del can also remove whole dictionary

  OR

  ::
   
    dict = {4.10:"Warty Warthog", 5.04:"Hoary Hedgehog", 5.10:"Breezy Badger"}
    removed = dict.pop(5.04)
    print(dict)
    >>>{4.10:"Bionic Beaver", 5.10:"Breezy Badger"}
    print(removed)
    >>>Hoary Hedgehog

The difference between del dict[key] and dict.pop() is that pop returns a removed element item value

====
Sets
====

* Create set

  Set like a dictionary is unordered.

  ::
 
    set = set()
    set = {1, 2, 3}
    
    l1 = {1:2} # dictionary
    l2 = {1,2} # set

    type(l1) == type(l2)
    >>>False

* Add element to set:
  
  ::
  
    set = {"Warty Warthog", "Hoary Hedgehog"}
    set.add("Breezy Badger")
    print(set)
    >>>{"Warty Warthog", "Hoary Hedgehog", "Breezy Badger"}
    other = {"Hoary Hedgehog", "Xenial Xerus"}
    set.update(other)
    print(set)
    >>>{"Warty Warthog", "Hoary Hedgehog", "Breezy Badger", "Xenial Xerus"}
    # Even if other will be changed it will no affect set
   
* Remove element from set:

  ::

    set = {"Warty Warthog", "Hoary Hedgehog"}
    set.remove("Warty Warthog")
    print(set)
    >>>{"Hoary Hedgehog"}

    set = {"Warty Warthog", "Hoary Hedgehog"}
    set.remove("Breezy Badger") // ERROR removing element that doesn't exists in set will raise an Exception
    
  To avoid raising exception You can use discard method:

  ::    

    set = {"Warty Warthog", "Hoary Hedgehog"}
    set.discaer("Breezy Badger")
    print(set)
    >>>{"Warty Warthog", "Hoary Hedgehog"}


