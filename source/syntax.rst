Syntax in python
****************



Syntax in python can be a bit strange for Java or C++ developers because:\n

* There is no semicolons ; at the end of line

.. code-block:: python
  
  print("example")

* Indents are necessary

.. code-block:: python

  list = [1,4,3,2,1,6]
  for x in list:
    if x % 2 == 0:
      print(x)
  # 4,2,6

* Compiler will raise an error if you made any mistake in indentation:

:: 

  list = [1,4,3,2,1,6]
  for x in list:
    if x % 2 == 0:
        print(x)  # too much spaces here (4)
  >>>IndentationError: unindent does not match any outer indentation level 

* There is no need to name a type of variable in python, you can change a type of value in your code 

.. code-block:: python

  x = 2
  print(x)
  #>>>2
  x = "abc"
  print(x)
  #>>>abc

* Every variable is the reference to a object in memory but for small integers nad short strings it behaves different that in other cases

.. code-block:: python

  x = 20
  y = x
  y = 10
  print(x)
  #>>>20
  print(y)
  #>>>10

.. code-block:: python

  l1 = [1,2,3,4]
  l2 = l1
  l1[0] = 24
  print(l2)
  #>>>[24,2,3,4]

.. image:: ../images/pythonReferenceDiagram.png

