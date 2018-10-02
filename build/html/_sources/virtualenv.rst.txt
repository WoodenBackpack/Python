Virtualenv good way to separate and organize projects
*****************************************************

Virtualenv is very popular external module to create separated environment for your python project.
Module allows you to limit scope of variables, modules and set individual configuration like python executable version etc.

To install virtualenv type:

::

  `$ pip install virtualenv`

Then to setup in the simplest way type:

::
 
  `$ virtualenv <project_name>`

it will create '<project_name>/lib' and '<_project_name>/bin' directiories, with python executable and necessary scripts.

To start work with freshly created evironment type 

::
 
  `$ source bin/activate`

to end work with it:

::

  `$ deactivate`

see: https://virtualenv.pypa.io/en/stable/
