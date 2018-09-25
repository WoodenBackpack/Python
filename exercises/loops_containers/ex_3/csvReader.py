#!/usr/bin/python3.6

class CsvFileOutput:
  def __init__(self, filename, header, records):
    self.fileName = filename
    self.header = header
    self.records = records

def readFromFile(filename):
  with open(filename) as csvFile:
    records = list()
    header = csvFile.readline()
    for record in csvFile.readlines():
      splitted = [x.replace('"', "") for x in record.split(",")]
      records.append(splitted)
    return CsvFileOutput(filename, header, records)

