import pandas

new = pandas.read_csv("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/Untitled spreadsheet - Sheet1.csv")

print(new.shape[0])

ger = pandas.Series(new["German"])


# print(ger)
