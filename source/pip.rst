Pip your best friend to organise external modules
*************************************************

Pip is recomended tool for installing Python packages. From python versions 3.4+ pip is included by default
To check if pip is installed type:

:code:`pip --version`

To install known package type:

::

  pip install PACKAGE_NAME
  # for example to install django type:
  pip install django


There will be a lot of external modules required by your project to help you and other users be sure that all modules are downloaded with correct version pip allows to create file with module names to install all of them with one command. This file is named "requirements.txt" example file:

:: 

   tox
   mock
   pytest
   pytest-cov
   pytest-httpbin>=0.0.6
   docutils
   wheel
   pycodestyle 

so to easy install all of them type:

::
 
  `$ pip install -r requirements.txt`

