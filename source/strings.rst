Strings
*******

* Substring:

You can access a string in the same way as in list:

::

  a = "Example text"
  print(a[1:4])
  >>>xam


* Remove whitespaces:

You can remove whitespaces from the left side of string, right side or buth using strip() function

::

  a = "  Example text   "
  print(a.lstrip())
  >>>'Example text  '
  print(a.rstrip())
  >>>'   Example text'
  print(a.strip())
  >>>'Example text'

* Legth of string same as for containers:

::

  a = "Example text"
  print(len(a))
  >>>12

* Replace all occurences of string in string but not change orginal string:

::

  a = "Example text"
  print(a.replace("x", "TEXT")
  >>>ETEXTample teTEXTt

You can also replace only first x occurences:

::

  a = "Example text"
  print(a.replace("x", "XXX", 1)
  >>>EXXXample text
 
Split string by a characters and return list of elements divided by provided characters

::

  a = "Jan,Dlugosz,,,,12,15"
  print(a.split(","))
  >>>["Jan","Dlugosz","","","","12","16"]

Reverse operation to split() - join

::

  a = ["Jan", "Dlugosz", "", "", "", "12", "16"]
  print(",".join(a))
  >>>'Jan, Dlugosz, "", "", "", "12", "16"'


