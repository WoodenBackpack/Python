Loops and if statemets
**********************

=====
While
=====

  ::

    x = 0
    while x != 5:
      print(x)
      x += 1


==========
While else
==========

  ::

    x = 0
    while x != 5:
      print(x)
      x += 1
    else :
      print(x) # 5


===
For
===

* Iterate over list elements:

  ::
  
    l = ["element", 1 , ["a","b","c"]]
    for it in l:
      print(it)
    #"element"
    #1
    #["a", "b", "c"]

* Iterate over numbers in range:

  ::

    for it in range(1,5):
      print(it)
    #1
    #2
    #3
    #4

* Iterate over number in range with step:

  ::

    for it in range(1,10,2):
      print(it)
    #1
    #3
    #5
    #7
    #9   
   
* Inline for:

  ::

    l = [x for x in range(1,5)]
    print(l)
    >>>[1, 2, 3, 4]

    def increaseBy2(x):
      return x + 2

    l = [increaseBy2(x) for x in range(1,5)]
    print(l)
    >>>[3, 4, 5, 6]
  

