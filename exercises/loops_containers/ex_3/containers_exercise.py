#!/usr/bin/python3

# 1. import module named csvReader
# 2. To check what classes/functions are provided by module type:
# >>> help(csvReader)
# 3. Read input file "players.csv" it's database of Major League Baseball Players
# 4. Output of reader is class CsvFileOutput with fields:
# header - list of columns names
# filename - name of readed file
# records - list of lists, each internal list have number of elements equal to length of header list
# Example:
# filename = "inputFile.csv"
# header = [name, surname]
# records = [
#   ["Jack", "Sparrow"],
#   ["Jacek", "Cygan"]
# ]
# 5. Create representation of each player in following form:
# {
#   Id: 1
#   Name: "Jack Sparrow"
#   Team: "BAL"
#   Position: "Relief Pitcher"
#   Height(centimeters): 175 // 1 inch ≈ 2.54 cm
#   Weight(kilograms): 60 // 1 pound ≈ 0.45 kg
#   Age(rounded up): 22
# }
