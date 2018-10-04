# Create a File manager
# File manager allows user to open and read file
# There are few file types but each has own way to print it
# * CSS file should print dictionary ie {"element": [rules] }
# style.css:
# A {
#  width: 50%
#  color: "black"
# } 
# B {
#  background-color: "grey"
# }
# print(cssFile)
# >>>A: width(50%), color("black")
# B: background-color("grey")


# * CSV file is raw representation of database each file represents one row
# First line represents a column names
# employees.csv:
# Id,Name,Age
# 1,Jacek,20
# 2,Aga,32
# 5,Iga,90
# string representation of CSV file should be a list of tuples

# output should be like:
# print(csvFile)
# >>>1 Jacek 20
# 2 Aga 32
# 5 Iga 90

# Usefull class elemnts:

# def __str__(self):
#   return "Hello"
# Allows You to use print() with myClass object

# def __enter__(self):
#   ... 
# def __exit__(self, type, vale, traceback)
#   ...
# Currently dont care about other parameters than self
# Allows You to use Your class in with ... as ..
# In example opening files with open method in "with" blocks works in this way:
# with open(filename) as inputFile:
#   ...
#   ...
# Here when we exit "with" block actions implemented in __exit__ will execute in this example function file.close() will be executed

# f = fileManager()
# f.readFile("style.css") << prints on screen
# f.readFile("employees.csv") << print formated 
