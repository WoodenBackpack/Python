Virtualenv good way to separate and organise projects
*****************************************************

Virtualenv is very popular external module to create separated environment for your python project.
Module allows you to limit scope of variables, modules and set individual configuration like python executable version etc.

To install virtualenv type:

:code: `$ pip install virtualenv`

Then to setup in the simplest way type:

:code: `$ virtualenv <project_name>`

it will create '<project_name>/lib' and '<_project_name>/bin' directiories, with python executable and necessary scripts.

To start work with freshly created evironment type 

:code: `$ source bin/activate`

to end work with it:

:code: `$ deactivate`

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

:code: `$ pip install -r requirements.txt`

see: https://virtualenv.pypa.io/en/stable/
